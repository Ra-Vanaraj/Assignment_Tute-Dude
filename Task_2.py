"""
Python program that:

1. Takes user's first name and last name as input
2. Concatenate the first and last name into a full name
3. Prints a personalised greeting message using the full name.
"""

f=input("Enter your first name: ")
l=input("Enter your last name: ")
name=f+' '+l
message="Hello "+name+"! Welcome to the Python program."
print(message)
