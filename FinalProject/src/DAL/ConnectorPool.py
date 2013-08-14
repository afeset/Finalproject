
import mysql.connector
from Configuration.Config import Config

_name_ = 'ConnectorPool'
#git test12
class ConnectorPool:
    #cnx = mysql.connector.connect(user=Config.USER, password=Config.PASSWORD, host=Config.HOST, database=Config.DATABASE)
    #cursor = cnx.cursor()
    cnx=0
    cursor=0
    
    @staticmethod
    def GetConnector():
        if(ConnectorPool.cursor==0):
            ConnectorPool.cnx = mysql.connector.connect(user=Config.USER, password=Config.PASSWORD, host=Config.HOST, database=Config.DATABASE)
            ConnectorPool.cursor = ConnectorPool.cnx.cursor()
        return ConnectorPool.cursor
        
    @staticmethod
    def InitConnector():
        if(ConnectorPool.cursor==0):
            ConnectorPool.cnx = mysql.connector.connect(user=Config.USER, password=Config.PASSWORD, host=Config.HOST, database=Config.DATABASE)
            ConnectorPool.cursor = ConnectorPool.cnx.cursor()
        
    
    @staticmethod
    def Execute(command):
        if(ConnectorPool.cursor!=0):
            return ConnectorPool.cursor.execute(command) 
        return -1
                    
    @staticmethod
    def CloseConnector():
        if(ConnectorPool.cursor != 0):
            ConnectorPool.cursor.close()
            ConnectorPool.cursor=0
        if(ConnectorPool.cnx!=0):
            ConnectorPool.cnx.commit()
            ConnectorPool.cnx.close()
            ConnectorPool.cnx=0   

