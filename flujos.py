import math
inf = float('inf')

n, m = [int(j) for j in input().split()]
vs = [[] for j in range(n)]
cap = [[0 for j in range(n)] for i in range(n)]
for i in range(m):
    x, y, w = [int(j) for j in input().split()]
    vs[x].append(y)
    vs[y].append(x)
    cap[x][y] = w
    cap[y][x] = w

for i in vs:
    print(i)

def bfs(s,t):
    parent = [-1]*n
    parent[s] = -2
    q = []
    q.append((s,inf))
    while(len(q)):
        v,f = q.pop(0)
        for x in vs[v]:
            if(cap[v][x] > 0 and parent[x] == -1):
                parent[x] = v
                if(t == x): return min(cap[v][x],f), parent
                q.append((x,min(cap[v][x],f)))
    return 0,parent

def flujomax(s,t):
    maxf = 0
    nf,parent = bfs(s,t)
    while nf > 0:
        v = t
        maxf += nf
        while v != s:
            u = parent[v]
            cap[u][v] -= nf
            cap[v][u] += nf
            v = u
        nf,parent = bfs(s,t)
    return maxf

print(flujomax(0,n-1))
            
