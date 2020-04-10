#Simple file writing
myint1=12
myint2=54
myint3=85

outputFile=open("OutputFile.txt", "w")


outputFile.write(str(myint1)+"\n")
outputFile.write(str(myint2)+"\n")
outputFile.write(str(myint3)+"\n")

outputFile.close()

#----------------------------------------------------
mylist=["David", "Lucy", "Thomas","Ping", "Dana", "Addison", "Jasmin"]

outputFile=open("OutputFile.txt", "w")

outputFile.writelines(mylist)
outputFile.close()

#----------------------------------
mylist=["David", "Lucy", "Thomas","Ping", "Dana", "Addison", "Jasmin"]

outputFile=open("OutputFile.txt", "w")

for name in mylist:
    outputFile.write(name+"\n")
outputFile.close()
#----------------------------------------------------
myint1=12
myint2=54
myint3=85
mylist=["David", "Lucy", "Thomas","Ping", "Dana", "Addison", "Jasmin"]

outputFile=open("OutputFile.txt", "w")

outputFile.write(str(myint1)+"\n")
outputFile.write(str(myint2)+"\n")
outputFile.write(str(myint3)+"\n")
outputFile.write("\n".join(mylist))

outputFile.close()
#---------------------------------------------------------------
#appending to files
myint1=12
myint2=54
myint3=85

# "a " append function to write two times/ in comparison to "w"
outputFile=open("OutputFile.txt", "a") 

outputFile.write(str(myint1)+"\n")
outputFile.write(str(myint2)+"\n")
outputFile.write(str(myint3)+"\n")

outputFile.close()
#---------------------------------------------------------------------
#appeding to Files
mylist=["David", "Lucy", "Thomas","Ping", "Dana", "Addison", "Jasmin"]

outputFile=open("OutputFile.txt", "a")
#outputFile=open("OutputFile.txt", "w")

for name in mylist:
    print(name, file=outputFile)

outputFile.close()
#-------------------------------------------------------------------------

