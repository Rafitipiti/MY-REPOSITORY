from random import *
archivo = open("archivo.txt", "r")
l = archivo.readline()
l.rstrip()
cnt = int(l)
mat = [[] for i in range (cnt)]
for i in range (cnt):
    mat[i] += [int(j) for j in archivo.readline().split()]
archivo.close()
print("Matriz:",mat)
n = 4
m = 8

def relaciones(mat):
    t = []
    for i in range (len(mat)):
        for j in mat[i]:
            t += [(i,j)]
    return t
print ("Relaciones:", relaciones(mat))

global vis, ds
vis = [0]*cnt
ds = []


def dfs(nod):
    global vis, ds
    if not (vis[nod] == 1):
        ds += [nod]
        vis[nod] = 1
    for i in mat[nod]:
        if not (vis[i] == 1):
            vis[i] = 1
            ds += [i]
            dfs(i) 
dfs(1)
print("DFS:", ds)

vis = [0]*cnt
rec = [0]*cnt
ds = []

def bfs(nod):
    global vis, ds
    if not (vis[nod] == 1):
        ds += [nod]
        vis[nod] = 1
        rec[nod] = 1
    for i in mat[nod]:
        if not (vis[i] == 1):
            vis[i] = 1
            ds += [i]
    for i in mat[nod]:
        if not (rec[i] == 1):
            rec[i] = 1
            bfs(i)
bfs(2)
print("BFS:", ds)
