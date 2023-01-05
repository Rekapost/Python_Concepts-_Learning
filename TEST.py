"""
class myclass:
    value1='xyz'
    value2='abc'
    def display(self):
        print(self.value1)
        print(self.value2)
obj=myclass()
obj.display()
"""
"""
a=10,20,30
print(a)
print(type(a))
"""
"""
print(oct(65))         #0o101
print(float(0o0101))   #65.0
print(9//4)    # 2
print(-9//4)   #-3
a=10
b=20
print(a**b)   #100000000000000000000
"""
"""
a=[10,20,30]
for i in a:
    print(i,":in loop")
else:
    print("not in loop")
"""
"""
import sys
#print(sys.version)
x="sekar"
y=x
print(sys.getrefcount(x))    #5
"""
"""
a=range(1,1000)
print(type(a))     #<class 'range'>
#x=Xrange(1,1000)
"""
a=[1,2,3,4,5,6,7,8]
print(a)
numbers=','.join(str(i) for i in a)
print(numbers)


