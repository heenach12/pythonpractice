"""Design a data-structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack. Your task is to complete all the functions, using stack data-Structure.


Example 1:

Input:
Stack: 18 19 29 15 16
Output: 15
Explanation:
The minimum element of the stack is 15."""

def push(arr, ele):
    arr.append(ele)

    # Code here

# Function should pop an element from stack
def pop(arr):
    return arr.pop()
    # Code here

# function should return 1/0 or True/False
def isFull(n, arr):
    if len(arr) == n:
        return True
    else:
        return False

    # Code here

# function should return 1/0 or True/False
def isEmpty(arr):
    if len(arr) == 0:
        return True
    return False

    # Code here

# function should return minimum element from the stack
def getMin(n, arr):
    return min(arr)
    # Code here
