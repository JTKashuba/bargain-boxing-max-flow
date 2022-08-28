"""
Author: JT Kashuba
Class: CIS 413 Winter '22
Homework 6: Implement Ford-Fulkerson to find max-flow in a bipartite graph.


Description:

You are to write code implementing the problem 10 from chap 11 of 
Erickson, slightly modified along the lines of the Luk’s Contest 
problem (available on class site). Suppose we are given a set of 
boxes, each specified by their height, width, and depth in inches.
All three side lengths of every box lie strictly between 1 inch and
36 inches. As you should expect, one box can be placed inside
another if the first box can be rotated so that its height, width,
and depth are respectively at least one inch smaller smaller than
the height, width, and depth of the second box. Boxes can be nested
recursively. Call a box visible if it is not inside another box.
Write code that will determine the smallest number of visible boxes.
Your code should use standard input/output. A test file will start
with an integer n (1 ≤ n ≤ 50), being the number of boxes. After that
will follow n lines of the form l w h (1 ≤ l, w, h ≤ 36), where the
three integers give the length, width, and height of that box.

Sample Input 1:
4
2 1 3
4 3 5
2 3 4
4 5 6

Sample Input 2:
5
5 5 5
4 4 5
4 5 5
2 3 3
5 6 6

The test files will end with a single blank line. The output for sample 1 should be 1 and for sample
2 it should be 3.
"""

import sys
from collections import defaultdict

numBoxes = int(sys.stdin.readline())

boxes = defaultdict(list)
#print(f'boxes defaultdict initialized as: {boxes}')

# for each box in the data set
for i in range(numBoxes):
    # obtain the data for the current box from std.in
    dimsStr = sys.stdin.readline()          # still represented in string form i.e. "2 1 3"

    # identify and store the individual dimensions in a nicely organized reformat

    dims = dimsStr.split()                  # makes a list of strings i.e. ['2', '1', '3']
    intDims = [int(dim) for dim in dims]    # re-types the list contents to ints i.e. [2, 1, 3]
    intDims.sort()                          # re-order the dimensions from smallest to largest
    boxes[i] = intDims                      # store the dimensions of box b_i in boxes[i]
    
    #print(f'boxes on iteration #{i}: {boxes}')

#print(f'final data set in boxes: {boxes}')


#####################################################################################
#
# ===========================================================================================
#   Detailed walkthrough for how this system works when computing inSample1.txt
# ===========================================================================================
#   * Note *: any extra 'whitespace' in the matrix Figures below is purely to aid the reader
#   in differentiating information in digestible chunks or to more clearly show columns. 
#   Any future developers of this codebase can easily verify the intermediate representations
#   of the graph by uncommenting the print statements throughout nestingBoxes_maxFlow.py
# ===========================================================================================
#
#       First the bipartite graph between L boxes b_i and R boxes b_i' is constructed.
#   At this point the adjacency matrix is far from complete, and of the following form:
#
# FIGURE A:
#     __ b0' b1' b2' b3'  __
#    |                     |
# b0 | [ 0,  1,  1,  1 ],  |
# b1 | [ 0,  0,  0,  1 ],  |
# b2 | [ 0,  1,  0,  1 ],  |
# b3 | [ 0,  0,  0,  0 ]   |
#    |__                 __|

#
#     This is obviously not enough information to represent the entire graph,
# it currently only shows which boxes b_i can fit inside of boxes b_i'
#
# Ultimately we need to represent each of the following:
#   1. s
#   2. the vertices for the L side of the bipartite graph b_i
#   3. the vertices for the R side of the bipartite graph b_i'
#   4. t
#
#
# FIGURE B:
#     __ s   b0 b1 b2 b3   b0' b1' b2' b3'   t    __
#    |                                             |
# b0 | [ 0,   0, 0, 0, 0,   0,  1,  1,  1,   0 ],  |
# b1 | [ 0,   0, 0, 0, 0,   0,  0,  0,  1,   0 ],  |
# b2 | [ 0,   0, 0, 0, 0,   0,  1,  0,  1,   0 ],  |
# b3 | [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   0 ]   |
#    |__                                         __|
#
#
# FIGURE C:
#     __ s   b0 b1 b2 b3   b0' b1' b2' b3'   t    __
#    |                                             |
# b0 | [ 0,   0, 0, 0, 0,   0,  1,  1,  1,   0 ],  |
# b1 | [ 0,   0, 0, 0, 0,   0,  0,  0,  1,   0 ],  |
# b2 | [ 0,   0, 0, 0, 0,   0,  1,  0,  1,   0 ],  |
# b3 | [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   0 ],  |
#    |                                             |
# b0'| [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   1 ],  |
# b1'| [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   1 ],  |
# b2'| [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   1 ],  |
# b3'| [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   1 ],  |
#    |__                                         __|
#
#
#  the final adjacency matrix will be of the form:
# FIGURE D:
#     __ s   b0 b1 b2 b3   b0' b1' b2' b3'   t    __
#    |                                             |
#  s | [ 0,   1, 1, 1, 1,   0,  0,  0,  0,   0 ],  |
#    |                                             |
# b0 | [ 0,   0, 0, 0, 0,   0,  1,  1,  1,   0 ],  |
# b1 | [ 0,   0, 0, 0, 0,   0,  0,  0,  1,   0 ],  |
# b2 | [ 0,   0, 0, 0, 0,   0,  1,  0,  1,   0 ],  |
# b3 | [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   0 ],  |
#    |                                             |
# b0'| [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   1 ],  |
# b1'| [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   1 ],  |
# b2'| [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   1 ],  |
# b3'| [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   1 ],  |
#    |                                             |
#  t | [ 0,   0, 0, 0, 0,   0,  0,  0,  0,   0 ]   |
#    |__                                         __|
#
#
#####################################################################################

# init data structure for bipartite graph
# 0 means "can not fit inside", and 1 means "can fit inside"
bipartiteGraph = [[0 for i in range(numBoxes)] for j in range(numBoxes)]

# for each box, determine whether the current box b_i can fit inside each of the other boxes b_j's
for i in range(numBoxes):
    for j in range(numBoxes):
        # all 3 dimensions must be smaller in order for box_i to fit inside of box_j
        # NOTE: WARNING! this is hard-coded! It is safe to assume that boxes will always
        # have 3 dimensions L x W x H, but if the parameters of the problem change, this will need updating.
        if boxes[i][0] < boxes[j][0] and boxes[i][1] < boxes[j][1] and boxes[i][2] < boxes[j][2]:
            bipartiteGraph[i][j] = 1  # box b_i fits inside of box b_j
#print(f'\nbipartiteGraph FIGURE A:\n{bipartiteGraph}\n')

#######################################################################
#### AT THIS POINT bipartiteGraph is of the form in FIGURE A above ####
#######################################################################

# expand the rows for each box b_i by an amount equal to numBoxes
# these new indices represent the b_i columns
for i in range(numBoxes):
    for num in range(numBoxes):
        bipartiteGraph[i].insert(0,0)
    
# expand the rows for each box b_i by 2
# these new columns represent s and t at the 0th and (numBoxes*2-1+2)'th indices
for i in range(numBoxes):
    bipartiteGraph[i].insert(0,0)
    bipartiteGraph[i].append(0)

#print(f'\nbipartiteGraph FIGURE B:\n{bipartiteGraph}\n')

#######################################################################
#### AT THIS POINT bipartiteGraph is of the form in FIGURE B above ####
#######################################################################

# add numBoxes more rows to represent the R boxes b_i'
for i in range (numBoxes):
    bipartiteGraph.append([0 for eachBox in range(numBoxes*2)])  # numBoxes*2 = both L b_i and R b_i'
    # account for s and t
    bipartiteGraph[numBoxes+i].insert(0,0)  # numBoxes+i to place b_i' rows after b_i rows
    bipartiteGraph[numBoxes+i].append(1)

#print(f'\nbipartiteGraph FIGURE C:\n{bipartiteGraph}\n')

#######################################################################
#### AT THIS POINT bipartiteGraph is of the form in FIGURE C above ####
#######################################################################

# Now we just have to insert s and t

# s has an edge to every L b_i with capacity 1 and no edges to any R b_i'
node_s = [0 for i in range((numBoxes*2)+2)]  #numBoxes*2 + 2 = both L b_i and R b_i' + s&t
for i in range(numBoxes):
    # s has a directed edge to each box b_i
    node_s[1+i] = 1     # Recall: the 0th column is s, the 1st is box1, etc. (visual aids in Figures above)

# t has an edge from every R box' with capacity 1 and none to any L box
# since t has no directed edges towards any vertex, we can leave it initialized with all 0's
node_t = [0 for i in range((numBoxes*2)+2)]  #numBoxes*2 + 2 = both L b_i and R b_i' + s&t


bipartiteGraph.insert(0,node_s)
bipartiteGraph.append(node_t)

#print(f'\nbipartiteGraph FIGURE D:\n{bipartiteGraph}\n')

#######################################################################
#### AT THIS POINT bipartiteGraph is of the form in FIGURE D above ####
#######################################################################

# Now that our (s-t) Graph with bipartite matching has been constructed and represented
# in a data structure, we can run BFS and Ford-Fulkerson to find max-flow.

# CREDIT: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
 
    def BFS(self, s, t, parent):
        '''
        Returns true if there is a path from source 's' to sink 't' in
        residual graph. Also fills parent[] to store the path
        '''
 
        # Mark all the vertices as not visited
        visited = [False]*(self.ROW)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
         # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
            # Get all adjacent vertices of the dequeued vertex u
            # If an adjacent vertex has not been visited, then mark it
            # as visited and enqueue it
            for idx, val in enumerate(self.graph[u]):
                if visited[idx] == False and val > 0:
                    queue.append(idx)
                    visited[idx] = True
                    # If we find a path from s to t, set it's parent and return true
                    parent[idx] = u
                    if idx == t:
                        return True
 
        # If no path is found from s to t, return false
        return False
             
     
    # Returns the max-flow from s to t in a given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
 
g = Graph(bipartiteGraph)
 
source = 0
sink = (numBoxes*2)-1+2  # -1 because it's 0 indexed, +2 to account for s and t

maxFlow = g.FordFulkerson(source, sink)
minCut = numBoxes - maxFlow
print(minCut)
#print(f'\nNumber of visible boxes: {minCut}')
#print(f'minCut={minCut}, numBoxes={numBoxes}, maxFlow={maxFlow}\n')