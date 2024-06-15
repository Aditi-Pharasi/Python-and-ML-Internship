# 16. Write a program in python that counts the frequency of each character in a string
s=input("Enter the string: ")
count=0
d={}
for i in s:    # Loop through each character in the input string
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
    

print("character : frequency ")
for j in d.keys():
    print(j," : ",d[j])