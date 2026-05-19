class Graph:
    def __init__(self):
        self.__adjacency = {}   # dizionario privato — chiave: nodo, valore: lista vicini

    def addNode(self, node):
        if node not in self.__adjacency:
            self.__adjacency[node] = []   # nuovo nodo — lista vicini vuota

    def addEdge(self, node1, node2):
        # aggiungiamo i nodi se non esistono già
        self.addNode(node1)
        self.addNode(node2)

        # grafo non orientato — l'arco vale in entrambe le direzioni
        self.__adjacency[node1].append(node2)
        self.__adjacency[node2].append(node1)

    def getNeighbors(self, node):
        if node not in self.__adjacency:
            raise ValueError(f"{node} non trovato nel grafo")
        return self.__adjacency[node]

    def hasEdge(self, node1, node2):
        if node1 not in self.__adjacency:
            return False
        return node2 in self.__adjacency[node1]

    def getNodes(self):
        return list(self.__adjacency.keys())
    
    def isEmpty(self):
        return len(self.__adjacency) == 0

    def __repr__(self):
        lines = []
        for node, neighbors in self.__adjacency.items():
            lines.append(f"  {node}: {neighbors}")
        return "Graph (undirected):\n" + "\n".join(lines)
    
g = Graph()

g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(3, 4)

print(g)
# Graph (undirected):
#   1: [2, 3]
#   2: [1, 4]
#   3: [1, 4]
#   4: [2, 3]

print(g.getNeighbors(1))   # [2, 3]
print(g.hasEdge(1, 2))     # True
print(g.hasEdge(1, 4))     # False
print(g.getNodes())        # [1, 2, 3, 4]


