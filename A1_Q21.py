#21 Write a python program that counts the occurrences of a specific element in a list
List=[4,6,7,2,5,7,3]
count=0
n=int(input("Enter the element to count its occurences in list"))
for i in List:
    if(i==n): count=count+1

print("No. of Occurences of element :",count)