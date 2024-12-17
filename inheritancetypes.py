# 1. Single Inheritance
class A:
    def feature1(self):
        print("Feature 1 is called")

class B(A):  # B inherits from A
    def feature2(self):
        print("Feature 2 is called")

print("Single Inheritance:")
b1 = B()
b1.feature1()
b1.feature2()
print("-" * 30)


# 2. Multi-level Inheritance
class C(B):  # C inherits from B, B inherits from A
    def feature3(self):
        print("Feature 3 is called")

print("Multi-level Inheritance:")
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
print("-" * 30)


# 3. Multiple Inheritance
class X:
    def featureX(self):
        print("Feature X is called")

class Y:
    def featureY(self):
        print("Feature Y is called")

class Z(X, Y):  # Z inherits from X and Y
    def featureZ(self):
        print("Feature Z is called")

print("Multiple Inheritance:")
z1 = Z()
z1.featureX()
z1.featureY()
z1.featureZ()
print("-" * 30)


# 4. Hierarchical Inheritance
class P:
    def featureP(self):
        print("Feature P is called")

class Q(P):  # Q inherits from P
    def featureQ(self):
        print("Feature Q is called")

class R(P):  # R inherits from P
    def featureR(self):
        print("Feature R is called")

print("Hierarchical Inheritance:")
q1 = Q()
q1.featureP()
q1.featureQ()

r1 = R()
r1.featureP()
r1.featureR()
print("-" * 30)


# 5. Hybrid Inheritance
class M:
    def featureM(self):
        print("Feature M is called")

class N(M):  # N inherits from M
    def featureN(self):
        print("Feature N is called")

class O(M):  # O inherits from M
    def featureO(self):
        print("Feature O is called")

class P(N, O):  # P inherits from both N and O
    def featureP(self):
        print("Feature P is called")

print("Hybrid Inheritance:")
p1 = P()
p1.featureM()  # Inherited from M
p1.featureN()  # Inherited from N
p1.featureO()  # Inherited from O
p1.featureP()
print("-" * 30)
