class A():
    def __init__(self):
        print("this is A init")

    def feature1(self):
        print("1st feature")

    def feature2(self):
        print("2nd feature")    

class B():
    def __init__(self):
        
        print("this is B init")
    def feature3(self):
        print("3rd feature")

    def feature4(self):
        print("4th feature") 

class C(A,B):
    def __init__(self):
        super().__init__()
        print("3d init")
    def feature5(self):
        print("5th init")    

a1 =A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature3()
b1.feature4()

c1=C()


##here A feature is not inherited in the B feature 
# so we use super keyword