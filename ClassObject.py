#class is blueprint of object
#class contains method and object ,if u want to access the method and varaible , u should create an object
#self keyword in method or function is default
#function and method are same in python
class MyClass:      # create class / declare a class, MyClass is class name
       def Myfunc(self): # create method, self is keyword saying  Myfunc belongs to this particular Myclass
           pass        #if u dont want any body\content
       def display(self,name): #creatine one more method, passing a parameter name
           print("name is:", name)        #printing the parameter
# to use the MyClass ,u should create object
mc=MyClass()     #creating object
mc.Myfunc()    #calling Myfunc
mc.display("Reka")              #it prints-  my name is Reka
# mc is reference varaiable , myclass is object, object is stored in variable
# , whenever u say myclass , it will create memory location ,
# that memory location will be identified/reffering by this mc, mc is object refernce variable