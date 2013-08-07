'''
Created on Jul 27, 2013

@author: asaf
'''
class ReqHeader:
    
    def __init__(self, Header_ID, Request_ID, Header_Name, Value):
        self.Header_ID=Header_ID
        self.Request_ID=Request_ID
        self.Header_Name=Header_Name
        self.Value=Value
        
    def printReqHeader(self, ReqHeader):
        print("Header ID is:")
        print(ReqHeader.Header_ID)
        print("Request ID:")
        print(ReqHeader.Request_ID)
        print("Header Name is:")
        print(ReqHeader.Header_Name)
        print("Value is:")
        print(ReqHeader.Value)