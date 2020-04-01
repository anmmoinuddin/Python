## Try catch

##mystring="This string is not a number!"
##print("Converting mystring to int")
##myint=int(mystring)
##print(myint)
##print("Done!")
#-----------------------------------------------------------------------
## Try catch

mystring="This string is not a number!"
try:
    print("Converting mystring to int")
    myint=int(mystring)
    print(myint)
    #if error occurs in this try block jump to next code
except:
    pass
print("Done!")

#-----------------------------------------------------------
mystring="This string is not a number!"
try:
    print("Converting mystring to int")
    myint=int(mystring)
    print(myint)
    #if error occurs in this try block jump to next code
except:
    print("Cant convert: mystring not a number")
print("Done!")
#-----------------------------------------------------------------
mystring="This string is not a number!"
try:
    print("Converting mystring to int")
   
    myint=int(mystring)
    print(myint)
    #if error occurs in this try block jump to next code
except ValueError :
    print("Cant convert: mystring not a number")
print("Done!")
#------------------------------------------------------------------
mystring="This string is not a number!"
try:
    print("Converting mystring to int")
    
    myint=int(mystring)
    print(myint)
    #if error occurs in this try block jump to next code
except ValueError as error:
    print(error)
print("Done!")
#------------------------------------------------------------------
mystring="This string is not a number!"
try:
    print("Converting mystring to int")
    print("String #" +  1 + ":" + mystring)#Typeerror
    myint=int(mystring)#Valueerror
    print(myint)
    print(1/0)
    #if error occurs in this try block jump to next code
##We can create several except likewise elseif statement.
        #----------------------------------------------
except ValueError as error:
    print(error)
except TypeError as error:
    print(error)
print("Done!")
#--------------------------------------------------------------------------
#Another approach by using several error in one except block
#------------------------------------------------------------------
mystring="This string is not a number!"
try:
    print("Converting mystring to int")
    print("String #" +  1 + ":" + mystring)
    myint=int(mystring)
    print(myint)
    print(1/0)
    #if error occurs in this try block jump to next code
except (ValueError, TypeError) as error:
    print("A valueerror or typeerror occurred")
except Exception as error:
    print("Some other type of error occured")
print("Done!")

