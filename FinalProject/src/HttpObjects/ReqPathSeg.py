'''
Created on Jul 27, 2013

@author: asaf
'''
class ReqPathSeg:
    
    def __init__(self, PathSeg_ID, Request_ID, Value, Relative_path_location):
        self.PathSeg_ID=PathSeg_ID
        self.Request_ID=Request_ID
        self.Value=Value
        self.Relative_path_location=Relative_path_location
        
    def printReqPathSeg(self, ReqPathSeg):
        print("Path Segment ID is:")
        print(ReqPathSeg.PathSeg_ID)
        print("Request ID:")
        print(ReqPathSeg.Request_ID)
        print("Value is:")
        print(ReqPathSeg.Value)
        print("Relative Path Location is:")
        print(ReqPathSeg.Relative_path_location)