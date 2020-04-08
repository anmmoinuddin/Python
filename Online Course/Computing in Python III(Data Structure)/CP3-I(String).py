##data Structure
## Interger by value
#----------------------------------------------------------------------
#integer
def addone(aninteger):
    aninteger=aninteger+1
    print("aninterger:", aninteger)

myinteger=5
print("myinteger before addone:", myinteger)
addone(myinteger)
print("myinteger after addone:", myinteger)
#----------------------------------------------------------------------
#string
def addexc(astring):
    astring=astring + " !"
    print("astring:", astring)

mystring="Hello, World"   
print("mylist before additem:", mystring)
addexc(mystring)
print("mystring after addexc", mystring)
#----------------------------------------------------------------------
#List and append option(to add sth new)
def additem(alist):
    alist.append("New item!")
    print("alist:", alist)
mylist=["One","Two", "Three"]
print("mylist before additem:", mylist)
additem(mylist)
print("myList after additem:", mylist)
#-----------------------------------------------------------------------------
#Variable assignment
#with list everything being updated at the same time
mylist1=["One", "Two", "Three"]
mylist2=mylist1
mylist1.append("Four")

print("mylist1:", mylist1)
print("mylist2:", mylist2)
#---------------------------------------------------------------------------
#with integer it keeps the old value in comparison with list
myint1=5
myint2=myint1
myint1=7

print("myint1:", myint1)
print("myint2:", myint2)

#--------------------------------------------------------------
#Mutable variable
myinteger=1
myinteger=2
print(myinteger)
#---------------------------------------------------------------
##Function vs. Methods
# function is normally defined at the beginnin of program

mynumericstring="123455"
mynonnumericstring="ABCDE"

print(mynumericstring.isdigit())
print(mynonnumericstring.isdigit())

#-------------------------------------------------------------------


##Strings
##3way to declare strings
#---------------------------------------------------------------------------------
mystring1='"12345"'
mystring2="'12345'"
mystring3='''"'12345'"'''
mystring4="'''12345'''"


print(mystring1)
print(mystring2)
print(mystring3)
print(mystring4)
#-------------------------------------------------------------------------------
mystring="12345 \n 45"
print(mystring)

#------------------------------------------------------
mystring="12345\n8910\tabcde\"fghiklm\\no"
print(mystring)

#----------------------------------------------------


