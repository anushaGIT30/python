class student:
    school="sai ram high school" #class variable
    def __init__(self,m1,m2,m3):
        #instance variable 
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3

   ## def __str__(self):
     ##   return f"marks={self.marks1},{self.marks2},{self.marks3}"

    def avg(self):
        return((self.marks1+self.marks2+self.marks3)/3)

    def get_marks1(self):
        return self.marks1
    def set_marks1(self,value):
        self.marks1=value

    #if we want to acess class variable 
    @classmethod
    def info(cls):
        ##if we want to work with a class variable we use cls
        return cls.school
#static vaiable which doesnot comes under instance and class variable\
    @staticmethod
    def staticmeth():
        print("this is a static method")


s1=student(99,100,98)
print(f"{s1.avg()}")
print(f"{s1.get_marks1()}")
s1.set_marks1(9236)                       # Updates marks1 to 96
print(f"{s1.get_marks1()}")
print(s1.info()) ##it is used for only one object if we want to use for entire class we use decorators "@classmethod"
print(student.info())

print(student.staticmeth())
