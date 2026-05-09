# Program to check palindrome

import string

text = input("Enter a string: ")

# Remove spaces and punctuation
cleaned = ""

for ch in text.lower():
    if ch not in string.punctuation and ch != " ":
        cleaned += ch

# Check palindrome
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#output
#Enter a string: Madam
#Palindrome
