"""
Ques:-
Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()
"""

# Custom filter function
def myfilter(func,m):

 # Initialize empty list
 final =  []
 # iterate over sequence of items in sequence and apply filter function
 for i in m:
  if func(i):
   final.append(i)

 # return funal output
 return final




# test myfilter function
def num_pos(n):
 if (n <= 0):
  return False
 else:
  return True


print ("Filter only positive Integers on list [0,-1,-2,-3,4,5]"  + str(myfilter(num_pos, [0,-1,-2,-3,4,5])))
