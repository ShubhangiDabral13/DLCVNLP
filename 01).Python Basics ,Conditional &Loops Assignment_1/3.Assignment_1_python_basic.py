"""
Ques:-
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r^3
"""
import math
def volume(r,pi):

    vol = 4.0/3.0 * pi* math.pow(r,3)
    print(vol)


pi = 3.1415926535897931
volume(4,pi)
