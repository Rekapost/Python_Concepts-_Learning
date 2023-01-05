# encapsulation can be achieved by private variabls and private methods
# private variables can only be accessed only within  the method
"""
class myclass:
    __a=10      # private variable
    def display(self):
        print(self.__a)
obj=myclass()
obj.display()     # 10"""

#print(myclass.__a)  #AttributeError: type object 'myclass' has no attribute '__a',
# cannot accesee private variable outside the class

#PRIVATE METHODS CAN BE ACCESSED ONLY WITHIN THE METHOD
"""
class myclass:
    def __display1(self):    # this is private method, u cannot accesse outside the class
        print("this is private display 1 method")
    def display2(self):   # u need one more method to access the private method , this is public method
        print("this is public display 2 method")
        self.__display1()  # calling private method
obj=myclass()
#obj.__display1() #AttributeError: 'myclass' object has no attribute '__display1'. Did you mean: 'display2'?
#u cannot call private method outside the class
obj.display2()   #this is public display 2 method
                  #this id private display 1 method"""

# WE can access private variable outside of the class indirectly using some methods
class myclass:
    __empid=101  #private variable
    def getempid(self,eid):
        self.__empid=eid   # assigning private variable to local variable
    def dispempid(self):
        print(self.__empid)   # print private variable  , inside the same class, this method can access private variable
obj=myclass()
#obj.getempid(105)   #assigns 105 to private variable
#obj.dispempid()   #prints new private variable 105
#or
obj.dispempid()  # it prints 101, we have acceesd private variable outside of the class indirectly by dispempid method
