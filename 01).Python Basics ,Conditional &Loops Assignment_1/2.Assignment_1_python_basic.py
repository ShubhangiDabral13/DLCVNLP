"""
Ques:-
Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between
first name and last name.
"""

def print_reverse(name):
    for i in range(len(name)-1,-1,-1):
        print(name[i],end="")
    print()

name = str(input("Enter your fullname"))
print_reverse(name)
