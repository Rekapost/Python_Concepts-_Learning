#IMPORTING CLASSES FROM DIFFERENT MODULES AND PACKAGES

import sys;
sys.path.append("C:/Users/Reka/PycharmProjects/pythonProject1/PackX")
sys.path.append("C:/Users/Reka/PycharmProjects/pythonProject1/PackY")
from emp import *
from stu import *
obj1=employee(1025,"reka",0.0)
obj1.displayemp()    #employee id=1025 employee name=reka employee salary=0.0
obj2=student(10,"narayanasamy")
obj2.displaystu()   #student id=10 student name=narayanasamy