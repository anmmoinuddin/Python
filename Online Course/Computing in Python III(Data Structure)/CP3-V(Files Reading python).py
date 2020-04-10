#Simple file Reading

inputFile=open("OutputFile.txt", "r")


print(inputFile.readline().strip())
print(inputFile.readline().strip())
print(inputFile.readline().strip())

inputFile.close()
#------------------------------------------------
mylist=[]


inputFile=open("OutputFile.txt", "r")

for line in inputFile:
    mylist.append(line.strip())


print(mylist)
inputFile.close()
#-------------------------------------------------------
mylist=[]

inputFile=open("OutputFile.txt","r")

myint1=int(inputFile.readline())
myint2=int(inputFile.readline())
myint3=int(inputFile.readline())

for line in inputFile:
    mylist.append(line.strip())

print(myint1)
print(myint2)
print(myint3)

inputFile.close()
#------------------------------------------------------------
