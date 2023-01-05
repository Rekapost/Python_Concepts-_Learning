"""class name : Employee  Emp
constructor: accepts eid,ename,sal
display method : prints eid, ename and sal"""
"""
class Emp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
    def display(self):
        print("employee id={} employee name={} employee salary={}" .format(self.eid,self.ename,self.esal))
      # or  print("employee id= %d name=%s employee salary=%g" %(self.eid,self.ename,self.esal))
obj=Emp(1025,"Narayanasamy",21000)
obj.display()"""

#__STR
"""
class myclass:
    pass
obj=myclass()
print(obj)   #<__main__.myclass object at 0x0000011D3713A140>
"""
"""
class myclass:
    def __str__(self):
        return "welcome"
obj=myclass()
print(obj)
"""


"""
# whenever i want to print the reference variable , immediately i want to get the values of the varaible
class Emp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
    def __str__(self):
        return("employee id={}, employee name={}, employee salary={}".format(self.eid, self.ename, self.esal))
        # or  print("employee id= %d name=%s employee salary=%g" %(self.eid,self.ename,self.esal))
obj=Emp(1025, "Narayanasamy", 21000)
print(obj)    #employee id=1025 employee name=Narayanasamy employee salary=21000
"""

class myclass:
    def __del__(self):
        print("destroyed")
c1=myclass()
c2=myclass()
del c1