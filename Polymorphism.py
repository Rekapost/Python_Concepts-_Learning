#Method Overriding

'''# 1 how to override a varaible
class parent:
    name="reka"
class child(parent):
    name="narayanasamy"
    #pass
obj=child()
print(obj.name)  # it prints narayansamy as child has variable and child is given priority
                 #if child does not have varaible , it print parent variable name   reka'''

# 2 How to override a method
"""
class bank:
    def rateofinterest(self):
        return 0
class ICICI(bank):
    def rateofinterest(self):
        return 10.5
obj=ICICI()
print(obj.rateofinterest())  #10.5
# if u want to call parent class method
obj1=bank()
print(obj1.rateofinterest())   #0"""

# OVERLOADING methods
class Human:
    def sayHellow(self, name=None): #one method
        if name is not None:     #works in 2 different way , way 1
            print("my name is ",name)
        else:                                               # way 2
            print("hellow")
obj=Human()
obj.sayHellow("reka")   # First way    my name is  reka
obj.sayHellow()          #second way   hellow
"""
# another example for overloading methods
class bird:
    def fly(self,name=None):      # one method , behave diff for each input
        if name=="parrot":
            print(name,"it can fly")
        if name=="penguine":
            print(name,"it cannot fly")
        if name is None:
            print("no input")
obj=bird()
obj.fly()   # no input
obj.fly("parrot")    # parrot it can fly
obj.fly("penguine")   #penguine it cannot fly

"""


