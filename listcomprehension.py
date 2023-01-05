"""for i in range(10):
    print(i)

for x in range(10):
    print(x, end=" ")

list1= [x for x in range(10)]
print(list1)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  it prints 0 to 9

#if u want to print from 1 to 9
list1= [x+1 for x in range(10)]
print(list1)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"""

# print even no from 0 to 9
"""for i in range(10):
    if (i%2==0):
        print(i)
 #0,2,4,6,8"""

# print even no from 0 to 9 in list
list1=[i for i in range(10) if i%2==0 ]
print(list1)
#[0, 2, 4, 6, 8]


