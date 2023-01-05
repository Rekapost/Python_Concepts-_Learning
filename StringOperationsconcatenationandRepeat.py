str="Reka"
print(str+"Narayanassamy")   #RekaNarayanassamy  concatenation
print(str*10)                #RekaRekaRekaRekaRekaRekaRekaRekaRekaReka prints repeatedly 10 times

#slicing strings[]
str="welcome"
print(str[1:3])          #index is 0, w-0,e-1,l-2,c-3,o-4,m-5,e-6      so el is printed
print(str[:6])            #start is not mentioned so welcom is printed
print(str[4:])            #no end value  ome is printed

#ord and chr functions
#ord gives ASCII no of the character
#chr gives character based on the ASCII no
print(ord('R'))             #82
print(chr(82))              #R
print(chr(ord('R')))        #R

#len length of the string, max characters having max ASCII value ,min charcater having min ASCII value\
#lower case letters in strings
name="reka"
print(len(name))       #4
print(len("reka"))     #4
print(max(name))       #r
print(max("reka"))     #r
print(min(name))       #a
print(min("reka"))     #a


#in and not in operator also called a membership operator
str="REKA NARAYANASAMY"
print ("REKA"in(str))    #True
print("xyz"in str)       #false
print("REKA"not in str)    #False
print("NARA" not in(str))  # False
print("xyz" not in str)     #true