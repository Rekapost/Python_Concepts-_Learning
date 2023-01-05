"""s="welcome to python"
print(s.isalnum())               #false
print("welcome". isalpha())       #true
print("2012".isdigit())           #true
print("first number" .isidentifier())   #false    it is not a number ie identifier
print(s.islower())                       # true
print("WELCOME".isupper())               #true
print(" ".isspace())                      #true"""

#searching function
"""s="welcome to python reka"
print(s.endswith("reka"))     #true
print(s.startswith("good"))   #false
print(s.find("come"))         # 3  in 3rd index come is present
print(s.find("become"))       # -1 be is not present so it returns -1
print(s.rfind("o"))           # 15 in which index last o is present
print(s.count("o"))            #  3 character o is present 3 times"""

#converting strings
s= "welcome to PYTHON, REKA"
s1= s.capitalize()
print(s1)     #Welcome to python, reka    first letter of the sentence is capital
s2= s.title()
print(s2)      #Welcome To Python, Reka   first letter of all the string is capital
s3= s.lower()
print(s3)       #welcome to python, reka    upper to lower case
s4= s.upper()
print(s4)       #WELCOME TO PYTHON, REKA     lower to upper case
s5= s.swapcase()
print(s5)       #WELCOME TO python, reka      upper  string to lower string , lower string to upper string
s6= s.replace("to","in")
print(s6)       #welcome in PYTHON, REKA "to" is replaced as "in"
print(s)        #welcome to PYTHON, REKA  printed as it is

#reka
s="123abc"
print(s.isnumeric()) #false
print(s.isalnum())   #TRUE
s1="123"
print(s1.isnumeric())   #true
