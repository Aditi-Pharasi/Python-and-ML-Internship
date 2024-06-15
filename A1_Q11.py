#11 Write a python program that generates the first n numbers in the Fibonacci sequence
first=0
second=1

n=int(input("Enter the number of elements required in Fibonacci :"))

print(first)
print(second)
while(n-2):
    third=first+second
    print(third)
    first=second
    second=third
    n=n-1
