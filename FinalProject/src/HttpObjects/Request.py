'''
Created on Mar 27, 2013

@author: elirans
'''

class Request:
    
    def __init__(self, Req_ID, http_version, Transactions_ID, method):
        self.Req_ID=Req_ID
        self.http_version=http_version
        self.Transactions_ID=Transactions_ID
        self.method=method
        self.params=[]
        self.headers=[]
        self.pathsegs=[]
        
    def printRequest(self, Request):
        print("Request ID is:")
        print(Request.Req_ID)
        print("Http Version is:")
        print(Request.http_version)
        print("Transaction ID is:")
        print(Request.Transaction_ID)
        print("Method is:")
        print(Request.method)
