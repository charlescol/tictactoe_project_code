from uuid import uuid4
from datetime import datetime
from lib.const import *
from lib.models.board import Board
import random

# Class represents the game state
class State :
    DRAW = 0,
    WIN = 1,
    NOT_FINISHED = 2
    
# Class represents a game
class Game() :
    def __init__(self, id:str, board:object, player1:object, player2:object, player:bool, date:datetime, version:str, winner_player=None) :
        self.id = id # string GUID
        self.board = board # Board
        self.player1 = player1 # User instance for player 1
        self.player2 = player2 # User instance for player 2
        self.player = player # last player who played (true for player 1)
        self.date = date # date of game creation
        self.version = version # model version
        self.winner_player = winner_player # true for player 1 has won, null if neither or if the game is in progress
        
    """ Create a Game from the players' User instances """
    @staticmethod
    def from_players(player1:object, player2:object) -> object :
        return Game(str(uuid4()), Board(), player1, player2, bool(random.getrandbits(1)), str(datetime.now()), GAME_MODEL_VERSION)
    
    """ Create a Game from a dic of parameters """
    @staticmethod
    def from_dic(dic:dict) -> object :
        board = Board.from_string(dic['board'])
        return Game(dic['id'], board, dic['player1'], dic['player2'], dic['player'], dic['date'], dic['version'])
    
    """ Create a Game from a tuple of parameters """
    @staticmethod
    def from_tuple(tpl:tuple) -> object :
        board = Board.from_string(tpl[1])
        return Game(tpl[0], board, tpl[2], tpl[3],  tpl[4], str(tpl[5]), tpl[6].replace(' ', ''), tpl[7])
