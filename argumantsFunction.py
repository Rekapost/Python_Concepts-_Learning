#example 1
"""
def sum(*args):    # * is mutilple values , args is varaible name, functions that will accept any no of arguments
    s=0
    for i in args:
        s+=i
    print("sum is " ,s)
sum(1,2)  #sum is 3
sum(4,5,6)   #sum is 15
sum(10,20,30,40,50)  #sum is 150"""

# example 2 with list

def my_three(a,b,c,d):
    print(a,b,c,d)
args=[1,2,3,4]   #list
my_three(*args) # 1 2 3 4

#-----**kwargs---------
#example 1
"""
def my_three(a,b,c,d):
    print(a,b,c,d)
a={'a':"one",'b':"two",'c':"three",'d':"four"}
my_three(**a)    #one two three four"""

# how to receive multiple arguments
"""
def my_func(**kwargs):
    for i,j in kwargs.items():   # to read key and value  i ,j
        print(i,j)
my_func(name='reka',spot="learn",roll="1025")"""
'''name reka
spot learn
roll 1025'''
