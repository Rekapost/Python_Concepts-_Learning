# i want to find how may classes are created in the module
"""
import ModuleFind
print(dir(ModuleFind)) # this will return/show  how many classes are there in the  ModuleFind"""
#u cannot see how many methods are there in the module
#['A', 'B', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

#if u want to see how many methods are there in the module , then u should not define class, just define functions ,
#within the class it is called methods , outside the class it is called functions

import ModuleFindClasses
print(dir(ModuleFindClasses))
#['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'm1', 'm2']