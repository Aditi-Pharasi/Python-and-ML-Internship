# 13. Write a program that asks the user for their birth year and calculates their age.
from datetime import date
user_birth_year=int(input("Enter your birth year: "))
current_age=date.today().year - user_birth_year
print("your current age is : ", current_age)