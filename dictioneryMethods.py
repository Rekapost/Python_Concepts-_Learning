friends={'reka': '999-000-666', 'raja': '555-444-333','vasu':'999-888-777'}
#popitem() returns randomly select item from dictionery and removes that select item from dictionery

print(friends.popitem())
#('vasu', '999-888-777')
print(friends)
#{'reka': '999-000-666', 'raja': '555-444-333'}

#del everything from dictionery
print(friends.clear())
#None  as nothing in dictionery all r cleared

#keys()   returns  keys in dictionery as tuples
friends={'reka': '999-000-666', 'raja': '555-444-333','vasu':'999-888-777'}
print(friends.keys())
#dict_keys(['reka', 'raja', 'vasu'])
#dict_keys is name of tuple,  all keys as tuples  keys in tuple format

#value()  returns values of the keys in dictionery in tuple format
print(friends.values())
#dict_values(['999-000-666', '555-444-333', '999-888-777'})

#get(key)
#returns the value of the specified key , if key is not found , it returns none instead of throwing keyerror exception
print(friends.get('reka'))
#999-000-666
print(friends.get('raka'))
#None

#pop(key) returns the value of the specified key and item and removes that item key from the dictionery,
# if that key is not present it throws keyerror
print(friends.pop('reka'))
#999-000-666
print(friends)
#{'raja': '555-444-333', 'vasu': '999-888-777'}






