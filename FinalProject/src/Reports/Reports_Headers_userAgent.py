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
cursor.execute("SELECT Count(*) FROM Transactions")
total=cursor.fetchone()
cursor.execute("SELECT Count(*) FROM `Requests-Headers` WHERE Header_Name LIKE '%user-agent%' AND (Value LIKE '%nativehost%' OR Value LIKE '%PS3%' OR Value LIKE '%playstation%' OR Value LIKE '%xbox%' OR Value LIKE '%zune%')")
count=cursor.fetchone()
if total[0] == 0 :
    print("Empty Database")
else :
    result=100*(float(count[0])/float(total[0]))
    print("Problematic user agents: PS3, playstation, xbox, nativehost, zune\n")
    print("Percentage of Requests with user problematic user agents:\n")
    print("In terms of number of transactions:")
    print(result)

#Percentage in terms of number of bytes:
cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions")
sum_of_bytes_total=cursor.fetchone()
cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions WHERE ID= ANY (SELECT Transactions_ID FROM Requests WHERE Req_ID= ANY (SELECT Request_ID FROM `Requests-Headers` WHERE Header_Name LIKE '%user-agent%' AND (Value LIKE '%nativehost%' OR Value LIKE '%PS3%' OR Value LIKE '%playstation%' OR Value LIKE '%xbox%' OR Value LIKE '%zune%')))")
sum_of_bytes_begin=cursor.fetchone()
if sum_of_bytes_total[0] == 0 :
    print ("Empty Database")
else :
    result=100*float(sum_of_bytes_begin[0])/float(sum_of_bytes_total[0])
    print("In terms of bytes:")
    print(result)


cursor.close()
cnx.commit()
cnx.close()
