from lib.services.db import Database
import sqlalchemy

""" Service to interact with the users table (using sqlalchemy)"""
class UserService() :
    table = None
    __table_name__ = 'UserTable'
    """ Init the service : user -> current user"""
    def __init__(self, user) :
        self.user = user
        UserService.table = Database.init(UserService.__table_name__) # get table
    
    """ insert the current user """
    def insertUser(self) -> None :
        Database.insert(UserService.table, (self.user.id, self.user.psn, self.user.version, self.user.date))
        
    """ Construct table for static call """
    @staticmethod
    def Init() :
        if UserService.table == None :
            UserService.table = Database.init(UserService.__table_name__)
            
    """ Get the two current players """
    @staticmethod
    def getPlayers() -> list :
        UserService.Init()
        query = sqlalchemy.select([UserService.table]).order_by(UserService.table.c.date)
        return Database.session.execute(query.limit(2)).fetchall()
    
    """ Get all player, including all players in the queue """
    @staticmethod
    def getAllPlayers() -> list :
        UserService.Init()
        query = sqlalchemy.select([UserService.table]).order_by(UserService.table.c.date)
        return Database.session.execute(query).fetchall()
    
    """ get a list of users from list of id : id -> list of id"""
    @staticmethod
    def getFromID(id:list) -> list:
        UserService.Init()
        query = sqlalchemy.select([UserService.table]).where(UserService.table.c.id == id)
        return Database.session.execute(query).fetchall()
        
    """ Return true if current user already exists """
    def userExists(self) -> bool :
        query = sqlalchemy.select([UserService.table]).where(UserService.table.c.psn == self.user.psn)
        return Database.session.execute(query).first() != None
    
    """ Remove current user from database """
    def removeUser(self) -> None :
        query = UserService.table.delete().where(UserService.table.c.id == self.user.id)
        Database.session.execute(query)