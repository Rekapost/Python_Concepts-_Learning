
name1=str("Reka")
name2=str("Reka")
print(id(name1))    # 3161997597488    #1355025242928
print(id(name2))    # 3161997597488    #1355025242928

name2= name2+"Narayanassamy"
print(id(name2))                       #1355030120608   memory location has changed once changed
print(id(name1))                       #1355025242928