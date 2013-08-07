'''
Created on Apr 19, 2013

@author: asaf
'''
class ResHeader:
    def __init__(self, Header_ID, Response_ID, Name_response_header, Value):
            self.Header_ID=Header_ID
            self.Response_ID=Response_ID
            self.Name_response_header=Name_response_header
            self.Value=Value
            
    def printResHeader(self, ResHeader):
            print("Response Header ID is:")
            print(ResHeader.ID)
            print("Its Response id is:")
            print(ResHeader.Response_ID)
            print("Name of response header is:")
            print(ResHeader.Name_response_header)
            print("Its value is")
            print(ResHeader.Value)