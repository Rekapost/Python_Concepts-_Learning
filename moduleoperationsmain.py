
# from moduleoperations, u have to import those functions
#Approach 1
import moduleoperations
moduleoperations.add(10,20)   #30
moduleoperations.mul(10,20)   #200

#Approach 2
from moduleoperations import add,mul
add(10,20)     # 30
mul(30,10)     # 300

#approach 3 if u have n number of operations in module
from moduleoperations import *
add(10,20)   #30
mul(30,10)   #300
sub(20,10)   #10
div(4,2)    #2.0
