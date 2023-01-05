# example 1 exception 1: ZeroDivisionError: division by zero
"""
print(" program is started")    #program is started
print(10/0)                     #ZeroDivisionError: division by zero
print("program is completed")"""
"""

print("program is started")
try:
    print(10/0)   #if not correct goes to except block
except ZeroDivisionError:
    print("entered into except block-Handling exception")
print("program is completed")
#program is started
#entered into  except block-Handling exception
#program is completed"""
"""

print("program is started")
try:
    print(10/5)    #if correct goes to else  block
except TypeError:
    print("entered into except block-handling typeerror exception")
except ZeroDivisionError:
    print("entered into  except block-Handling zerodivisionerror exception")
else:
    print("entered else block")
finally:
    print("entered finally block")
print("program is completed")"""
#program is started
#2.0
#entered else block
#entered finally block
#program is completed

# example 2 value error
"""
def enterage(age):
    if age<0:
        raise ValueError
        print("enter positive integers only ")
    if age %2==0:
        print("age is even")
    else:
        print("age is odd")
try:
    num=0
    enterage(num)
except ValueError:
    print("only positive integers are allowed")
except:
    print("something is wrong")"""

"""if num = -5 , only positive integers are allowed
if num = 5, age is odd
if num is 0, age is even"""

#EXAMPLE 3  EXCEPTION OBJECTS
try:
    number= one
    print("the number is :", number)
except NameError as NE:    #object is NE
    print("exception is :",NE)
#exception is : name 'one' is not defined

