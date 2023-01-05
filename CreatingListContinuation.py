list1=[1,2,3,4,35,4,4]
list1.append(19)  #[1, 2, 3, 4, 35, 4, 4, 19]
print(list1)

print(list1.count(4))  #3  it counts how many times 4 has appeared

list2=[66,7]
list1.extend(list2)
print(list1)      #[1, 2, 3, 4, 35, 4, 4, 19, 66, 7]

print(list1.index(4))   #3    it will not say the no in index 4, instead it prints the index no of 4 in list
print(list1.index(35))   #4

list1.insert(4,25)
print(list1)    #[1, 2, 3, 4, 25, 35, 4, 4, 19, 66, 7]

print(list1.pop(9))    #66   returns the value in index 9  then ,
print(list1)  # prints [1, 2, 3, 4, 25, 35, 4, 4, 19, 7] after pop

list1.remove(35)
print(list1)   #[1, 2, 3, 4, 25, 4, 4, 19, 7]

list1.reverse()
print(list1)   #[7, 19, 4, 4, 25, 4, 3, 2, 1]

list1.sort()
print(list1)  #[1, 2, 3, 4, 4, 4, 7, 19, 25]


