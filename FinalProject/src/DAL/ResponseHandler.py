'''
Created on Apr 19, 2013

@author: asaf
'''
import mysql.connector
import datetime
from time import strftime
from datetime import datetime
from HttpObjects import *
from Configuration.Config import Config
       
class ResponseHandler:
    cnx = mysql.connector.connect(user=Config.USER, password=Config.PASSWORD, host=Config.HOST, database=Config.DATABASE)    
    
    #blabla
    #Insert a single Response to Responses table on DB
    def insertResponse(self, res):
        cursor = self.cnx.cursor()
        add_responses=("INSERT INTO Responses "
                   "(Transactions_ID, Response_Code) "
                   "VALUES (%s, %s)")
        data_responses=(res.transID, res.response_code)
        cursor.execute(add_responses, data_responses)
        self.cnx.commit()
        self.cnx.close()
        cursor.close()
    
    #Insert all Responses in a given list to Responses table on DB
    def insertResponsesList(self, resList):
        cursor = self.cnx.cursor()
        for i in range(0, len(resList)):
            add_responses=("INSERT INTO Responses "
                   "(Transactions_ID, Response_Code) "
                   "VALUES (%s, %s, %s)")
            data_responses=(resList[i].transID, resList[i].response_code)
            cursor.execute(add_responses, data_responses)
        self.cnx.commit()
        self.cnx.close()
        cursor.close()
    
    #Insert a single Response Header to Responses-Headers table on DB
    def insertResHeader(self, resheader):
        cursor = self.cnx.cursor()
        add_resp_headers=("INSERT INTO `Responses-Headers` "
               "(Response_ID, Name_response_header, Value) "
               "VALUES (%s, %s, %s)")
        data_resp_headers=(resheader.Response_ID, resheader.Name_response_header, resheader.Value)
        cursor.execute(add_resp_headers, data_resp_headers)
        self.cnx.commit()
        self.cnx.close()
        cursor.close()
   
    #Insert all Response Headers in a given list to Responses-Headers table on DB
    def insertResHeadersList(self, resheaderList):
        cursor = self.cnx.cursor()
        for i in range(0, len(resheaderList)):
            add_responses=("INSERT INTO `Responses-Headers` "
                   "(Response_ID, Name_response_header, Value) "
                   "VALUES (%s, %s, %s)")
            data_responses=(resheaderList[i].Response_ID, resheaderList[i].Name_response_header, resheaderList[i].Value)
            cursor.execute(add_responses, data_responses)
        self.cnx.commit()
        self.cnx.close()
        cursor.close()
        
    
    #Sample Query1: Return a list of responses with the given transaction id    
    def getTransResponses(self, transID):
        cursor = self.cnx.cursor()
        cursor.execute("Select * from Responses where Transactions_ID="+str(transID))
        resList=[]
        for (ID, Transactions_ID, Response_Code) in cursor:
            response=Response.Response(ID, Transactions_ID, Response_Code)
            resList.append(response)
        self.cnx.commit()
        self.cnx.close()
        cursor.close()
        return resList


#Testing1:
print("Test1:")
r=ResponseHandler()
resList=r.getTransResponses(308)
for i in range(0, len(resList)):
    print(resList[i].response_code)

#Testing2:
print("Test2:")
res=Response.Response(308,308,204)
res.printResponse(res)

#Testing3:
print("Test3:")
resheader=ResHeader.ResHeader(15,16,17,18)
resheader.printResHeader(resheader)
