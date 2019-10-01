# Program 5 Telecom Company
class CallDetail:
    def __init__(self, caller, called, duration,calltype):
        self.caller = caller
        self.called = called
        self.duration = duration
        self.calltype = calltype

    def __str__(self):
        return self.caller.ljust(15)+self.called.ljust(15)+self.duration.ljust(15)+self.calltype.ljust(15)

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        self.list_of_call_string = list_of_call_string
        for x in list_of_call_string:
            call = x.split(",")
            callobj = CallDetail(call[0],call[1],call[2],call[3])
            print(callobj)

call1 = "9880424607,9916650273,20,STD"
call2 = "9916650273,9876975126,30,ISD"
call3 = "9880424607,7908273162,100,Local"
list_of_call_string = [call1,call2,call3]
print("Caller".ljust(14),"Called".ljust(14),"Duration".ljust(14),"Type".ljust(14))
Util().parse_customer(list_of_call_string)
    
