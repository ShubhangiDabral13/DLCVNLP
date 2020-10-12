"""
Ques:
Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

def pattern():

    for i in range(5):
        for j in range(i):
            print("*",end=" ")
        print()

    for i in range(5,-1,-1):
        for j in range(i):
            print("*",end=" ")
        print()

pattern()
