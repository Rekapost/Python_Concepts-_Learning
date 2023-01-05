#How to open a file and write in a file
#create a file.txt
# note Location of the file
"""
file = open("C:\\Users\\Reka\\Desktop\\New\\PythonHandling.txt", 'w')  # open file for writing
file.write("this is my first line in python handling \n ")
file.write("this is my second line in python handling \n")   #if u want to write each sentence in new line add \n
file.write("this is my third line in python handling \n")
file.write("this is my fourth line in python handling \n")
"""
#How to read from a file
#READING ALL DATA AT ONCE

#file = open("C:\\Users\\Reka\\Desktop\\New\\PythonHandling.txt", 'r')
#print(file.read())  #it reads all characters from .txt
#print(file.read(10)) #it just reads 10 characters including space from .txt
#print(file.readlines())    #it prints all lines in a array format
#print(file.readline())   #it reads only the first line
#file.close()

"""file = open("C:\\Users\\Reka\\Desktop\\New\\PythonHandling.txt", 'a')
file.write("this is the end of the line")
file.close()
#it adds/appends extra data\line to the existing file """

#read all the lines in a file  in Loop , it reads one line by line by loop

file = open("C:\\Users\\Reka\\Desktop\\New\\PythonHandling.txt", 'r')
for l in file:
    print(l)
file.close()
