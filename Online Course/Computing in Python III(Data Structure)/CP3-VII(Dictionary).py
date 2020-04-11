#simple Dictionary
mydictionary=   {"Sprockets": 5,
                 "widgets": 11,
                 "cogs":3,
                 "gizmos":15
                }
print(mydictionary)
mydictionary["Sprockets"]+=1
print(mydictionary)
#------------------------------------------------------------
#adding and removing from dictionary

mydictionary=   {"Sprockets": 5,
                 "widgets": 11,
                 "cogs":3,
                 "gizmos":15
                 }
print(mydictionary)
#adding sth
mydictionary["gadgets"]=1
print(mydictionary)
#Removing sth
del mydictionary["gadgets"]
print(mydictionary)

#------------------------------------------------------------
mydictionary=   {"Sprockets": 5,
                 "widgets": 11,
                 "cogs":3,
                 "gizmos":15
                 }

print(mydictionary)

if "David" in mydictionary:
    print("David is already in mydictionary")
    mydictionary["David"]="4015126656"
else:
    mydictionary["David"]="40451225"
print(mydictionary)
#-------------------------------------------------------------------
mydictionary=   {"Sprockets": 5,
                 "widgets": 11,
                 "cogs":3,
                 "gizmos":15
                 }
for(key,value) in mydictionary.items():
    if value<5:
        print(key, "is less than :", value)
