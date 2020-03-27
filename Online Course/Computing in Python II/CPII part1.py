##Control Structure

#if

myNum1=3
myNum2=2

if myNum1<myNum2:
    print("myNum2 is greater than myNum1")
    print("Yes it is!")
    print("Yes it is!")

print("Execution complete")
#---------------------------------------------------------------------------------
#Thedangers of Scope

myNum1=3
myNum2=2
result="Unchange"  # if you declared early then no possibilty to show error
if myNum1<myNum2:
     
    result="mynum2 is greater than mynum1"
print(result)
print("Execution complete")
#--------------------------------------------------------------------------------
##Relational and Mathematical Operators with if/else

balance=20
purchasePrice=19
salesTax=1.08

if balance>=purchasePrice*salesTax:
    print("Purchase possible!")
else:
    print("Purchase not possible")
print("Done!")

##SetMemship Operator
jacketWeather=["cold", "windy","raining","snowing"]
todaysWeather="raining"

if todaysWeather in jacketWeather:
    print("jacket")
print("Done!")
#------------------------------------------------------------------------------

##Boolean Function

myNumericString="12345"
myNonNumericString="ABCDE"

if myNumericString.isdigit(): #isdigit() acts as boolean
    print("The first String is numerical")

else:
    print("The first String is nonnumerical")

if myNonNumericString.isdigit():
    print("The Second string is numerical")
else:
    print("The Second string is non-numerical")

## boolean operator
todaysweather ="cold"
if todaysweather =="cold" and todaysweather=="windy":
    print("jacket")
print("Done")
#----------------------------------------------------------------------------
##Boolean operator with logical operation
#-----------------------------------------


balance=20
salesTax==1.08
cardholdersname="Moin"
trustedvendors=["Maria","bob", "Masoud", "John"]
purchaseprice=19
customername="Moin"
vendor="Masoud"
 

if balance>=purchaseprice*salesTax and cardholdersname==\
       customername and vendor in trustedvendors:   #same statement 
    print("Purchase approved")
else:
    print("Declined")
print("Done")
 #       ---------------------------------------
    #bank overdraft
balance=20
salesTax==1.08
cardholdersname="Moin"
trustedvendors=["Maria","bob", "Masoud", "John"]
purchaseprice=19
customername="Moin"
vendor="Masoud"
overdraftprotection=True

if balance>=purchaseprice*salesTax and cardholdername==\
       customername and vendor in trustedvendors:   #same statement 
    print("Purchase approved")
else:
    print("Declined")
print("Done")
if (balance>=purchaseprice*salesTax or overdraftprotection) and cardholdersname==\
       customername and vendor in trustedvendors:   #same statement 
    print("Purchase approved")
else:
    print("Declined")
print("Done")
#-------------------------------------------------------------------------------------
##Imagine you're writing code for a cash register at a restaurant.
#This restaurant serves burritoes. The base price of a burrito is $8.
#If the customer wants steak or pork, it adds $0.50.
#If they want quacamole, it adds $1.00. If they want queso, it adds $1.00.
#The customer may only select one meat, but they may have both queso and guacamole,
#neither, or just one.

steak=False
pork=True
guacamole=False
queso=False

price=5
if steak or pork:
    price+=0.50
elif guacamole:
    price+=1
else:
    price+=1
print(price)
