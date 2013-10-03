#!/usr/bin/env python

class Node(object):

    def __init__(self, name):
        self.name = name 
        self.neighbours = []
        self.distances = []
        self.visited = False
        self.distance = float("inf")
        self.previous = ''

    def join(self, nodename, d):
        self.neighbours.append(nodename)
        self.distances.append(d)

    def unjoin(self, nodename):
        index = self.neighbours.index(nodename)
        self.neighbours.remove(nodename)
        self.distances.pop(index)

    def get_neigh_unvisited(self):
        return [(node, distance) for node, distance in zip(self.neighbours, self.distances) if node.visited == False]

    def dijkstra(self):

        self.visited=True

        n_nodes = self.get_neigh_unvisited()
        neighbours = sorted(n_nodes, key=lambda distance: distance[1]) 

        if not neighbours:
           return

        for node, distance in neighbours:

            if (self.distance + distance) < node.distance:
                node.distance = self.distance+distance
                node.previous = self 
                node.dijkstra()

                            



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.join(b, 16)
a.join(c, 9)
a.join(d, 35)

b.join(a, 16)
b.join(d, 12)
b.join(e, 25)

c.join(a, 9)
c.join(d, 15)
c.join(f, 22)

d.join(a, 35)
d.join(b, 12)
d.join(c, 15)
d.join(e, 14)
d.join(f, 17)
d.join(g, 19)

e.join(b, 25)
e.join(d, 14)
e.join(g, 8)

f.join(c, 22)
f.join(d, 17)
f.join(g, 14)

g.join(d, 19)
g.join(e, 8)
g.join(f, 14)

def dijkstra(start):

    start.distance = 0 
    start.dijkstra()
    
