'''
Created on Mar 13, 2013

@author: asaf
'''
#This query returns txt files with content of all tables to tmp folder (file system- /tmp)

import mysql.connector
import subprocess
cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='Project')
cursor = cnx.cursor()
file_name=["Flow", "Transactions", "Requests", "Requests-Params", "Requests-Headers", "Requests-PathSeg", "Responses", "Responses-Headers"]
for i in range(0,7):
    string_to_use="rm -f /tmp/"+str(file_name[i])+".txt" #If the file already exists, delete it
    subprocess.call(string_to_use, stdin=None, stdout=None, stderr=None, shell=True) #Execute the above in Terminal
    cursor.execute("SELECT * from `"+str(file_name[i])+"` into outfile '/tmp/"+str(file_name[i])+".txt'") #Query and write to file
    print(str(file_name[i])+" table data has been written to tmp folder")
cnx.commit()
cursor.close()
cnx.close()