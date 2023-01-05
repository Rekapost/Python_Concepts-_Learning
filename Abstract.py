# abstarct class can be used when u know the requirement/ what to implement , but dont know how to implement it
#know the requirement ,but dont know the design , abstarct class is created at this situation
#ABC is prdefined abstarct class in python
"""
from abc import ABC,abstractmethod    # from abc module /package , import ABC ,abstract Class and method
class A(ABC):    # making class A as abstarct class   ,
    @abstractmethod   # making absatrct method
    def display(self):    # u cannot implement in this abstract method
        None   # nothing to implement
class B(A):        # B class becomes child for parent A
    def display(self):    # u can implement in this method
        print("this is Display method")   # have message to immplement
obj=B()   # we cannot create object for abstarct class A
obj.display()   # it calls class B , it cannot call abstract method A
# it prints      this is Display method  """

# one more example
"""
from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def eat(self):
        pass
class tiger(animal):
    def eat(self):
        print("eats non veg")
class cow(animal):
    def eat(self):
        print("eats veg")
tobj=tiger()
tobj.eat()   #eats non veg
cobj=cow()
cobj.eat()   # eats veg """

# second example:
# u have to use all the methods in abstract class in python,
"""
from abc import ABC, abstractmethod
class x(ABC):
    @abstractmethod    # this abstract class has 2 methods, u can implement these methods in multiple classes
    def m1(self):
        pass
    def m2(self):
        pass
class y(x):
    def m1(self):   # using one method m1 from abstarct class x, u have to use m2 also ,
                    # if not using m2 , u cant create object
        print("this is from method m1")
class z(y):
    def m2(self):   # using second method m2 from abstract class x
        print("this is from method m2")
obj=z()
obj.m1()   #this is from method m1
obj.m2()   #this is from method m1"""

# third example implement constructor within abstarct class
#abstract is used for security, to secure our methods
from abc import ABC, abstractmethod
class cal(ABC):
    def __init__(self, value):   # constructor is used to initialize some value
        self.value=value
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
class c(cal):
    def add(self):
        print(self.value+100)
    def sub(self):
        print(self.value-10)
obj=c(100)
obj.add()   # 200
obj.sub()   # 90

