'''
Created on Feb 19, 2013

@author: asaf
First draft for YouTube
'''
import mysql.connector
import datetime
from time import strftime
from datetime import datetime
from Configuration.Config import Config

def pushToDB(coal, req, resp):
    cnx = mysql.connector.connect(user=Config.USER, password=Config.PASSWORD, host=Config.HOST, database=Config.DATABASE)
    cursor = cnx.cursor()
#  bla
    #Get values from miner and print them out for testing
    print ("cgid is:")
    cgid=coal.decoding.cgid
    print (cgid)
    print ("cid is:")
    cid=coal.decoding.cid
    print (cid)
    print ("Duration in miliseconds is:")
    duration=coal.DurationMili
    print (duration)
    print ("Destination IP is:")
    client_ip=coal.flow.clientIP.text
    print (client_ip)
    print ("Client Dest Port is:")
    client_dest_port=coal.flow.clientPort
    print (client_dest_port)
    print ("Server IP is:")
    server_ip=coal.flow.serverIP.text
    print (server_ip)
    print ("Server Dest port is:")
    server_dest_port=coal.flow.serverPort
    print(server_dest_port)
    print ("checksum is:")
    checksum=coal.decoding.checksum1k10k
    print (checksum)
    print("method is:")
    meth=req.method
    print(meth)
    print("http version is:")
    hVer=req.httpVersion
    print(hVer)
    print("http path is:")
    http_path=req.path
    print (req.path)
    print("parsed url:")
    print (req.parsedUrl)
    print("Response Code is:")
    respcode=resp.statusCode
    print(respcode)
    trans_time=datetime.fromtimestamp(int(coal.unixTime)).strftime('%Y-%m-%d %H:%M:%S')
    print("trans_time is:")
    print (trans_time)
     
    #Handle Flow table:
    now=datetime.now()
    d = now.strftime("%Y-%m-%d %H:%M:%S")
    print('INSERT INTO Flow (System_date) VALUES ("'+str(d)+'")')
    cursor.execute('INSERT INTO Flow (System_date) VALUES ("'+str(d)+'")')
    
    #Handle transactions table:
    cursor.execute("SELECT max(ID) FROM Flow")
    f=cursor.fetchone()
    f1=f[0]
    add_transactions=("INSERT INTO Transactions "
           "(Transaction_time, cgid, cid, site_signature_name, duration, Client_IP, Client_Dest_Port, Server_IP, Server_Dest_Port, checksum, Flow_ID) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    sitename='Static-YOUTUBE'
    data_transactions=(trans_time, cgid, cid, sitename, duration, client_ip, client_dest_port, server_ip, server_dest_port, checksum, f1)
    cursor.execute(add_transactions, data_transactions)
  
    #Handle requests table:
    cursor.execute("SELECT max(ID) FROM Transactions")
    t=cursor.fetchone()
    t1=t[0]
    add_requests=("INSERT INTO Requests "
           "(Transactions_ID, method, http_version) "
           "VALUES (%s, %s, %s)")
    data_requests=(t1, meth, hVer)
    cursor.execute(add_requests, data_requests)
  
    #Handle requests-params table:
    add_req_params=("INSERT INTO `Requests-Params` "
           "(Request_ID, Value, Name_request_param) "
           "VALUES (%s, %s, %s)")
    cursor.execute("SELECT max(Req_ID) FROM Requests")
    r=cursor.fetchone()
    r1=r[0]
    for (name,value) in req.params.iteritems ():
        data_req_params=(r1, value, name)
        cursor.execute(add_req_params, data_req_params)
  
    #Handle requests-PathSeg table:
    add_req_pathseg=("INSERT INTO `Requests-PathSeg` "
           "(Request_ID, Value, Relative_path_location) "
           "VALUES (%s, %s, %s)")
    segments=http_path.split("?")
    pathsegments1=segments[0]
    pathsegments2=pathsegments1.split("/")
    for i in range (1,len(pathsegments2)):
        data_req_pathseg=(r1, pathsegments2[i], i)
        cursor.execute(add_req_pathseg, data_req_pathseg)

    #Handle requests-Headers table:
    add_req_headers=("INSERT INTO `Requests-Headers` "
           "(Request_ID, Header_Name, Value) "
           "VALUES (%s, %s, %s)")
    for (name,value) in req.headers.dict.iteritems ():
        data_req_headers=(r1, name, value)
        cursor.execute(add_req_headers, data_req_headers)

    #Handle responses table:
    add_requests=("INSERT INTO Responses "
           "(Transactions_ID, Response_Code) "
           "VALUES (%s, %s)")
    data_requests=(t1, respcode)
    cursor.execute(add_requests, data_requests)

    #Handle responses-Headers table:
    add_resp_headers=("INSERT INTO `Responses-Headers` "
           "(Response_ID, Name_response_header, Value) "
           "VALUES (%s, %s, %s)")
    cursor.execute("SELECT max(ID) FROM Responses")
    res=cursor.fetchone()
    res1=res[0]
    for (name,value) in resp.headers.dict.iteritems ():
        data_resp_headers=(res1, name, value)
        cursor.execute(add_resp_headers, data_resp_headers)

    #commit
    cnx.commit()
    cursor.close()
    cnx.close()
    #raw_input() //LOAD PER LINE