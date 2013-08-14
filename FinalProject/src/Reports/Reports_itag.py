'''
Created on Jun 3, 2013

@author: asaf
'''

#This query returns the percentage of itag values from all transactions:

import mysql.connector
cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='Project')
cursor = cnx.cursor()

#Get only distinct values of itag:
cursor.execute("SELECT DISTINCT(Value) FROM `Requests-Params` WHERE Name_request_param='itag'")
distinct=cursor.fetchall()
count=[]

#Omit redundant characters from results and count occurrences of each distinct itag value:
for i in range (0, len(distinct)):
    distinct[i]=(str(distinct[i]))[3:-3]
    distinct[i]=int(distinct[i]) #Need to find out how to recognize relevant characters
    cursor.execute("SELECT COUNT(*) from `Requests-Params` where Name_request_param='itag' AND Value="+str(distinct[i]))
    temp=cursor.fetchone()
    count.append(temp[0])
print("itag Statistics:\n")
print("The distinct values of itag in coal are:")
print(distinct)
print("\n")
print("Their matching count is:")
print(count)
print("\n")

#Calculate percentage in terms of transactions:
cursor.execute("SELECT Count(*) FROM Transactions")
total=cursor.fetchone()
percent_trans=[]
for i in range (0, len(count)):
    temp=100*float(count[i])/float(total[0])
    percent_trans.append(temp)
print("Percentage in terms of transactions (indices match the distinct itag vector):")
print(percent_trans)
print("\n")
#Calculate percentage in terms of bytes:
cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions")
sum_of_bytes_total=cursor.fetchone()
percent_bytes=[]
for i in range (0, len(distinct)):
    cursor.execute("SELECT SUM(NumDownloadedBytes) from Transactions where ID=ANY (SELECT Transactions_ID FROM Requests where Req_ID=ANY (SELECT Request_ID from `Requests-Params` where Name_request_param='itag' AND Value="+str(distinct[i])+"))")
    temp1=cursor.fetchone()
    temp2=100*float(temp1[0])/float(sum_of_bytes_total[0])
    percent_bytes.append(temp2)
    
print("Percentage in terms of bytes (indices match the distinct itag vector):")
print(percent_bytes)



cursor.close()
cnx.commit()
cnx.close()