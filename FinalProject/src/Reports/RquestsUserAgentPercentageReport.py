'''
Created on Jun 1, 2013

@author: asaf
'''

from DAL import ConnectorPool
import mysql.connector
from Configuration.Config import Config
from HttpObjects.HTTP_Constants import UserAgent

class RquestsUserAgentPercentageReport:
    
    def __init__(self, HeaderName, StartDate, EndDate):
        self.HeaderName=HeaderName
        self.StartDate=StartDate
        self.EndDate=EndDate
        self.NumberOfTransactionsResult=0
        self.NumberOfBytesResult=0
        
    def loadResults(self):
        cursor = ConnectorPool.ConnectorPool.GetConnector()
        #Percentage in terms of number of transactions:
        cursor.execute("SELECT Count(*) FROM Transactions")
        total=cursor.fetchone()
        cursor.execute("SELECT Count(*) FROM `Requests-Headers` WHERE Header_Name LIKE '%user-agent%' AND (Value LIKE '%"+UserAgent.Nativehost+"%' OR Value LIKE '%"+UserAgent.PS3+"%' OR Value LIKE '%"+UserAgent.Playstation+"%' OR Value LIKE '%"+UserAgent.Xbox+"%' OR Value LIKE '%"+UserAgent.Zune+"%')")
        count=cursor.fetchone()
        if total[0] == 0 :
            print ("Empty Database - cannot complete calculation\n")
        else :
            self.NumberOfTransactionsResult=100*(float(count[0])/float(total[0]))
        
        #Percentage in terms of number of bytes:
        cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions")
        sum_of_bytes_total=cursor.fetchone()
        cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions WHERE ID= ANY (SELECT Transactions_ID FROM Requests WHERE Req_ID= ANY (SELECT Request_ID FROM `Requests-Headers` WHERE Header_Name LIKE '%user-agent%' AND (Value LIKE '%"+UserAgent.Nativehost+"%' OR Value LIKE '%"+UserAgent.PS3+"%' OR Value LIKE '%"+UserAgent.Playstation+"%' OR Value LIKE '%"+UserAgent.Xbox+"%' OR Value LIKE '%"+UserAgent.Zune+"%')))")
        sum_of_bytes_begin=cursor.fetchone()
        if sum_of_bytes_total[0] == None :
            print ("Empty Database - cannot complete calculation\n")
        else :
            self.NumberOfBytesResult=100*float(sum_of_bytes_begin[0])/float(sum_of_bytes_total[0])
        
        ConnectorPool.ConnectorPool.CloseConnector()
        
    def PrintReportResults(self):    
        print("Problematic user agents: PS3, playstation, xbox, nativehost, zune\n")
        print("Percentage of Requests with user problematic user agents:\n")
        print("In terms of number of transactions:")
        print(self.NumberOfTransactionsResult)

        print("Problematic user agents: PS3, playstation, xbox, nativehost, zune\n")
        print("Percentage of Requests with user problematic user agents:\n")
        print("In terms of bytes:")
        print(self.NumberOfBytesResult)
     
    

r=RquestsUserAgentPercentageReport(1,1,1)
r.loadResults()
r.PrintReportResults()      

