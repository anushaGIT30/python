class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def add(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a 
        return s           
s=student(44,12)
print(s.add(2,4))
