#18 Write a python program that checks if two strings are anagrams of each other.

# Example usage
string1 = "saw"
string2 = "was"


# Remove any whitespace and convert strings to lowercase
s1 = string1.replace(" ", "").lower()
s2 = string2.replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print(string1," and ",string2," are anagrams.")
else:
    print(string1," and ",string2," are not anagrams.")
