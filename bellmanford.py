from random import *

def crearmatriz(matriz,n,m):
    for i in range(m):
        V1 = randint(0,n-1)
        V2 = randint(0,n-1)
        V3 = randint(1,50)
        while(V1==V2 or V2 in matriz[V1]):
            V1 = randint(0,n-1)
            V2 = randint(0,n-1)
        matriz[V1] += [(V2,V3)]
    return matriz

def bellman(matriz,valores):
    for i in range(len(matriz)):
        for j in matriz[i]:
            a,b = j
            if(valores[i] + b < valores[a]):
                valores[a] = valores[i] + b
    
def main():
    n = int(input())
    m = int(input())
    matriz = [[] for i in range (n)]
    matriz = crearmatriz(matriz,n,m)
    valores = []
    for i in range(n):
        valores += [float('inf')]
    valores[0] = 0
    for i in range(n-1):
        bellman(matriz,valores)
    print(valores)
main()
