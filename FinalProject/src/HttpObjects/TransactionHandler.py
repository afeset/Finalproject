'''
Created on May 1, 2013

@author: asaf
'''
import mysql.connector
import datetime
from time import strftime
from datetime import datetime
from HttpObjects import *
       
class ResponseHandler:
    cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='Project')
        
    
    
    #Insert a single Response to Responses table on DB
    