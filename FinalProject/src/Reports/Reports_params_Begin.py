'''
Created on Jun 1, 2013

@author: asaf
'''

#This query returns the percentage of requests with uri_param "begin", out of all requests in that coal file

import mysql.connector
cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='Project')
cursor = cnx.cursor()

#Percentage in terms of number of transactions:
cursor.execute("SELECT COUNT(*) FROM `Transactions`")
total=cursor.fetchone()
cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='begin'")
count=cursor.fetchone()
result=(float(count[0])/float(total[0]))
print("Percentage of Requests with 'begin' URI param (all values):")
print("In terms of number of transactions:")
print(result)
no_begin_percent=1-result
#Percentage in terms of number of bytes:
cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions")
sum_of_bytes_total=cursor.fetchone()
cursor.execute("select SUM(NumDownloadedBytes) from Transactions where ID=(select Transactions_ID from Requests where Req_ID=(select Request_ID from `Requests-Params` where Name_request_param='begin'))")
sum_of_bytes_begin=cursor.fetchone()
result=float(int(sum_of_bytes_begin[0] or 0))/float(sum_of_bytes_total[0])
no_begin_bytes=1-result
print("In terms of bytes:")
print(result)
print("\n")

#Non-begin requests:

print("Percentage of Requests WITHOUT 'begin' URI param:")
print("In terms of number of transactions:")
print(no_begin_percent)
print("In terms of bytes:")
print(no_begin_bytes)
print("\n")

#Percentage only of begin=0, transactions:
cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='begin' AND Value='0'")
count=cursor.fetchone()
result=(float(count[0])/float(total[0]))
print("Percentage of Requests with 'begin'=0:")
print("In terms of number of transactions:")
print(result)
#Percentage only of begin=0, bytes:
cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions WHERE ID=(select Transactions_ID from Requests where Req_ID=(select Request_ID from `Requests-Params` where Name_request_param='begin' and Value='0'))")
sum_of_bytes_begin=cursor.fetchone()
result=float(int(sum_of_bytes_begin[0] or 0))/float(sum_of_bytes_total[0])
print("In terms of bytes:")
print(result)
print("\n")

#Percentage only of begin!=0, transactions:
cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='begin' AND Value!='0'")
count=cursor.fetchone()
result=(float(count[0])/float(total[0]))
print("Percentage of Requests with 'begin'!=0:")
print("In terms of number of transactions:")
print(result)
#Percentage only of begin!=0, bytes:
cursor.execute("select SUM(NumDownloadedBytes) from Transactions where ID= ANY(select Transactions_ID from Requests where Req_ID= ANY(select Request_ID from `Requests-Params` where Name_request_param='begin' and Value!='0'))")
sum_of_bytes_begin=cursor.fetchone()
result=float(int(sum_of_bytes_begin[0] or 0))/float(sum_of_bytes_total[0])
print("In terms of bytes:")
print(result)

cursor.close()
cnx.commit()
cnx.close()