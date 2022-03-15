from lib.services.connectionService import ConnectionService

""" Insert a connection id """
def create(id:str) -> None :
    ConnectionService(id).create()
    
""" Remove a connection id"""
def remove(id:str) -> None :
    ConnectionService(id).remove()

""" Select all id stored in the db """
def selectAll() -> list :
    return ConnectionService.selectAll()
    
