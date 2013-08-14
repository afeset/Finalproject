
from DAL import RequestHandler
from Tests import TestResult
from HttpObjects import Request

class RequestHandlerTests:
    # all expected constants
    handler=RequestHandler() # note - this is a static variable
    
    def RunTests(self):
        result=[]
        
        #insert test
        request=Request(123, 1, 456, "bla") 
        RequestHandlerTests.handler.insertRequest(request)
        if(RequestHandlerTests.handler. gettRequest(request.id)!=123):    
            result.append(TestResult(False, "RequestHandlerTests : insert request : no connection to DB"))
        else:
            result.append(TestResult(True, "RequestHandlerTests : insert request : pass"))
    
    
        #getTransRequests test
        request=Request(123, 1, 456, "bla") 
        RequestHandlerTests.handler.getTransRequests(123)
        if(RequestHandlerTests.handler. gettRequest(request.id)!=123):    
            result.append(TestResult(False, "RequestHandlerTests : getTransRequests  : no connection to DB"))
        else:
            result.append(TestResult(True, "RequestHandlerTests : getTransRequests : pass"))

        return result
    
    
    
    