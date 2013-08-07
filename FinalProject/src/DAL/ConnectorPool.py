
import mysql.connector
from Configuration.Config import Config

_name_ = 'ConnectorPool'

class ConnectorPool:
    cnx = mysql.connector.connect(user=Config.USER, password=Config.PASSWORD, host=Config.HOST, database=Config.DATABASE)
    cursor = cnx.cursor()
    
    @staticmethod
    def GetConnector():
        cnx = mysql.connector.connect(user=Config.USER, password=Config.PASSWORD, host=Config.HOST, database=Config.DATABASE)
        cursor = cnx.cursor()
        return cursor
        
    @staticmethod
    def CloseConnector():
        ConnectorPool.cursor.close()
        ConnectorPool.cnx.commit()
        ConnectorPool.cnx.close()   

