a=10#global variable
def something():
    a=15#local variable
    x=globals()['a']
    print(a)
something()
print(a)    