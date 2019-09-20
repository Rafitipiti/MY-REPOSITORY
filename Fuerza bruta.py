######################

#EJERCICIO 1
arr = [7,5,4,6,8,2,9]
n = 7
for i in range(n-1):
    sorted = True
    for j in range (n-1-i):
        if(arr[j] > arr[j+1]):
            sorted = False
            aux = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = aux

    if(sorted):
        break
print(arr)
   
######################

#EJERCICIO 2

from math import *

ve = float(input())
def polinomio(ve,arr):
    pila = 0
    for i in range (len(arr)):
        pila += arr[i]*(pow(ve,len(arr)-i-1))
    return pila

print(polinomio(ve,arr))

######################

#EJERCICIO 3

def sumador():
    m = 1
    for s in range (9,0,-1):
        for e in range (0,10):
            for n in range (0,10):
                for d in range (0,10):
                    for o in range (0,10):
                        for r in range (0,10):
                            for y in range (0,10):
                                v = [s,e,n,d,m,o,r,y]
                                sumando1 = s*1000 + e*100 + n*10 + d
                                sumando2 = m*1000 + o*100 + r*10 + e
                                suma = m*10000 + o*1000 + n*100 + e*10 + y
                                if len(v) == len(set(v))and suma == sumando1 + sumando2:                                  
                                    return v
arreglo = sumador()
print("S= ", arreglo[0])
print("E= ", arreglo[1])
print("N= ", arreglo[2])
print("D= ", arreglo[3])
print("M= ", arreglo[4])
print("O= ", arreglo[5])
print("R= ", arreglo[6])
print("Y= ", arreglo[7]) 
