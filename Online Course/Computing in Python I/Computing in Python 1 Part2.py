

#In operator in python

myString ="Hello, world"
print("H" in myString)
print("lo, w" in myString)
print("oll" in myString)

# Mathematical Operator

myNum=5
print(myNum)
myNum=myNum+3
print(myNum)
myNum=myNum-3
print(myNum)
myNum=myNum*3
print(myNum)
myNum=myNum//3# floor division
print(myNum)
myNum=myNum**3#exponential 
print(myNum)
myNum=myNum%3#modulus
print(myNum)

#length of string

myString="Hello, world"
print(myString)
    #find the length of myString
myString=str(len(myString))
print(myString)
    #find the length again
myString=str(len(myString))
print(myString)


#Incrementingandloops
letterCount=0

    #Run this code for each letter in the string
for character in "Hello, world":
    #Add one to lettercount
    letterCount+=1
print(letterCount)

# Checking if a triangle exists
side1=int(input("Enter the shortest side: "))

side2=int(input("Enter the next shortest side: "))

side3=int(input("Enter the shortest side: "))

result=(side1+side2)>side3
print("These sides can form a triangle" , result)

#create the string
myString= "Hello, World"
myString+="!"
print(myString)


myAString="A"
myBString="B"
myCString="C"
    # Sorting the string alphabetically
print(myAString<myBString)
print(myCString<myAString)
print(myAString==myAString)
print(myAString<myaString)
  #string multiplication
myAString="A"
myInt=5
print(myAString*myInt)



