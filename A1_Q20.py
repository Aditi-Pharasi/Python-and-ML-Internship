#20. Write a python program that takes a list of numbers and returns their sum.
sum=0
n=int(input("Enter the size of list :"))
List=[]
for i in range(n):
    number=int (input("Enter a number:"))
    List.append(number)
for i in List:
    sum=sum+i

print(sum)