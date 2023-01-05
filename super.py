#super() to invoke parent class methods
#to invoke parents class varaibles
#to invoke parent class constructor
"""
class A:
    x,y=10,20
class B(A):
    a,b=10,100
    def m2(self,e,f):
        print(e+f)    #local variable   40
        print(self.a+self.b)     #child class variable  110
        print(self.x+self.y)     #parent class variable   30   to invoke parents class varaibles
obj=B()
obj.m2(10,30)"""


"""# if all the variables have same name
a,b=5,10          #global variable
class A:
    a,b=10,20       #parent class variable
class B(A):
    a,b=10,100      #child class variable
    def m2(self,a,b):    # method /local varaible
        print(a+b)    #local variable      #40
        print(self.a+self.b)     #child class variable   #110
        print(super().a+super().b)     #parent class variable   #30
        print(globals()['a']+globals()['b'])   #global variable   #15
obj=B()
obj.m2(10,30)"""

"""# to invoke parent class constructor
class A:
    def __init__(self):
        print("constructor from parent A")
class B(A):
    pass
obj=B()   #constructor from parent A 
          # it invokes parents class constructor and prints since child class does not have constructor"""

#IF both parent and child has constructor
#first priority goes to child class constructor
class A:
    def __init__(self):
        print("constructor from parent A")
class B(A):
    def __init__(self):
        print("constructor from B")
        super().__init__() # to invoke parent class constructor
        #or another approach
    #   A.__init__(self)
obj=B()  #constructor from B
        #constructor from parent A   # prints because of super().__init__() step




