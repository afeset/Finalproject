'''
Created on May 1, 2013

@author: asaf
'''
class Transaction:

        def __init__(self, ID, Transaction_time, cgid, cid, site_signature_name, duration, Client_IP, 
                     Client_Dest_Port, Server_IP, Server_Dest_Port, checksum, Flow_ID, NumDownloadedBytes):
            self.ID=ID
            self.Transaction_time=Transaction_time
            self.cgid=cgid
            self.cid=cid
            self.site_signature_name=site_signature_name
            self.duration=duration
            self.Client_IP=Client_IP
            self.Client_Dest_Port=Client_Dest_Port
            self.Server_IP=Server_IP
            self.Server_Dest_Port=Server_Dest_Port
            self.checksum=checksum
            self.Flow_ID=Flow_ID
            self.NumDownloadedBytes=NumDownloadedBytes
            self.requests=[]
            self.responses=[]
        
        def printTransaction(self, Transaction):
            print("Transaction ID is:")
            print(Transaction.ID)
            print("Transaction time is:")
            print(Transaction.Transaction_time)
            print("Cgid is:")
            print(Transaction.cgid)
            print("Cid is:")
            print(Transaction.cid)
            print("Site signature name is:")
            print(Transaction.site_signature_name)
            print("Duration is:")
            print(self.duration)
            print("Client IP is:")
            print(self.Client_IP)
            print("Client Dest Port is:")
            print(Transaction.Client_Dest_Port)
            print("Server IP is:")
            print(Transaction.Server_IP)
            print("Server Dest Port is:")
            print(Transaction.Server_Dest_Port)
            print("Checksum IP is:")
            print(Transaction.checksum)
            print("Flow ID is:")
            print(Transaction.Flow_ID)
            print("Number of Downloaded Bytes is:")
            print(Transaction.NumDownloadedBytes)
           
            
