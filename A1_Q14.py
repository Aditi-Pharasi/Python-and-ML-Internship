# 14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
n=''
while True:
    inn=input("Enter the input line: ")
    if(inn): 
        n+=inn
        
    else:
        break

print(n)