from random import *
import heapq as pq
import time

START = time.time()
END = time.time()
INF = float('inf')
n = 0
m = 0


def generar(n,m,mat):
    for i in range(m):
        x = randint(0,n-1)
        y = randint(0,n-1)
        z = randint(-5,10)
        while(x == y or z == 0):
            x = randint(0,n-1)
            y = randint(0,n-1)
            z = randint(-5,10)
        if(mat[x][y]==INF): mat[x][y] = z
        else:
            mat[x][y] += z

def bellman(n,m,mat,valores):
    for i in range(n):
        for j in range(n):
            if(mat[i][j] != 0):
                b = mat[i][j]
                if(b+valores[i] < valores[j]):
                    valores[j] = valores[i] + b


def dijkstra(n,m,G,s):
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
            for j in range(n):
                if(G[u][j] != INF and G[u][j] != 0):
                    v = j
                    w = G[u][j]
                    if not visitado[v]:
                        f = g + w
                        if f < costo[v]:
                            costo[v] = f
                            recorrido[v] = u
                            pq.heappush(cola, (f, v))
    print(recorrido)

def johnson(n,m,mat,valores):
    for i in range(n):
        print(mat[i])
    bellman(n,m,mat,valores)
    print("-------")
    print(valores)
    for i in range(n):
        dijkstra(n,m,mat,0)

def main():
    n = int(input())
    m = int(input())
    mat = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(mat[i][j] == 0):
                mat[i][j] = INF
    for i in range(n):
        mat[i][i] = 0
    valores = [float('inf')]*n
    valores[0] = 0
    generar(n,m,mat)
    johnson(n,m,mat,valores)

main()
