class A:
    def show(self):
        print("this is a A")
class B(A):
    def show(self):
        print("this is a B")

a1=B()
a1.show()