name="Reka"
age= 40
sal=0.0

print(name,age,sal)
#Reka 40 0

print("name:%s,age:%d,sal:%f" %(name,age,sal))
#name:Reka,age:40,sal:0.000000    type

print("name:{},age:{},sal:{}" .format(name,age,sal))
#name:Reka,age:40,sal:0.0       value

print("name:{0},age:{1},sal:{2}" .format(name,age,sal))
#name:Reka,age:40,sal:0.0     index and value

print("name:{2},age:{2},sal:{2}" .format(name,age,sal))
print("name:{1},age:{1},sal:{1}" .format(name,age,sal))
print("name:{0},age:{0},sal:{0}" .format(name,age,sal))
'''name:0.0,age:0.0,sal:0.0
name:40,age:40,sal:40
name:Reka,age:Reka,sal:Reka'''

print("name:{2},age:{2},sal:{2}" .format(age,sal,name))
#name:Reka,age:Reka,sal:Reka

print("name is:",name)
print("age is:",age)
print("sal is :",sal)
'''name is: Reka
age is: 40
sal is : 0.0'''


