#range function returns a sequence of nos, starting 
# from 0 by default,# increments by 1(by default) 
# and ends at a specified number

for x in range(6):
    print(x)

#The range() function defaults to increment the sequence
# by 1, however it is possible to specify the increment 
# value by adding a third parameter: 

for x in range(2, 30, 3): 
    print(x)

#for loops cannot be empty, but if you for some reason
#have a for loop with no content, put in the pass 
#statement to avoid getting an error.

for x in [0,1,2]:
    pass

Example    