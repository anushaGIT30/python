#decorators can change the behaviour of the  existing function at compile time
def div(a,b):
    return a/b
#so here we can use if condition but without changing the behaviour of this function we can use decorators
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=smart_div(div)
print(div(2,4))

