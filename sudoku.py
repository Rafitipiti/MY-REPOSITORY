#EJERCICIO 1

import random

#######################
arr = []

def generar(n):
    for i in range(n):
        n = random.randrange(100)
        arr.append(n)
    return arr

print("\n",generar(25))

#######################

def mostrar(n):
    for x in n:
        print(x, end=" ")
       
mostrar(arr)

#######################
       
def reverse(n):
    aux = 0
    for i in range(len(n)//2):
      aux = n[i]
      n[i] = n[len(n)-i-1]
      n[len(n)-i-1] = aux

reverse(arr)
print("\n",arr)
   
#######################

def minelem(n):
    aux = arr[0]
    for i in range (len(n)):
        if(n[i] < aux):
            aux = n[i]
    print("MIN ELEM: ", aux)

minelem(arr)

#######################

def media(n):
    aux = 0
    for i in range (len(n)):
        aux = aux + arr[i]
    aux = aux / len(n)
    print("Media Aritmetica: ", aux)

media(arr)

#######################

def ocurrencias(n):
    arr2 = [0]*(100) #INICIALIZO EN 0
    for i in n:
        arr2[i] = arr2[i]+1
    return arr2
print(ocurrencias(arr))

#######################

#EJERCICIO 2

ar = [None]*100
for i in range (len(ar)):
    ar[i] = i
print(ar)

#######################

#EJERCICIO 3.- SUDOKU!!!

matriz = [[0]*9 for i in range (9)]

for i in matriz:
    print(i)
   
def verificarbloque(b):
    return len(set(b)) == len(b)

def funciona(m):
    for i in range (9):
        for k in range (9):
            fil = m[i][k]
            col = m[k][i]
            for j in range (k+1,10):
                axf = m[i][j]
                axc = m[j][i]
                if(fil == axf or col == axc):
                    print("FALSO")
                    return False
    cont1 = 0
    cont2 = 0
    for k in range (9):
        arreglito = [None]*9
        for i in range (3):            
            for j in range (3):
                 arreglito.append(m[i+3*cont][j+3*cont2])
        if(cont1 != 3):
            cont1 = cont1+1
        else:
            cont2 = cont2+1
            cont1 = 0
        if (verificarbloque(arreglito) == False):
            print("NO SE CUMPLE")
    print("SE CUMPLE")
