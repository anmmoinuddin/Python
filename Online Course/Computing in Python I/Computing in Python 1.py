from datetime import date
import keyword

myInt=5
print(myInt)
myfloat=5.1
print(myfloat)
mydate=date.today()
print(mydate)

#comments

def countdown(i):
    for j in range(1, i+1):
        print(j, end="    ")
    print()

countdown(10)
countdown(5)


#boolean and other number and string
c=2
d="Hello"
e=True
print(c*d)
print(e*c)

a = "Hello"
b = "world"
c = a + b
d = print(c)
print(d)

#some keywords which python has
print(keyword.kwlist)

#date
myDate=date.today()
print(myDate.year)
print(myDate.month)
print(myDate.day)

#Numeric equality comparison
print(2==2)
print(5==2)
a=2
b=2
c=3
print(a==b)
print(a==c)
#print(a=c)

#Numeric value comparison
print(3>2)
print(3<5)
a=7
b=9
c=9
print(a<b)
print(a<c)

#No Numeric equality comparison
a="Hello, World"
b="Hello, World"
c="Hello"
d="World"

print(a==b)
print(a==c)
print(a== c+d)
print(a>b)
print(a>=b)
print(a>=d)

#In operator in python

myString ="Hello, world"
print("H" in myString)
print("lo, wd" in myString)
print("oll" in myString)
print(c>=b)



#In operator in python

myString ="Hello, world"
print("H" in myString)
print("lo, w" in myString)
print("oll" in myString)


