
##function Declaration

def printDollar():
    print("$", end='')

printDollar()
print(5)
#---------------------------------------------------------------------

def returnDollar():
    return "$"
print(returnDollar(),end="")
print(5)

#--------------------------------------------------------------------

def returnDollar():
    return "$"
print(returnDollar(), 5, sep="")

#-----------------------------------------------------------------------

def returnDollar(amount):
    return "$" +str(amount)
print(returnDollar(5))

#-----------------------------------------------------------------------

def returnDollar(amount):
    return "$" +str(amount)
inputamount=int(input("Enter the amount: "))
print(returnDollar(inputamount))
#----------------------------------------------------------------------
def currencyamount(currency, amount):
    if currency=="JPY":
       return "Y" +str(amount)
    elif currency=="USD":
       return "$" +str(amount)
    elif currency=="GBP":
       return "P" +str(amount)
    else: 
       return str(amount)
print(currencyamount("GBP", 5))
#------------------------------------------------------------------------
print("A", "B", "C", sep="#", end="")  #seperate
print("D", "E", "F", sep=" ", end="")
    
