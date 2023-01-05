# u have 2 modules animal ModuleA and bird ModuleB
#APPROACH 1
import ModuleA
import ModuleB
# HOW to call classes and methods, so create  object
obj=ModuleA.animal()  # calling module by module name
obj.display()     #i like animals
obj1=ModuleB.bird()
obj1.display()   #i like parrot

#APPROACH 2
from ModuleA import animal
from ModuleB import bird
obj2=animal()
obj2.display()   #i like animals

obj3=bird()
obj3.display()    #i like parrot