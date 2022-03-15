from lib.services.db import Database
import sqlalchemy

""" Service to interact with the connection table (using sqlalchemy)"""
class ConnectionService() :
    table = None
    __table_name__ = 'ConnectionTable'
    def __init__(self, connectionID) :
        self.connectionID = connectionID
        ConnectionService.table = Database.init(ConnectionService.__table_name__)
    
    """ Construct table for static call """
    @staticmethod
    def Init() :
        if ConnectionService.table == None :
            ConnectionService.table = Database.init(ConnectionService.__table_name__)
            
    """ Insert a connection id """
    def create(self) -> None :
        print(self.connectionID)
        Database.insert(ConnectionService.table, (self.connectionID,))
    
    """ Remove a connection id"""
    def remove(self) -> None :
        query = ConnectionService.table.delete().where(ConnectionService.table.c.connectionID == self.connectionID)
        Database.session.execute(query)
    
    """ Select all id stored in the db """
    @staticmethod
    def selectAll() -> list :
        ConnectionService.Init()
        query = sqlalchemy.select([ConnectionService.table])
        return Database.session.execute(query).fetchall()