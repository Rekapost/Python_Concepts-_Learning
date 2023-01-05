"""global variable  and loacal variable
local variable can be accesed within the function , but not outside the function
global variable can be accesed within the function and outside the function"""
"""global_var=15
def fun():
    local_var=20
    print(global_var)     #15
    print(local_var)      #20
fun()
print(global_var)     #15
#print(local_var)    #NameError: name 'local_var' is not defined."""


## #same variable name xy for global and local
"""xy=100                   
def cool():
    xy=200
    print(xy)     #200
cool()
print(xy)    #100 """

t=100
def test():
   global t     #u can change global variable value inside a function  as method  , by defining
   t=200        # u cannot assign value t when defining global variable inside function( global t=100) so put t=200
   print(t)         # make global variable = local variable    it prints 200
test()
print(t)              #it print 200 as value of the global variable is changed inside the function




