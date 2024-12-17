class person:
    ##everytime we create an object it will take new space
    def __init__(self):
        self.name="anu"
        self.age=21
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False    
        
p1=person()
p1.age=22
p2=person()
p2.age=22
if p1.compare(p2):
    print("they are same")
else:
    print("not same")
                
