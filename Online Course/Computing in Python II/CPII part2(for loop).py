##for loop

for i in range(1,11):
    print("Before addition: ", i)

    i+=1
    print("After addtion: ", i)

#---------------------------------------------------------------------    
##sum=0
##for i in range(1,11):
##    nextNumber=int(input("Enter the number #" +str(i )+ ":"))
##    sum+=nextNumber
##print(sum/10)

#---------------------------------------------------------------------

sum=0
numcount=int(input("How many numbers will you average?"))
for i in range(1,numcount+1):
    nextNumber=int(input("Enter the number #" +str(i )+ ":"))
    sum+=nextNumber
print(sum/numcount)

#---------------------------------------------------------------------
#For-each and lists

listofnumbers=[91, 92, 93 ,94, 95, 96, 97, 98, 99,100]
sum=0
      
for i in range(0, len(listofnumbers)):
    currentnumber=listofnumbers[i]
    sum+=currentnumber
print(sum/len(listofnumbers))
#-------------------------------------------------------------
mystring="There are seven words in this string"
numspaces=0

for currentcharacter in mystring:
    if currentcharacter == " ":
        numspaces+=1
print("There are " + str(numspaces +1) + " words in the strings.")

#-----------------------------------------------------------------------
##while loop

i=1
while i<11:
    print(i)
    i+=1
#------------------------------------------------------------------------
##infinite loop
##i=1
##while i>0:
##    print(i)

#-------------------------------------------------------------------------
listofstrings= ["This is the first string", "This is the second string",
                "This is the third string", "This is the fourth string",
                "This is the fifth string"]

numspaces=0
for currentstring in listofstrings:
    for currentcharacter in currentstring:
      if currentcharacter == " ":
          numspaces +=1
numwords=numspaces+ len(listofstrings)
print("There are ", numwords, " words in the strings.")
#--------------------------------------------------------------------------
for i in range(1,21):
    if i%2==0:
        continue
    print(i, "is odd.")
print("Done!")
#---------------------------------------------------------------------------
numCount=int(input("How many numbers would you like to average?"))

for i in range(1, numCount+1):
    sum=0
    nextnumber=int(input("Enter number #" +str(i) +":"))
    sum+=nextnumber
print(sum /numCount)

