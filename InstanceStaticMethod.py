"""#u can create instance and static method inside class
class myclass:
    def m1(self):
        print("instance method")

#if u want to make this method as static method ,u should use @staticmethod
    @staticmethod
    def m2():      #1.by default static method does not take any self parameter 
    #def m2(self):  #2. if u r giving self , then static method takes self as argument
        print("static method")   #1
        print(self)              #2  self will be treated as argument for the method m2(self)
m3=myclass()
m3.m1()
myclass.m2()   #1.calling a static method by class name , dont need object
#myclass.m2(10)  #2.self is argument , so u need send parameter value"""


#how to declare variable inside the class
class myclass:
    a,b=100,200      #class variables
    def add(self):
        print(self.a+self.b)    #prints 300  , u can access class variable by self keyword
    def mul(self):
        print(self.a*self.b)    #print 20000
obj=myclass()
obj.add()
obj.mul()

