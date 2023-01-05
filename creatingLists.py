#creating lists
"""list1=list()
print(list1)      #[]     list() is empty
list2=list([21,31,41,51])
print(list2)      #[21, 31, 41, 51]
list3=list(["reka","raja","vasantha","narayanasamy"])
print(list3)       #['reka', 'raja', 'vasantha', 'narayanasamy']
list4=list("reka")
print(list4)       #['r', 'e', 'k', 'a']"""

#access elements from the lists
#index operator[]
"""x=[1,2,3,4,5]       #index 0-1,index 1-2,index 2-3,index 3-4
print(x[2])     #3
print(x[0])      #1"""

"""list1=[2,3,4,1,32]
print(2 in list1)    #true
print(5 in list1)    #false
print(32 not in list1)   #false
print(len(list1))    #5
print(max(list1))    #32
print(min(list1))    #1
print(sum(list1))    #42
#print(for loop(list1))  NEXT SESSION """

#list slicing
"""list1=[11,22,33,44,55,66]
print(list1[1:4])     #[22, 33, 44]             0 to n-1
print(list1[:2])       #[11, 22]
print(list1[3:])       #[44, 55, 66]  till n"""

#concatenation and repetition/replication/duplicate the list values
"""list1=[1,2,3,4,5]
list2=[6,7,8]
list3=print(list1 + list2)      #[1, 2, 3, 4, 5, 6, 7, 8]
list4=print(list2*3)             #[6, 7, 8, 6, 7, 8, 6, 7, 8]"""

#  in or not in operator
"""list5=[22,33,44,55]
print(55 in list5)        #true
print(55 not in list5)    #false"""

#for loop to traverse in list
'''list6=[1,2,3,4,5]
for i in list6:
    print(i)'''
'''
1
2
3
4
5'''

#if u want to print in same line
list6=[1,2,3,4,5]
for i in list6:
    print(i,end=" ")
#1 2 3 4 5

"""for i in list6:
    print(list6)
''' [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]'''"""

