""" #lambda function is a function that does not have any name, it is anonymus function
x=lambda a: a+10   # x is function, a is argument
print(x(5))   #15
x=lambda a,b:a*b
print(x(5,6))   #30
y=lambda a,b,c:a*b+c
print(y(2,5,10))   #20
z=lambda a,b,c:a+b+c
print(z(2,2,2))   #6"""

def add(a):
    a=a+10
    return(a)
print(add(5))   # 15
