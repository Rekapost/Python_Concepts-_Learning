t1=()
print(t1)           #()
t2=(11,21,31)
print(t2)           #(11, 21, 31)
t3=([22,32,42,52])
print(t3)           #[22, 32, 42, 52]
t4=tuple("abc")
print(t4)           #('a', 'b', 'c')

#tuples functions
t1=(1,20,88,40,15)
print(len(t1))    #5
print(max(t1))    #88
print(min(t1))    #1
print(sum(t1))    #164

#iterating through tuples
for i in t1 :
    print(i, end =" ")     #1 20  88 40 15

#slicing tuples
t1=(1,20,88,40,15)
print(t1[0:3])  # (1, 20, 88)
print(t1[3:])    #(40, 15)
print(t1[1:3])   #(20, 88)

#in and not in operator in tuples
t1=(1,20,88,40,15)
print(20 in t1)          #true
print(30 in t1)          #false
print(20 not in t1)      #false
print(30 not in t1)   #true

#concatenate in tuples   reka model
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)

