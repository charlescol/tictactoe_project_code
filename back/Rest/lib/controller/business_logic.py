from lib.const import *
from lib.services.gameservice import GameService
from lib.models.board import *
from lib.models.game import *
from lib.services.userservice import UserService
from lib.models.user import User
from ressources import *
from broadcast import Hub

""" Get the two current players """
def get_players() -> tuple:
    players = UserService.getPlayers()
    if len(players) == 2 :
        return User.from_tuple(players[0]), User.from_tuple(players[1])
    elif len(players) == 1 : # if only one, return it in a tuple
         return User.from_tuple(players[0]),
    return ()

""" Get user from id string """
def get_user(id) -> object :
    return User.from_tuple(UserService.getFromID(id)[0])

""" Get all psn from database """   
def getAll_psn() -> list:
    return [p[1] for p in UserService.getAllPlayers()]

""" Business logic for user creation """
def create_user(user:User) -> None :
    service = UserService(user) # create service
    if len(user.psn) > MAX_PSN_SIZE or len(user.psn) < MIN_PSN_SIZE : # throw exception if user doesn't match 
        raise ValueNotMatchError
    if service.userExists() :
        raise UserNotAllowedError
    
    begin_new = (len(get_players()) == 1)
    service.insertUser()
    Hub.broadcast_message("user+"+str(','.join(getAll_psn()))) # Broadcast the new list of users
    if begin_new : # if the user is the second to join
        create() # create a game 
    elif len(getAll_psn()) > 2 : # if not participating to the game
        game = get_currentGame()
        Hub.broadcast_message("board+"+str(game.board)+"+"+game.player1.psn+"+"+game.player2.psn+"+"+str(game.player)+"") # Broadcast current game state for new specators

""" Business logic for user deletion """
def remove_user(user:User) -> None:
    user_service = UserService(user) # create service
    players = get_players() # Get the two game players
        
    if len(players) == 2 and (user == players[0] or user == players[1]) : # if this user is participating to the current game
        GameService(get_currentGame()).setWinner(user != players[0]) # the other wins
        user_service.removeUser() # remove the user
        create() # create a new game based on the new user list
    else :
        user_service.removeUser() # else just remove from database
    Hub.broadcast_message("user+"+str(','.join(getAll_psn()))) # broadcast the new list of users

""" Business logic for the winner calculation, return true if the parameter -player- has won in the -game- """
def isWinner(player:object, game:object) -> bool:
    conditions = [(0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6), (0,3,6), (1,4,7), (2,5,8)] # list of possibilities for win
    symbol = get_playerSymbol(game, player)
    for condition in conditions :
        if game.board.get(condition[0]) == symbol and game.board.get(condition[1]) == symbol and game.board.get(condition[2]) == symbol :
            return True
    return False

""" Get the player symbol. The calculation is based on the game state and the player order in the game """
def get_playerSymbol(game:object, player:object) -> str:
    next_symbol = game.board.getNextSymbole()
    if (player == game.player1 and game.player) or (player == game.player2 and not game.player):  return next_symbol
    if next_symbol == GAME_SYMBOLE1 : return GAME_SYMBOLE2
    else : return GAME_SYMBOLE1
    
""" Business logic for game creation"""
def create() -> Game :
    players = get_players() # get current game players
    if len(players) != 2 :  # if not enough players
        Hub.broadcast_message("board+"+str(Board())+"+++") # broadcast an empty board to all clients
        return None
    
    game = Game.from_players(players[0], players[1]) # create a new game based on players
    GameService(game).createGame() 
    Hub.broadcast_message("board+"+str(game.board)+"+"+game.player1.psn+"+"+game.player2.psn+"+"+str(game.player)+"") # broadcast the new board
    return game
    
""" Get the game which is actually being played """
def get_currentGame() -> Game:
    game = Game.from_tuple(GameService.getCurrentGame())
    players = get_players()
    game.player1 = players[0]
    game.player2 = players[1]
    return  game

# Return a game state based on -player- and the actual -game-
def isGameFinished(player:object, game:object) -> State: 
    if isWinner(player, game)  :
        return State.WIN
    elif len(str(game.board)) >= 17:
        return State.DRAW
    return State.NOT_FINISHED

# Business logic for new moves"""
def playedEvent(player:object, index:int) -> None:
    game = get_currentGame() # get actual game
    if (player != game.player1 and not game.player) or (player != game.player2 and game.player) : # throw error if -player- not participating
        raise UserNotAllowedError 
    if game.board.board_list[index] == '' : # if index is empty in the board
        game.board.set(index) # update the index
        service = GameService(game) # update the game
        service.play()
        result = isGameFinished(player, game)
        if result == State.NOT_FINISHED :  # if game not finished
            Hub.broadcast_message("board+"+str(game.board)+"+"+game.player1.psn+"+"+game.player2.psn+"+"+str(game.player)+"") # broadcast the new board
            return  
        if result == State.WIN: service.setWinner(not game.player) # create a new game if finished
        create()
    else :
        raise ValueNotMatchError 