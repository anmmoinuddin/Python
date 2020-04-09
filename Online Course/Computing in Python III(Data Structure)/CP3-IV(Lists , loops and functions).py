#Functions
grades=[100,95,93,90,89,87,85,80,85,84,82,75]

sum=0
count=0

for grade in grades:
    count=count+1
    sum=grade
print(sum/count)

#---------------------------------------------------------------
# averages the numbers in a list

def average(inlist):
    sum=0
    for number in inlist:
        sum+=number
    return sum/len(inlist)

mylist1=[1,2,3,4,5,6,7,8,9]
mylist2=[97,87,91,83,91,85,95,85,75]

print("The average of mylist1 is:", average(mylist1))
print("The average of mylist2 is:", average(mylist2))
#----------------------------------------------------------------
#Iteratingover2Dimensionallist

def TwoDaverage(in2DList):
    result=[]
    #for each list in the list of lists
    for numlist in in2DList:
        sum=0
        for number in numlist:
            sum+=number
        result.append(sum/len(numlist))
    return result

my2DList=[[91,95,89,92,56],
          [85,87,91,81,82],
          [79,75,85,83,89],
          [81,89,91,91,90],
          [99,91,95,89,90]]
print("Averages:", TwoDaverage(my2DList))
#-------------------------------------------------------------------
#Removing a number from a list
def TwoDaveragewithpop(in2DList):
    result=[]
    #Repeat until 2DList is empty
    while len(in2DList)>0:
        #Remove and assign the last item of in 2DList to numlist
        numList=in2DList.pop()
        sum=0
        count=0
        #Repeat until numlist is empty
        while len(numList)>0:
            number=numList.pop()   #pop() methods removing a value from list 
            sum+=number
            count+=1
        #Insert this average at the beginning of result    
        result.insert(0,sum/count)
    return result

my2DList=[[91,95,89,92,56],
          [85,87,91,81,82],
          [79,75,85,83,89],
          [81,89,91,91,90],
          [99,91,95,89,90]]
print("Averages:", TwoDaveragewithpop(my2DList))
print("my2DList:", my2DList)
#--------------------------------------------------------------------------
mystring="Hello, world"
mylist=[4,1,2,3]

print("mystring before upper():", mystring)
print("mylist before sort():", mylist, "\n")

mystring.upper()
mylist.sort()

print("mystring after upper():", mystring)
print("mylist after sort():", mylist, "\n")

