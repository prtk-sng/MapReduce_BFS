#!/usr/bin/env python3
import sys

# starting distances from the text file are obtained and added to an array.
def getDistances(initial_file):
    distances = []

    with open(initial_file) as file:
        lines = file.readlines()
        for line in lines:
            if line:
                try:
                    line = line.strip()
                    node, dist = line.split(': ')
                    distances.append([int(node), int(dist)])
                except:
                    break
            else:
                break

    file.close()
    return distances

# Emit the node IDs and the distance from source based on initialization.
def emitDistances(distances):
    '''
    For hassle free retrieval of distances for particular node, make a dictionary to store
    nodes as keys and their distance from source as values.
    '''
    dist_dic=dict((distances[i][0], distances[i][1]) for i in range(len(distances)))

    for line in sys.stdin:
        line = line.strip()
        curr_node, outlinks = line.split(': ')
        curr_node = int(curr_node)
        if outlinks != 'none':
            outlinks = [int(node) for node in outlinks.split()]

        try:
            # emit node and the distance to itself.
            print("%s\t%s" %(curr_node, dist_dic[curr_node]))

            if outlinks != 'none':
                for node in outlinks: # emit node IDs of outlinks and their distance from source.
                    print("%s\t%s" %(node, dist_dic[curr_node]+1))
        
        except:
            continue

if __name__ == "__main__":
    distances = getDistances('distance.txt')
    emitDistances(distances)