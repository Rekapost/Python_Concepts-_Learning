"""def myfun():     how to define a function
    #statements
    pass
myfun()"""

#sum function
"""def sum(start,end):
    result=0
    for i in range(start,end+1):
        result= result+ i
        print(result)
sum(0,5)  #15"""

"""def sum(start,end):
    result=0
    for i in range(start,end+1):
        result= result+ i
        print(result)
sum(10,20)    #165"""

"""def sum(start,end):
    result=0
    for i in range(start,end+1):
        result= result+ i
    return result           #instead of printing result , return result 
s=sum(10,20)
print(s)     #165       # prints s here"""

#another type
"""def sum(start,end):
    if(start>end):
        print("start value should be less than end valuse to sum")
        return     #none
    result=0
    for i in range(start,end+1):
        result=result+i
    return result
#s= sum(5,0)     # start value should be less than end valuse to sum
#print(s)        #none
s=sum(1,5)
print(s)      #15"""

def test():
    i=100
    return       #none         with return step it returns none
print(test())    #none         it returns none even without return step







