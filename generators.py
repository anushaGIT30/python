#generators are the updated version of iterator because in iterator we use 2 objects but here we use yeild
def funcion():
    yield 5
    yield 'ak'
 
val=funcion()
print(val.__next__())
print(val.__next__()) 


def square():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
value=square()
for i in value:
    print(i)
#generators are used to fetch one value at a time suppose if we have so many records if we fetch all values these
# all records are loaded in the memory if we want to work with a 1 value at atime 