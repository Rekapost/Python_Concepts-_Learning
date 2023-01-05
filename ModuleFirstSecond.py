# have created two modules(ModuleFirst and ModuleSecond) , with same functions fly() and color()
# but body is different animal cant fly , animal is black , bird can fly , bird is green
# APPROACH 1
import ModuleFirst
import ModuleFirstSecond

ModuleFirst.fly()    #animal cant fly
ModuleFirst.color()  #animal is black

ModuleFirstSecond.fly()   #bird can fly
ModuleFirstSecond.color()  #bird is green

#APPROACH 2
from ModuleFirst import fly,color
fly()   #animal cant fly
color()  #animal is black

from ModuleFSecond import fly,color
fly()     #bird can fly
color()   #bird is green

# APPROACH 3
from ModuleFirst import *
fly()    #animal cant fly
color()   #animal is black

from ModuleFirstSecond import *
fly()    #bird can fly
color()   #bird is green
""" in this method modulesecond is called latest , so it executes the functions from second
whichever module is put latest , latest functions will be taken """
from ModuleFirst import *
from ModuleFirstSecond import *
fly()       #bird can fly
color()     #bird is green

from ModuleFSecond import *
from ModuleFirst import *
fly()     #animal cant fly
color()   #animal is black
