import copy # For deepcopy 

"""
Author - Rohith Prabakar
This is done to solve the viral jailor problem
PROBLEM:
[[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]]
A prisoner is dead in block 13,
his body must be removed through block 4 
after passing all of the other blocks.
IS IT POSSIBLE?
"""

#SOLUTION


def checkPassedAll(lst):
    # Checks if all positions has been passed
    # lst is list
    for i in lst:
        for j in i:
            if j == False:
                return False
    return True

def hasElement(lst,r,c):
    # lst is 2D square matrix
    if r < 0 or c < 0 or r > len(lst) - 1 or c > len(lst) - 1:
        return False
    return lst[r][c] == False # returns true if it is not passed

def getUp(r,c):
    # gets the up position
    return [r-1,c]

def getRight(r,c):
    # gets the right position
    return [r,c+1]

def getDown(r,c):
    # gets the down position
    return [r+1,c]

def getLeft(r,c):
    # gets the left position
    return [r,c-1]

def canCross(r,c,lst):
    # returns true if there is a unique cross
    # r is row, c is column, and lst is list
    output = [] 
    lst[r][c] = True #updates the list
    if r == 0 and c == len(lst) - 1:
    	return checkPassedAll(lst)
    else:
    	a,b = getUp(r,c)
    	if hasElement(lst,a,b):
    		output.append(canCross(a,b,copy.deepcopy(lst)))
    	a,b = getDown(r,c)
    	if hasElement(lst,a,b):
    		output.append(canCross(a,b,copy.deepcopy(lst)))
    	a,b = getLeft(r,c)
    	if hasElement(lst,a,b):
    		output.append(canCross(a,b,copy.deepcopy(lst)))
    	a,b = getRight(r,c)
    	if hasElement(lst,a,b):
    		output.append(canCross(a,b,copy.deepcopy(lst)))
    	return True in output

# r represents row and c represents column
passed = [
        [False,False,False,False],
        [False,False,False,False],
        [False,False,False,False],
        [False,False,False,False]
        ]
r,c = 3,0 # 13 is 3,0
print(canCross(r,c,passed))
