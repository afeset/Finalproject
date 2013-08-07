'''
Created on Jul 27, 2013

@author: asaf
'''

class Flow:
    
    def __init__(self, ID, System_date):
        self.ID=ID
        self.System_date=System_date
    
    def printFlow(self, Flow):
        print("Flow ID is:")
        print(Flow.ID)
        print("Flow System Date is:")
        print(Flow.System_date)
    