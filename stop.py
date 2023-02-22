from mapper import getDistances

def closestDistance(old, new):
    '''
    This function checks the distances from source for every node after each iteration.
    If the distance for all nodes in the graph before and after an iteration comes out 
    to be equal, then the stop condition is met and the program exits the loop.
    '''

    # Since integer values 1 and 0 are equivalent to the boolean values True and False.
    check = [int(old[idx][1] != new[idx][1]) for idx in range(len(old))] 
    
    if sum(check) == 0: # executes when all the check list elements are zero.
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    old = getDistances('distance.txt')
    new = getDistances('distance1.txt')
    
    closestDistance(old, new)
