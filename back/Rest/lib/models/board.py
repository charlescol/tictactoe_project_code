from lib.const import *

""" Class represents a board """
class Board() :
    def __init__(self, *args) :
        self.version = BOARD_MODEL_VERSION
        if len(args) > 0 : 
            self.board_list = args[0]
        else :
            self.board_list = self.generate()
    
    """ Generate an empty board """
    def generate(self) -> list :
        return [''] * 9
    
    """ Get value at index """
    def get(self, index) :
        return self.board_list[index]
    
    """ Set a value at index """
    def set(self, position:int) -> list :
        self.board_list[position] = self.getNextSymbole()
    
    """ Given the current state, returns the most present symbol. return const.GAME_SYMBOLE1 if same"""
    def getNextSymbole(self) :
        symbol = GAME_SYMBOLE1
        if self.board_list.count(GAME_SYMBOLE1) > self.board_list.count(GAME_SYMBOLE2) : 
            symbol = GAME_SYMBOLE2
        return symbol
    
    """ Create a Board from  """
    @staticmethod
    def from_string(boardString:str) -> object:
        return Board(boardString.replace(' ','').split(','))
        
    """ String conversion of Board """
    def __str__(self):
        return str(self.board_list).replace("'", '').replace(' ','').strip("][")