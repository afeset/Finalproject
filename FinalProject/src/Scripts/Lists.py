import mysql.connector
import datetime
from time import strftime
from datetime import datetime
from HttpObjects import *


#Retrieve Max Transactions ID from DB:
cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='Project')
cursor = cnx.cursor()
cursor.execute("SELECT max(ID) FROM Transactions")
t=cursor.fetchone()
cursor.close()
cnx.close()

#Create empty lists and initialize variables:
translist=[]
reslist=[]
main_count=0;
count=0;

#Insert from Miner to lists:
def createLists(coal, req, res):

    #Create Objects:
    
    #Transactions object ('trans'):
    d=datetime.now()
    trans_time=datetime.fromtimestamp(int(coal.unixTime)).strftime('%Y-%m-%d %H:%M:%S')
    cgid=coal.decoding.cgid
    cid=coal.decoding.cid
    sitename='Static-YOUTUBE'
    duration=coal.DurationMili
    client_ip=coal.flow.clientIP.text
    client_dest_port=coal.flow.clientPort
    server_ip=coal.flow.serverIP.text
    server_dest_port=coal.flow.serverPort
    checksum=coal.decoding.checksum1k10k
    trans=Transaction.Transaction((), d, trans_time, cgid, cid, sitename, duration, client_ip, client_dest_port, server_ip, server_dest_port, checksum)
    translist.append(trans)
    
    #Responses object ('resp'):
    t1=t[0]+len(translist)
    response_code=res.statusCode
    if(response_code==204):
        count=count+1
    resp=Response.Response((), t1, response_code)
    reslist.append(resp)

    return {'translist':translist, 'reslist':reslist, 'count':count, 'main_count':main_count}

    #Use the above function to get lists and print different variables
    def getLists(coal, req, res):
        result=createLists(coal, req, res)
        print("Number of Responses with Response Code of 204 is:")
        print(result['count'])
        print("The Percentage of these responses out of all responses is:")
        p=result['count']/result['main_count']
        print(p)
    '''translist=result['translist']
    reslist=result['reslist']
    print("Transactions list length:")
    print(len(translist))
    print("last transaction is:")
    translist[len(translist)].printTransaction(translist[len(translist)])
    print("Responses list length:")
    print(len(reslist))
    print("last response is:")
    reslist[len(reslist)].printResponse(reslist[len(reslist)])'''



