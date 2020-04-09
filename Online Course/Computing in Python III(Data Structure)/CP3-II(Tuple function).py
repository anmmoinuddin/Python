#find out the quotient and remainder
#string with quotation mark, list with third []brackets and tuple with first brackets
#----------------------------------------------------------------------------
def quotientandremainder(dividend, divisor):
    quotient=dividend//divisor
    remainder=dividend%divisor
    return (quotient, remainder)

mydividend=11
mydivisor=4

print(quotientandremainder(mydividend,mydivisor))
#tuple allow us to store value
tupleresults=quotientandremainder(mydividend, mydivisor)

print("Quotient:",tupleresults[0])
print("Remainder:", tupleresults[1])
#----------------------------------------------------------------------------------------
#Using unpacking approach

def quotientandremainder(dividend, divisor):
    return (dividend//divisor, dividend%divisor)

mydividend=11
mydivisor=4

(myquotient, myremainder)=quotientandremainder(mydividend,mydivisor)
print("Quotient:",myquotient)
print("Remainder:",myremainder)
#-------------------------------------------------------------------------------------
mytuple1=(1,2,3)#0  >index value
mytuple2=(4,5,6)#1
mytuple3=(7,8,9)#2

mysupertuple=((1,2,3),(4,5,6),(7,8,9))
print(mysupertuple)
#how to access individual values
print(mysupertuple[1][0]) #index value  [1][0]=2nd row 1st number

#------------------------------------------------------------------------
#List as tuples
mylist1=[1,2,3]
print(mylist1)
print()

myint1=1
myint2=2
myint3=3
mylist2=[myint1,myint2,myint3]
print(mylist2)
print()
#-----------------------------------------------------------------
#different techniques/methods
mylist=[17,12,9,18,11,7,13,14,1,4,6,8,9,7,66,2,66]
print(mylist, ":Original List")

mylist.sort()
print(mylist, ":After Sorting")

mylist.append(21)
print(mylist, ":After appending 21")

myotherlist=[26,22,23,24]
mylist.extend(myotherlist)
print(mylist, ":after extending with myotherlist")

mylist.insert(15,25)
print(mylist, ":After inserting 25 at the index 25")

mylist.remove(26)
print(mylist, ":after removing 26")

mylist.reverse()
print(mylist, ":After reversing")

mylist.pop()
print(mylist, ":After popping")
#after deleting the last five items
del mylist[-5]
print(mylist.index(23), ":Index of 23")
print(mylist.count(15), ":Count of 15")
print(4 in mylist, ":4 in mylist")

#---------------------------------------------------------------------




#-------------------------------------------------------------------------
