"""
Ques:
Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()
"""
# Reduce will produce a single result
def my_reduce(func, num):

 # Get first item in sequence and assign to result
  final = num[0]
 # iterate over remaining items in sequence and apply reduction function
  for i in num[1:]:
   final = func(final, i)

  return final


  # test myreduce function
def sum(x,y):
    return x + y


print ("Sum on list [4,5,3] using my reduce function "   + str(my_reduce(sum, [4,5,3])) )
