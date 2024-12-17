#polymorphysim:
#1.duck typing
#2. operator overloading
#3.method overloading
#4.method overiding

#1.duck typing

class pycharm:
    def execute(self):
        print("compiling")
        print("running")
class myEditor:
    def execute(self):
        print("spell check")
        print("name check")
        print("compiling")
        print("running")
class laptop:
    def code(self,ide):
        ide.execute() 
ide=myEditor()
lap1=laptop()
lap1.code(ide)  


#2.operator overloading
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)  # Return a new Student object

    def __gt__(self, other):  # Corrected the method name
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        return r1 > r2  # Return a boolean value for comparison
    
    def __mul__(self,other):
        a1=self.m1*other.m1
        a2=self.m2*other.m2
        return Student(a1,a2)

    def __str__(self):
        return f"Marks1: {self.m1}, Marks2: {self.m2}"  # Display marks meaningfully


# Creating student objects
s1 = Student(10, 20)
s2 = Student(30, 40)

# Displaying student objects
print("Student 1:", s1)
print("Student 2:", s2)

# Adding two student objects
s3 = s1 + s2
print("After Addition (Student 3):", s3)

# Comparing two student objects
if s1 > s2:
    print("Student 1 has higher total marks")
else:
    print("Student 2 has higher total marks")

s4=s1*s2
print("total",s4)    
