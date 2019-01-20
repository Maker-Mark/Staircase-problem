# The staircase problem: 
# With a n that describes the number of steps in the staircase,
# make a function that return the total number of ways you can climb the staircase
# while obeying the following constraints: You can either take small steps (one at a time) OR big steps (2 at a time). 

a = 9 # size of our staircase

# We can solve this problem both iteratively and recursively
# recursive solution:


def num_ways(n):
  if n == 0 or n == 1:
    return 1
  else:
    return num_ways(n-1) + num_ways(n-2) #Does this relation look familiar?
print('You can climb a staircase with ' + str(a) + " steps " + str(num_ways(a)) + " ways!")

# the recursive nature of the above code has some inefficiencies, as 
# num_ways(2) will be calculated multiple times. 
# Let's take a look at the non-recursive solution to see how they differ.
# non-recursive solution:
