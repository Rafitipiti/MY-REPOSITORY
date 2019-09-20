###########################################################################################
#############################    DOS FORMAS DE APLICAR UCS    #############################
###########################################################################################

from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node + to_node)]
   
def ucs(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost, i))

###########################################################################################

import heapq as pq
INF = float('inf')
def UCS(G,s,e):
    n = len(G)
    visitado = [False] * n
    costo = [INF] * n
    recorrido = [None] * n
    cola = []
    pq.heappush(cola, (0,s))
    costo[s] = 0
    while cola:
        g, u = pq.heappop(cola)
        if not visitado[u]:
            visitado[u] = True
            if u == e:
                break
            for v, w in G[u]:
                if not visitado[v]:
                    f = g + w
                    if f < costo[v]:
                        costo[v] = f
                        recorrido[v] = u
                        pq.heappush(cola, (f, v))
    return recorrido, costo
