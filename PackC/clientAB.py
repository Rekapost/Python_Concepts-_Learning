# importing module from 2 different packages  PackA and PackB
import sys;
sys.path.append("C:/Users/Reka/PycharmProjects/pythonProject1/PackA")
from module1 import *

sys.path.append("C:/Users/Reka/PycharmProjects/pythonProject1/PackA/PackB")
from module2 import *

display()    #this is from PackA module1
show()       #this is from PackB module2

