#12. Write a python program that calculates the sum of the digits of a given number.
n=1256
sum=0
while(n):
    digit=n%10
    sum+=digit
    n=int(n/10)
print("sum of digits:",sum)
