from lib.services.db import Database
import sqlalchemy

""" Service to interact with the games table (using sqlalchemy)"""
class GameService() :
    table = None
    __table_name__ = 'GameTable'
    """ Init the service : game -> current game"""
    def __init__(self, game) :
        self.game = game
        GameService.table = Database.init(GameService.__table_name__)
    
    """ Create a game based on current (passed in constructor)"""
    def createGame(self) -> None :
        Database.insert(GameService.table, (self.game.id, str(self.game.board), self.game.player1.id, self.game.player2.id, self.game.player, self.game.date, self.game.version))
        
    """ Get the game that is being played"""
    @staticmethod
    def getCurrentGame() -> object :
        if GameService.table == None :
            GameService.table = Database.init(GameService.__table_name__)
        query = sqlalchemy.select([GameService.table]).order_by(GameService.table.c.date.desc())
        return Database.session.execute(query.limit(1)).fetchall()[0]
    
    """ Update the actual game with the current (passed in constructor)"""
    def play(self) :
        query = sqlalchemy.update(GameService.table).where(GameService.table.c.id == self.game.id).values({GameService.table.c.board : str(self.game.board), GameService.table.c.player : not self.game.player})
        Database.session.execute(query)
    
    """ Set actual game winner : player -> true if player1 """
    def setWinner(self, player:bool) :
        query = sqlalchemy.update(GameService.table).where(GameService.table.c.id == self.game.id).values({GameService.table.c.winner_player : player})
        Database.session.execute(query)