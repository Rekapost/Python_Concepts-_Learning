#__str__   executes automatically when u print refernce varaible
#__del__ destroy an object
#__init__ invoke at time of object creation
"""
class myclass:
    pass
obj=myclass()   #obj is refernce variable
# whenever u try to print the reference varaible , __str__ will be invoked
print(obj)    #<__main__.myclass object at 0x000002AF100B9390>   this is memeory location

#if u want to overwrite the str function
class myclass:
    def __str__(self):
        return "welcome"   #str can only return not print
obj = myclass()
print(obj) #welcome #actually invoking str has to print string memory location,but we are overwriting the str to print welcome
           #within the class , it prints only string"""

# del to delete the object
class myclass:
    def __del__(self):
        print("deleted")
ob1=myclass()
ob2=myclass()
del ob1     #prints deleted
           # deleted