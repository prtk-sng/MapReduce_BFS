#!/usr/bin/env python3
import sys

def shortestPath():
    # empty dictionary to store nodeIDs as keys and their shortest distance from source as values.
    container = {} 

    for line in sys.stdin:
        node, distance = line.split('\t')
        try:
            node = int(node)
            distance = int(distance)
        except ValueError:
            continue
        
        if node in container.keys():
            # check and store the shortest distance.
            curr_distance = container[node]
            if distance < curr_distance:
                # update shortest distance in the container.
                container[node]=distance 
            else:
                continue
        else:
            # create key value pair if node not found in container.
            container[node] = distance

    for node in container:
        # emit node ID along with shortest distance from source.
        print(str(node)+ ": " +str(container[node]))


if __name__ == "__main__":
    shortestPath()
