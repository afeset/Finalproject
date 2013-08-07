'''
Created on Jun 1, 2013

@author: asaf
'''
#This query returns the percentage of itag values from all transactions:
from DAL import ConnectorPool
import mysql.connector
from Configuration.Config import Config
from HttpObjects.HTTP_Constants import UserAgent

class RequestsWithItagPercentageReport:
    
    def __init__(self, StartDate, EndDate):
        self.StartDate=StartDate
        self.EndDate=EndDate
        self.distinct=0
        self.count=0
        self.percent_trans=0
        self.percent_bytes=0
        
    def loadResults(self):
        cnx = mysql.connector.connect(user=Config.USER, password=Config.PASSWORD, host=Config.HOST, database=Config.DATABASE)
        cursor = cnx.cursor()
        #Get only distinct values of itag:
        cursor.execute("SELECT DISTINCT(Value) FROM `Requests-Params` WHERE Name_request_param='itag'")
        self.distinct=cursor.fetchall()
        self.count=[]
        
        #Omit redundant characters from results and count occurrences of each distinct itag value:
        for i in range (0, len(self.distinct)):
            self.distinct[i]=(str(self.distinct[i]))[3:-3]
            self.distinct[i]=int(self.distinct[i]) #Need to find out how to recognize relevant characters
            cursor.execute("SELECT COUNT(*) from `Requests-Params` where Name_request_param='itag' AND Value="+str(self.distinct[i]))
            temp=cursor.fetchone()
            self.count.append(temp[0])
            
        #Calculate percentage in terms of transactions:
        cursor.execute("SELECT Count(*) FROM Transactions")
        total=cursor.fetchone()
        self.percent_trans=[]
        for i in range (0, len(self.count)):
            temp=100*float(self.count[i])/float(total[0])
            self.percent_trans.append(temp)
        
        #Calculate percentage in terms of bytes:
        cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions")
        sum_of_bytes_total=cursor.fetchone()
        self.percent_bytes=[]
        for i in range (0, len(self.distinct)):
            cursor.execute("SELECT SUM(NumDownloadedBytes) from Transactions where ID=ANY (SELECT Transactions_ID FROM Requests where Req_ID=ANY (SELECT Request_ID from `Requests-Params` where Name_request_param='itag' AND Value="+str(self.distinct[i])+"))")
            temp1=cursor.fetchone()
            temp2=100*float(temp1[0])/float(sum_of_bytes_total[0])
            self.percent_bytes.append(temp2)
 
        cursor.close()
        cnx.commit()
        cnx.close()
        
    def PrintReportResults(self):
        print("itag Statistics:\n")
        print("The distinct values of itag in coal are:")
        print(self.distinct)
        print("\n")
        print("Their matching count is:")
        print(self.count)
        print("\n")
        print("Percentage in terms of transactions (indices match the distinct itag vector):")
        print(self.percent_trans)
        print("\n")
        print("Percentage in terms of bytes (indices match the distinct itag vector):")
        print(self.percent_bytes)
        

r=RequestsWithItagPercentageReport(1,1)
r.loadResults()
r.PrintReportResults()