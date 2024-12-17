"""
Abstract classes: python doesnot support abstract classes but it uses ABC methods(Abstract base class)
what is abstract class:
methods which has a declaration but not a definition 
->we cannot declare object of an abstract class like this 
 class computer:
    def process(self):
        pass
        



"""

from abc import ABC,abstractmethod
class computer:
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process(self):
        print("run")    

