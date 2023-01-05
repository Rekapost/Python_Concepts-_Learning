
# u have 1 package(pack1)  with 2 modules(module1 and module2), u r going to access pack 1 from pack 2 client
# syntax to access pack1 from pack2
import sys;
sys.path.append("C:/Users/Reka/PycharmProjects/pythonProject1/Pack1");

# Approach 1
import module1
import module2

module1.display()  # this is display function from module1
module2.show()     #  this is show function from module 2

# Approach 2
#not specifying module name , but accessing its functions
from module1 import *
from module2 import *

display()   #this is display function from module1
show()      #this is show function from module 2

