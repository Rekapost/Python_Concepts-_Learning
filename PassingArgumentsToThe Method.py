#passing arguments with default values (positional)
"""def func(i,j=100):    # passing arguments with values called positional arguments
    print(i,j)
func(i=50)        #50,100
func(50,250)  """    #50,250    default value 100 is overwritten as 250

#keyword arguments
"""def name_args(name,greeting):
    print(greeting+" "+name)
name_args("Reka","hi")   #hi Reka     POSITIONAL ARGUMENTS
#or
name_args(name="Reka",greeting="hi")   #hi Reka   KEYWORD ARGUMENTS
name_args(greeting="hi",name="reka") """   #hi reka keyword arguments  , position is not important


#combine positional and keyword arguments
def poskey(a,b,c):
    print(a,b,c)
poskey(10,20,30)     #10,20,30
#or
poskey(10,b=20,c=30) #10,20,30
#or
poskey(10,c=30,b=20) #10,20,30  order is not important in keyword arguments
#or
#poskey(10,b=20,30)    #incorect, first postional then keyword , no mixing
                      #SyntaxError: positional argument follows keyword argument

#returning multiple values from function , it returns multiple values as tuples
def bigger(a,b):
    if(a>b):
        return(a,b)
    else:
        return(b,a)
s=bigger(10,20)
print(s)    #(20, 10)
print(type(s))   #<class 'tuple'>