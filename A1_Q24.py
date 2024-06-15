#24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result
num1=int (input("Enter the first number: "))
num2=int (input("Enter the second number: "))
operator=input("Enter the operator(+,-,*,/) to be performed on above numbers : ")

if(operator=='+'):
    print("The sum is : ", num1+num2)
elif(operator=='-'):
    print("The difference is : ", max(num1,num2)-min(num1,num2))
elif(operator=='*'):
    print("The product is : ", num1*num2)
elif(operator=='/'):
    print("The division is : ", num1/num2)
else:
    print("Invalid choice")


