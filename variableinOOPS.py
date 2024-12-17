#in oops there are 2 types of variables  are present 
#1.instance variable :if we define a variable inside the init it is instance vaiable
#2.static or class variables : outside the init and inside the class static or class variables
class bikes:
    wheels=2 #it is a class variable
    #declaring variables
    def __init__(self):
        self.bikename="rs200" #it is a instance variable
        self.milage=500
b1=bikes()
b2=bikes()
b1.milage=1000
b1.wheels=3
print(b1.bikename,b1.wheels,b1.milage) 
print(b2.bikename,b2.wheels,b2.milage)       
