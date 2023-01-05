"""j,k=50,60                #global varaible
class myclass:
    a,b=10,20              #class variable
    def add(self,c,d):      #c,d are local variable
     #   c,d=30,40
        print(c+d)     #70        local variable
        print(self.a+self.b)    #30    class varaible
        print(j+k)     #110 global varaible,since global name is diff from local, u can use the variables as it is
        obj=myclass()
obj.add(30,40)"""

#same varaiable name for class, global and local
"""a,b=10,20
class myclass:
    a,b=30,40
    def add(self,a,b):
        print("local varaiable=", a+b)    #110
        print("class varaible=" ,self.a+self.b)     #70
# to contact global variable as it has same variable name as local
# u have to use a format globals()['a'],globals()['b']
        print("global variable=" , globals()['a']+globals()['b'])    #30
obj=myclass()
obj.add(50,60)"""

#creating mutiple objects for one class
"""class myclass:
    def display(self):
        print("good morning Reka")
obj1=myclass()    #object 1  creating a memory location
obj1.display()       #prints good morning Reka
print(id(obj1))       #memory location of object 1   1338304626640
obj2=myclass()    #object 2   creates another memory location for object 2
obj2.display()     #prints good morning Reka
print(id(obj2))      #memory location of object 2  1338304626448
obj3=obj1
print(id(obj3))      #1338304626640
print(obj1 is obj2)    #false
print(obj1 is obj3)    #true
print(obj1 is not obj2)  #true
print(obj1 is not obj3)    #false

# memory location of two objects are diffrenet as it is two diff physical entity"""

#creating named object and nameless object
"""class myclass:
    def func(self):
        print("continue")
obj=myclass()    # named object, as myclass is given a refernce variable   prints continue
obj.func()
myclass().func()   # nameless object as it is not given any reference variable   prints continue"""

#converting local variable to class variable
class myclass:
    def m1(self, value1,value2):
        print("local variable=",value1)
        print("local variable=",value2)
        self.value1=value1   # making local variable of method m1 to a class variable
        self.value2=value2  # so putting self, it makes local to class, so that other method can
                            # make use of class variable
    def m2(self):    # to make local varaible to class variable , u need to define local variable to class
                     # by making use of self keyword
        print("class varaible=",self.value1)  #using local as class varaible which was changed
        print("class variable=",self.value2)
        print(self.value1+self.value2)
obj=myclass()
obj.m1(10,20)
obj.m2()
"""local variable= 10
local variable= 20
class varaible= 10
class variable= 20"""


