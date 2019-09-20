from random import *


n = 3
m = 5

#################### GENERO LAS RELACIONES DE MI GRAFO ##########################

matriz = [[] for i in range(n)]
 
def crearmatriz(mat, n, m):
    for j in range (m):
        v1 = randint(0, n - 1)
        v2 = randint(0, n - 1)
        while(v2 in matriz[v1] or v2 == v1):
            v1 = randint(0, n - 1)
            v2 = randint(0, n - 1)
        matriz[v1] += [v2]
    return matriz
           
print(crearmatriz(matriz, n, m))
       
###################### MUESTRO RELACIONES ############################

def listaaristas(t):
    t1 = []
    for i in range (len(t)):
        for j in t[i]:
            t1 += [(i,j)]
    return t1
           
print(listaaristas(matriz))
