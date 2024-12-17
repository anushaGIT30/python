#__init__ is a special method and it is a constructor
class computer:
    def __init__(self,cpuname,ram):
        self.cpuname=cpuname ##attributes or properties
        self.ram=ram
    def config(self):##behaviour
        print("config is", self.cpuname,self.ram)
computer1=computer("i5",16)
computer2=computer("i12",64)
computer1.config()
computer2.config()           