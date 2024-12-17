class A:
    def feature1(self):
        print("feature1 is called")
    def feature2(self):
        print("feature2 is called")


class B:
    def feature3(self):
        print("feature3 is called")
    def feature4(self):
        print("feature4 is called")    

class C(A):
    def feature5(self):
        print("feature 5is called")
    def feature6(self):
        print("feature 6 is called")  

class D(C,B): ##multiple inheritance 
    def feature7(self):
        print("feature 7 is called")
a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature3()
b1.feature4()

c1=C()
c1.feature2()
c1.feature5()

d1=D()
d1.feature6()
d1.feature4()