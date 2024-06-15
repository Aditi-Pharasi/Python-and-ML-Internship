#22. Write a python program that returns the minimum and maximum values in a list of numbers
List=[4,6,7,2,5,7,3]
mini=List[0]
maxi=List[0]
for i in List:
    if(i<mini) : mini=i
    elif(i>maxi) : maxi=i

print("Maximum value in the list: ", maxi,"\n Minimum value in the list: ", mini)
