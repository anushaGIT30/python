#to represent the super class we use super method

class P:
    def __init__(self):
        print("p1 init")
    def p1(self):
        print("p1")
    def p2(self):
        print("p2")

class Q(P):
    def __init__(self):
        super().__init__()
    def q1(self):
        print("q1")
    def q2(self):
        print("q2") 



a=P()
a.p1()
a.p2()

b=Q()
b.q1()
b.p2()
