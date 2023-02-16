'''
Discussion 3 - ANLY-555
Author: Brendan Baker

Prompt:

You are tasked with design the most efficient algorithm to complete the following task. Implement a function findMedian(n) that

1. randomly generates n floating point values between 0 and 100. (Feel free to use random library)
2. compute and return the median value. Do not use a pre-existing median function or sorting function, but instead code it "from scratch". 
I encourage you to think about this design individually without the use of internet resources. 
That is one of the main goals of this exercise -- translate your sequence of steps needed to compute the median to Python code! 

Hint: First consider what steps you would take to find the median yourself. Next, write down these steps. Finally, translate these steps into Python Code.

Consider both time complexity and space complexity.

- Implement the above algorithm in Pseudo-code or Python code. Please code from "scratch" -- do not use others code.
- Assuming n is the length of the randomly generated values, derive a Step Count Function T(n) and Space Count Function S(n).
- Do this for both the best case and the worst case. Explain your counts line-by-line.
- Determine a tight-fit upperbound using Big-O notation. 
- Explain and justify why you believe this is an efficient solution

'''

import random

def findMedian(n):
    '''
    Function that finds the median of n floating point values between 0 and 100.
    '''
    values = [random.randint(0,100) for n in range(n)] # Generate n values within the parameters
    
    order = True 
    while order == True: # Keep going while values are still being sorted
        values_found = False # Start with no values having been sorted
        for i in (range(len(values)-1)): # Loop through entire range of values
            if values[i]>values[i+1]: # If the next value is less than the current
                order = True # Still ordering this cycle
                values_found = True # Note that we found a value and should not stop
                a = values[i] # Save the first value
                b = values[i + 1] # Save the second value
                values[i+1] = a # Switch them 
                values[i] = b 
            if not values_found:
                order = False # Stop the loop if no further elements are changed
    
    mid = len(values)//2 
    if len(values)%2 == 0: # If length is even
        median = (values[mid] + values[mid-1])/2 # Average of n//2 and n//2-1 index
    else: 
        median = values[mid] # Otherwise just n//2
    
    return(values, median)   

res = findMedian(100)
print(res)

'''
COMPLEXITY
---------------
Summary: Time complexity is not the best, with a worse case of O(n^2).  Space complexity is good and will stay constant around O(1).
Would be ideal in situations with high computational resources and low memory resources.



T(n)/S(n): declare function 1 ops
    values = [random.randint(0,100) for n in range(n)] # n ops, 1 space
    
    order = True # 1 ops, 1 space
    while order == True: # 1 - n*n ops, 1 space
        values_found = False # 1 ops, 1 space
        for i in (range(len(values)-1)): # 2-2n*n ops, 0 spaces
            if values[i]>values[i+1]: # 1 - n*n ops, 0 spaces
                order = True # 1 - n*n ops, 1 space
                values_found = True # 1 - n*n ops, 1 space
                a = values[i] # 1 - n*n ops, 1 space
                b = values[i + 1] # 1 - n*n ops, 1 space
                values[i+1] = a # 1 - n*n ops, 0 extra spcaes
                values[i] = b # 1 - n*n ops, 0 extra spaces
            if not values_found:
                order = False # 0 - n*n ops, 0 extra spaces
    
    mid = len(values)//2 # 1 ops, 1 spaces
    if len(values)%2 == 0: # 0 - 1 ops
        median = (values[mid] + values[mid-1])/2 # 0 - 1 ops, 1 space
    else: # 0 - 1 ops
        median = values[mid] # Otherwise just n//2 0 - 1 ops, 1 space
    
    return(values, median)  # 1 ops

Notation: 
TIME COMPLEXITY

WORST CASE:
10^2 + n + 7 or O(n^2)

BEST CASE: 
n + 14 or O(n)

SPACE COMPLEXITY
always about 7 spaces

WORSE CASE: 
O(1)

BEST CASE:
O(1)

'''


        
    