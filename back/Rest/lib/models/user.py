from uuid import uuid4
from datetime import datetime
from lib.const import *

# Class represents an User
class User() :
    def __init__(self, id:str, psn:str, version:str, date:str) :
        self.id = id # string GUID
        self.psn = psn # psn
        self.version = version # model version
        self.date = date # date of creation
    
    """ Create an User instance from a psn """
    @staticmethod
    def from_psn(psn:str) -> object :
        return User(str(uuid4()), psn, USER_MODEL_VERSION, str(datetime.now()))
    
    """ Create an User from a dic of parameters """
    @staticmethod
    def from_dic(dic:dict) -> object :
        return User(dic['id'], dic['psn'], dic['version'], dic['date'])
        
    """ Create an User from a tuple of parameters """
    @staticmethod
    def from_tuple(tpl:tuple) -> object :
        return User(tpl[0], tpl[1], tpl[2].replace(' ', ''), str(tpl[3]))
    
    """ Equality is only based on id """
    def __eq__(self, other):
        return self.id.upper() == other.id.upper() # sql server return uppercase for unique id

    def __str__(self): 
        return "User : (id=%s, psn=%s, version=%s, date=%s" % (self.id, self.psn, self.version, self.date) 