'''
Created on Mar 13, 2013

@author: asaf
'''
import mysql.connector
cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='Project')
cursor = cnx.cursor()
file_name=raw_input("Choose a table to delete from.\nNote: You can also type All to delete all data")
yn=raw_input("are you sure??? This will delete all data in the table and its children (Y/N)")
if(yn=="Y"):
    if (file_name=="All"):
        cursor.execute("DELETE FROM Flow")
        print("All data has been deleted!")

    else:
        cursor.execute("Delete FROM `"+str(file_name)+"`")
        print(str(file_name)+" table data has deleted")
    
cnx.commit()
cursor.close()
cnx.close()