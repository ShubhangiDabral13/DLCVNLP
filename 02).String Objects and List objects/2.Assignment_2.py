"""
Ques:
Write a Python program to reverse a word after accepting the input from the user.
Sample Output:
Input word: ineuron
Output: norueni
"""

def reverse(s):

    s = s[::-1]
    print(s)

s = str(input("Enter a word"))
reverse(s)
