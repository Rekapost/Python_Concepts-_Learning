# how to create constructor
"""class myclass:
    def m1(self):
        print("good morning")
    def __init__(self):   #constructor is used to initialize some values, it does not carry any arguments
         print("this is contructor")   # constructor values
obj=myclass()# when u create object  for the method/function , constructor is invoked automatically
obj.m1()
#this is contructor
#good morning"""

class myclass:
    def __init__(self, value1,value2):
        print("local variable=",value1)
        print("local variable=",value2)
        self.value1=value1   # making local variable  to a class variable
        self.value2=value2  # so putting self, it makes local to class, so that other method can
                            # make use of class variable
    def m2(self):    # to make local varaible to class variable , u need to define local variable to class
                     # by making use of self keyword
        print("class varaible=",self.value1)  #using local as class varaible which was changed
        print("class variable=",self.value2)
obj=myclass(100,200)
obj.m2()

"""#calling current one method from another method within class
class myclass:
    def m1(self):
        print("hi this is reka")
        self.m2(100)      #calling m2 from m1(in m1),
    def m2(self,a):
        print("hi print this number", a)
obj=myclass()
obj.m1()  #dont need to call m2 as m1 has already called m2"""

#constructor with arguments and same varaible name  in class and constructor
class myclass:
    name="Narayanasamy"
    def __init__(self,name):
        print("this is my first name", name)  #constructor argument local argument Reka
        print("this is my last name", self.name)  #represents class variable Narayanasamy
obj=myclass("Reka")





