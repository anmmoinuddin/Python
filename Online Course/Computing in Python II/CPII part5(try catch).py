mystring="1"

try:
    print("Converting mystring to int")
    myint=int(mystring)
    print(myint)
except (ValueError, TypeError) as error:
    print("A valueerror or typeerrror occurred")
except Exception as error:
    print("Some other type of Error")
else:
    print("No errors occurred")
print("Done!")

## Else and file input
#---------------------------------------------------------------
try:
    inputFile=open("InputFile.txt", mode="r")
except IOError as error:
    print("An input error occurred")

else:
    #for each line in the file
    for line in inputFile:
        print(line)
    inputFile.close()
#---------------------------------------------------------------
inputFile=open("InputFile.txt", mode="r")
try:
    for line in inputFile:
        print(int(line))

except ValueError as error:
    print("An Value error occurred")

else:
    #for each line in the file
    print("No errors occurred")

inputFile.close()
#-----------------------------------------------------------------------
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
finally:
    print("An unknown error occurred")
print("Done!")
#------------------------------------------
def dividebyzero():
    print(1/0)
print("About to encounter an error....")
try:
    dividebyzero()
except Exception as error:
    print(error)
print("We just encountered an error")

