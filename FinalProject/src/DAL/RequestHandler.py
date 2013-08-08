'''
Created on Mar 27, 2013

@author: eliran shemer bla
'''
import mysql.connector
import datetime
from HttpObjects import *
from time import strftime
from datetime import datetime
from Configuration.Config import Config
from DAL import ConnectorPool
       
class RequestsHandler:
        
    
    
    def insertRequest(self, req):
        cursor = ConnectorPool.ConnectorPool.GetConnector()
        #Handle requests table:
        add_requests=("INSERT INTO Requests "
                   "(Transactions_ID, method, http_version) "
                   "VALUES (%s, %s, %s)")
        data_requests=(req.transID, req.method, req.httpVersion)
        cursor.execute(add_requests, data_requests)
        self.cnx.commit()
        self.cnx.close()
        cursor.close()
    
    #Insert all requests in the given list to requests table on DB
    def insertRequestsList(self, reqList):
        cursor = self.cnx.cursor()
        for i in range(0, len(reqList)):
            add_requests=("INSERT INTO Requests "
                   "(Transactions_ID, method, http_version) "
                   "VALUES (%s, %s, %s)")
            data_requests=(reqList[i].transID, reqList[i].method, reqList[i].httpVersion)
            cursor.execute(add_requests, data_requests)
            cursor = ConnectorPool.ConnectorPool.CloseConnector()
    
    #Return a list of requests with the given transaction id    
    def getTransRequests(self, transID):
        cursor = ConnectorPool.ConnectorPool.GetConnector()
        #Handle requests table:
        cursor.execute("Select * from Requests where Transactions_ID="+str(transID))
        reqList=[]
        for (Req_ID, http_version, Transactions_ID, method) in cursor:
            request=Request.Request(Req_ID, http_version, Transactions_ID, method)
            reqList.append(request)
        cursor = ConnectorPool.ConnectorPool.CloseConnector()
        return reqList
    
    

#Testing:
r=RequestsHandler()
reqList=r.getTransRequests(308)
for i in range(0, len(reqList)):
    print(reqList[i].ID)
