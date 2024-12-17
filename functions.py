def add(a,b):
    return a+b
print(add(33,4))

"""
In this lecture, we are discussing types of arguments in python :
-- formal argument
-- actual argument 

   Actual arguments have 4 types:
1)position 
2)keyword
3)default
4)variable length argument  

Position argument:
-- During a function call, values passed through arguments should be in the order of parameters in the function definition. This is called positional arguments.
e.g
def person(name,age):
    print(name)
    print(age)
add(5,6)

keyword argument:
-- During a function call, values passed through arguments don’t need to be in the order of parameters in the function definition. Keyword arguments can achieve this. 
-- All the keyword arguments should match the parameters in the function definition.
e.g 
person(age=28,name='navin') 

default argument: 
-- Default arguments are values that are provided while defining functions.
-- The assignment operator = is used to assign a default value to the argument.
-- Default arguments become optional during the function calls.
-- If we provide a value to the default arguments during function calls, it overrides the default value.
-- The function can have any number of default arguments.
-- Default arguments should follow non-default arguments.

e.g
def person(name,age=28):
    print(name)
    print(age)
person('navin')

variable length argument:
-- if you want to pass multiple value in a function call we can use variable length argument
def sum(a,*b):
    print(a)
    print(b)
    c=a
    for i in b:
       c=c+i
    print(c)

sum(5,6,34,78)


"""
#if we want to add any arguments we use *
#like if we dont know how many arguments is to be used
def sumOf(a, *b):
    l = a
    for i in b:  # Iterate over the tuple `b`
        l += i  # Add each element of `b` to `l`
    print(l)

sumOf(5, 6, 7, 8, 99)

def person(name,**data):
    print (name)
    for i,j in data.items():
        print(i,j)
person("anu",age=21,address="banglore",mob=23456)        

   
       
