'''
Created on Jul 27, 2013

@author: asaf
'''
class ReqParam:
    
    def __init__(self, Param_ID, Request_ID, Name_request_param, Value):
        self.Param_ID=Param_ID
        self.Request_ID=Request_ID
        self.Name_request_param=Name_request_param
        self.Value=Value
        
    def printReqParam(self, ReqHeader):
        print("Param ID is:")
        print(ReqParam.Param_ID)
        print("Request ID:")
        print(ReqHeader.Request_ID)
        print("Name of param is:")
        print(ReqParam.Name_request_param)
        print("Value is:")
        print(ReqParam.Value)