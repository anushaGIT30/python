l=[1,2,3,4,5]
it=iter(l)
print(it.__next__())
# it is also be used
print(next(it))

#creating an own class and object to iterator

class topten:
    def __init__(self):
        self.num=1 #iter and next meethods are used

   