'''
Created on Apr 19, 2013

@author: asaf
'''
class Response:

        def __init__(self, ID, Transactions_ID, Response_Code):
            self.ID=ID
            self.Transactions_ID=Transactions_ID
            self.Response_Code=Response_Code
            self.headers=[]
        
        def printResponse(self, Response):
            print("Response ID is:")
            print(Response.ID)
            print("Its Transaction id is:")
            print(Response.Transactions_ID)
            print("The Response Code is:")
            print(Response.Response_Code)
            print("The Headers of the Response are:")
            print(Response.headers)