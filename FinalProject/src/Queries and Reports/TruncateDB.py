'''
Created on Mar 13, 2013

@author: asaf
'''
import mysql.connector
cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='Project')
cursor = cnx.cursor()
all_tables=["Flow","Transactions", "Requests", "Requests-Params", "Requests-Headers", "Requests-PathSeg", "Responses", "Responses-Headers"]
table=raw_input("Choose a table to truncate.\nNote: You can also type All to truncate all tables")
yn=raw_input("are you sure??? This will delete all data in the table and its children (Y/N)")
if(yn=="Y"):
    if (table=="All"):
        for i in range (0,8):
            cursor.execute("TRUNCATE `"+str(all_tables[i])+"`")
        print("All tables have been truncated!")
    else:
        cursor.execute("TRUNCATE `"+str(table)+"`")
        print(str(table)+" has been truncated!")
cnx.commit()
cursor.close()
cnx.close()