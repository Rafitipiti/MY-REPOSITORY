from random import *

import time


start = time.time()
print("Ingrese cantidad de nodos:")
nodos = int(input())
print("Ingrese cantidad de relaciones:")
relaciones = int(input())
while(relaciones > (nodos*(nodos-1))//2):
    print("Seas mamon:")
    relaciones = int(input())

matriz = [[] for i in range(nodos)]

def existe(matriz, n1,n2):
    for i in matriz[n1]:
        a,b = i
        if(a == n2):
            return True
    return False
        
def crearmatriz(matriz,n,m):
    for i in range(m):
        n1 = randint(0,n-1)
        n2 = randint(0,n-1)
        n3 = randint(1,10)
        while(n2 == n1 or existe(matriz,n1,n2)):
            n1 = randint(0,n-1)
            n2 = randint(0,n-1)
        matriz[n1] += [(n2,n3)]
        matriz[n2] += [(n1,n3)]
    return matriz

print("Relaciones:",crearmatriz(matriz,nodos,relaciones))

arr = [0]*nodos
suma = 0

global recorrido
recorrido = []

def MSTPRIM(act,arr,suma,matriz):
    global recorrido
    arr[act] = 1
    mn = 9999
    elem = 9999
    for i in range(len(arr)):
        if arr[i] == 1:
            for j in matriz[i]:
                a,b = j
                if(b < mn and arr[a] == 0):
                    elem = a
                    mn = b
                    prov = i
    if (elem == 9999) : return suma
    recorrido += [(prov,elem)]
    suma += mn
    return MSTPRIM(elem,arr,suma,matriz)

def detectarciclos(rec,a,b,nodos):
    #union-find
    return False
        

def kruskal(nodos,arror,arr,suma):
    cont = 0
    recorrido = []
    i = 0
    while(cont != nodos-1):
        a,b,c = arror[i]
        recaux = recorrido
        recaux += [(a,b)]
        if not (detectarciclos(recaux,a,b,nodos)):
            recorrido += [(a,b,c)]
            suma += c
    return (recorrido,suma)

def ORDENAARISTAS(nodos,arr,suma,matriz):
    arror = []
    for i in range(nodos):
        for j in matriz[i]:
            a,b = j
            arror.append([i,a,b])
    arror.sort(key = lambda x:x[2])
    print("RELACIONES ORDENADAS:", arror)
    return kruskal(nodos,arror,arr,suma)

print("Ingrese elemento para comenzar búsquedas")
elemen = int(input())
while(elemen > nodos-1):
    print("Seas mamon:")
    elemen = int(input())
recorrido += [(elemen,elemen)]
print("PRIM:", MSTPRIM(elemen,arr,suma,matriz))
print("Recorrido:", recorrido)
end = time.time()
arr = [0]*nodos
suma = 0
kra,krb = ORDENAARISTAS(nodos,arr,suma,matriz)
print("KRUSKAL:", krb)
print("Recorrido", kra)
print("Tiempo:", end - start)
