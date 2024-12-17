"""
errors are of 3 types:
1.compile : like syntax errors
2.logical: in logical code gives output but the output is wrong

3.run time: it is done by incorect input like divide by 0 


"""

a=11
b=0
try:  #it might cause the exception
    print("the progrram is opened")
    print(a/b)
    k=int(input("enter the value of k"))
    print(k)

except ZeroDivisionError as e:
    print('')


except Exception as e: ## this block can be executed only we get the error
    print("u cant divide",e) 

##finally block: finally block is executed if we get an error as well as if we donot get the error
finally:
    print("the program is closed")
           