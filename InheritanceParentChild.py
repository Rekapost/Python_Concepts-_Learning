# SINGLE INHERITANCE means single parent and single child
"""
class A:      #parent
    def m1(self):
        print("I am from class A")
class B(A):   # calling class A  from class B    child
    def m2(self):    #  (child =it gets all the benifts of Parents)
        print("i am from class B")
Aobj= A()
Aobj.m1()  # calling m1 from class A    #I am from class A
Bobj= B()
Bobj.m1()   #calling m1 from class A    #I am from class A
Bobj.m2()   #calling m2 from class B    #I am from class B"""

## SINGLE INHERITANCE means single parent and single child
"""
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)
obj=B()
obj.m1()     # 30
obj.m2()     # 300"""

"""#Mutilevel Inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)
class C(B):
    c,d=5,10
    def m3(self):
        print(self.c+self.d)
obj=B()
obj.m1()     # 30   A
obj.m2()     #300   B
obj=C()
obj.m1()   #30   A
obj.m2()   #300  B
obj.m3()   #15   C  """

"""#HEIRARCHICAL INHERITANCE one parent and 2 child
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=30,40
    def m2(self):
        print(self.a+self.b)
class C(A):
    e,f=50,60
    def m3(self):
        print(self.e+self.f)
bobj=B()
bobj.m1()    #30   A
bobj.m2()    #70  B
cobj=C()
cobj.m1()    #30  A
cobj.m3()    #110  C  """

#MULTIPLE INHERITANCE  2 PARENT AND 1 CHILD
class A:              #FIRST PARENT
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B:              # SECOND PARENT
    a,b=30,40
    def m2(self):
        print(self.a+self.b)
class C(A,B):       #ONE CHILD HAS BENIFITS FROM 2 PARENTS
    e,f=50,60
    def m3(self):
        print(self.e+self.f)
bobj=C()
bobj.m1()    #30   A
bobj.m2()    #70  B
bobj.m3()    #110  C





