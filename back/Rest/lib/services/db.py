import sqlalchemy

""" Generic Database Class using sqlalchemy"""
class Database() :
    session = None
    metadata = None
    def __init__(self):
        raise RuntimeError('Cannot instanciate object Database')
    
    """ Init connection to database and return table associated to the string passed as argument """   
    @staticmethod
    def init(tableName:str) -> object :
        if Database.session == None and Database.metadata == None: # if the connection is established for the first time
            engine = sqlalchemy.create_engine("mssql+pyodbc://"+os.environ.get('username')+":"+os.environ.get('mdp')+"@"+os.environ.get('dbserver')+".c4v8gfe7914t.us-east-1.rds.amazonaws.com:1433/"+os.environ.get('dbname')+"?driver=ODBC+Driver+17+for+SQL+Server")
            Database.session = engine.connect()
            Database.metadata = sqlalchemy.MetaData(bind=engine)
        return sqlalchemy.Table(tableName, Database.metadata, autoload = True)# 
    
    """ Generic method to insert element in table """
    @staticmethod
    def insert(table:object, values:tuple) -> None :
        if Database.session != None :
            query = table.insert().values(values)
            Database.session.execute(query)
    
    """ Close Database """
    @staticmethod
    def close() :
        Database.session.close()
