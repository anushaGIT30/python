##inner class that means class within the class
class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll 
        #that means inside the outer class
        self.lap=self.laptop() 
    def show(self):
        print(self.name,'',self.roll)
    class laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=64
            #in order to create an object for this class laptop we use outside of this class  


        
s=student("ak",11)
s.show()  
lap1=s.laptop  