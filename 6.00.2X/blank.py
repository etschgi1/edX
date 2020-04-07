from Lect3ex2 import*
g = Digraph()
for n in nodes:
    nn = n.getName()
    for e in nodes:
        ee = e.getName()
        if (ee[0] == nn[0] or ee[2] == nn[2]) and ee[1] != nn[1]:
            if e not in g.childrenOf(n):  # this line (6)
                g.addEdge(Edge(n, e))
