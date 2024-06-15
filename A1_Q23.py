#23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

print("1. convert Celsius to Fahrenheit \n2. Convert Fahrenheit to Celsius")
n=int (input("Enter your choice: "))
if(n==1):
    temp=int(input("Enter Temperature in celsius: "))
    fahrenheit = (temp * 9/5) + 32
    print("temperature in fahrenheit: ",fahrenheit)
elif(n==2):
    temp=int(input("Enter Temperature in fahrenheit : "))
    celsius = (temp - 32) * 5/9
    print("temperature in celsius: ",celsius)

else:
    print("incorrect choice")