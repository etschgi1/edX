"""
Created on Tue Jul 12 15:04:56 2016

@author: guttag
"""


class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class WeightedEdge(Edge):
    '''Same as edge but with weight attribute'''

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        return str(self.weight)

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() +\
            ' ('+self.getWeight()+')'


class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                    + dest.getName() + '\n'
            result += ("-------------\n")
        return result[:-1]  # omit final newline


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))

g = Graph()  # create obj: Graph g
for n in nodes:
    g.addNode(n)  # add each Node to the graph
# Node solution code


def getallpaths(nodes):
    '''adds all edges to the graph, note that graph is a dict mapping 
    key(node) to val(childrennodes) therefor an edge is a key val pair
    '''
    # Logic first or last element are equal, middle are not equal
    for n in nodes:  # iterate over each node
        node = n.getName()  # get its name
        for p in nodes:  # once again to compair to all other nodes
            pnode = p.getName()
            # compare if one node using above logic
            if node[0] == pnode[0] or node[2] == pnode[2] and \
                    node[1] != pnode[1]:
                # check for same node case, or node already added case
                if p not in g.childrenOf(n) and p != n:
                    # g is the graph obj on which
                    g.addEdge(WeightedEdge(n, p, 5))

                    # the funct addEdge is performed, this funct takes
                    # origen and destination node and stores it in the dict as
                    # key-val pair
getallpaths(nodes)

print(g)
