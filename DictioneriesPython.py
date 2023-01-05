#CREATE dictionery , with key and values
"""friends={"reka":"999-000-666",     #reka is key   999-000-666 is value
        "raja":"555-444-333"}      #raja is key  555-444-333 is value
print(friends)     #friends is dictionery variable
#{'reka': '999-000-666', 'raja': '555-444-333'}

#retrieve the element from dictionery
print(friends['reka'])
#999-000-666

#add new element or item to a dictionery
friends['vasu']= '888-999-000'
print(friends)
#{'reka': '999-000-666', 'raja': '555-444-333', 'vasu': '888-999-000'}

#modify existing item
friends['vasu']='777-888-999'
print(friends)
#{'reka': '999-000-666', 'raja': '555-444-333', 'vasu': '777-888-999'}

#delete element from dictionery
del friends['vasu']
print(friends)   #{'reka': '999-000-666', 'raja': '555-444-333'}"""

#looping items in dictionery
friends={'a':'100',
         'b':'200',
         'c':'300',
         'd':'400'}
for i in friends:
        print(i, ":" ,friends[i])
'''
a : 100
b : 200
c : 300
d : 400'''

#print friends available in dictionery
print(friends)
#{'a': '100', 'b': '200', 'c': '300', 'd': '400'}

#length of dictionery
print(len(friends))
#4

#equality test in dictionery
d1={'reka':1983, 'raja':1985}
d2={'raja':1985,'reka':1983}
print(d1==d2)    #true
print(d1!=d2)    #false