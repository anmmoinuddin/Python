##tuple----------------------------------------------------------------
mytuple=(1,2,3)
print(mytuple)
#tuple remains unchanged
int1=1
int2=2
int3=3
mytuple=(int1,int2,int3)
print(mytuple)
#tuple remains unchanged----------------------------------------------
int1="Hello World"
int2=5.2
int3=3
mytuple=(int1,int2,int3)
print(mytuple)
#Access individual Tuple----------------------------------------------
mystring="Hello World"
myfloat=5.1
myinteger=5
mytuple=(mystring,myfloat,myinteger)
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
#Access individual Tuple----------------------------------------------
mystring="Hello World"
myfloat=5.1
myinteger=5
myint1=2
myint2=-1
mytuple=(mystring,myfloat,myinteger,myint1,myint2)
#print values from #4
print(mytuple[3:])
#print first two values
print(mytuple[:2])
#print the second and third values
print(mytuple[1:3])
#print the last three values
print(mytuple[-3:1])
#print all but the last three values of tuple
print(mytuple[:-3])
#-------------------------------------------------------------------
#Unpacks tuple into these variable to see individual item------------------------
mystring="Hello World"
myfloat=5.1
myinteger=5
myint1=2
myint2=-1
mytuple=(mystring,myfloat,myinteger,myint1,myint2)

(mynewstring,mynewfloat,mynewinteger,mynewint1, mynewint2)=mytuple

print(mynewstring)
print(mynewfloat)
print(mynewinteger)
print(mynewint1)
print(mynewint2)
