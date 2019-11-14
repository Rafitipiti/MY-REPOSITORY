import time
from random import *
INF = float('inf')

def repe(x,y):
    for i in mat[x]:
        a,b = i
        if(a == y):
            return True
    return False

def crear():
    for i in range(m):
        x = randint(0,n-1)
        y = randint(0,n-1)
        z = randint(1,10)
        while(x == y or repe(x,y)):
            x = randint(0,n-1)
            y = randint(0,n-1)
        mat[x] += [(y,z)]
        mat[y] += [(x,z)]
        
def llenarmatriz():
    for i in range(len(mat)):
        matriz[i][i] = 0
        for j in mat[i]:
            a,b = j
            matriz[i][a] = b

def floydwarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(matriz[i][j] > matriz[i][k] + matriz[k][j]):
                    matriz[i][j] = matriz[i][k] + matriz[k][j]
                     
n,m = [int(i) for i in input().split()]
mat = [[] for i in range(n)]
matriz = [[INF]*n for i in range(n)]
crear()
llenarmatriz()
for i in matriz:
    print(i)
floydwarshall()
for i in matriz:
    print(i)
