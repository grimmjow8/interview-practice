#! /usr/bin/python
# http://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph

# program to print BFS traversal from given source vertex.
# BFS(s) traverses vertices reachable from s.

import json
import logging
from collections import defaultdict

LOG = logging.getLogger("BFS")
formatter = logging.Formatter('>>> %(message)s')
#formatter = logging.Formatter('%(asctime)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
LOG.addHandler(handler)
LOG.setLevel(logging.INFO)

# class represents directed graph using adjacency list representation
class Graph:
    def __init__(self):
        LOG.info("init graph")
        self.graph = defaultdict(list)

    # add edge to graph
    def addEdge(self, u, v):
        LOG.info("addEdge " + str(u) + " : " + str(v))
        self.graph[u].append(v)

   # print BFS of graph
    def BFS(self, s):
        LOG.info("performing BFS")
        LOG.info(json.dumps(self.graph))

        # init, all vertices as not visited
        v = [False]*(len(self.graph))
        LOG.info("graph len: " + str(len(v)))

        # processing queue
        q = []

        # mark src node as visited
        q.append(s)
        v[s] = True

        # iterate until queue is empty
        # best/worst case: n
        while q:
            # dequeue vertex, display
            s = q.pop(0)
            print s,

            # add all non-visited adjacent vertices to queue
            # worst case. each node connected to all others: n
            for i in self.graph[s]:
               if v[i] == False:
                  LOG.info("node visited FALSE: " + str(i) + " parent: " + str(s))
                  q.append(i)
                  v[i] = True
               else:
                  LOG.info("node visited TRUE:  " + str(i) + " parent: " + str(s))
   

# main
# overall: n*n = n^2
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

#  representation attempt
#
#      0 - 1
#      | /
#      2 - 3
#

print "breadth first traversal from vertex 2"
g.BFS(2)
