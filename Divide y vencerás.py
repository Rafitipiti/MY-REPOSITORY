#########################
#Algoritmo simple

a = [5,7,6,1,3,8,2,9,4,0]
def funcionsimple(a):
    max = a[0]
    for i in a:
        if max < a[i]:
            max = a[i]
    return max
print("El maximo valor del arreglo es: ", funcionsimple(a))

#Divide y vencerás

def divyven(a,i,f):
    if i==f:
        return a[i]
    else:
        mid = (i+f)//2
        auxi = divyven(a, i, mid)
        auxi2 = divyven(a,mid+1,f)
        if auxi > auxi2:
            return auxi
        else:
            return auxi2
print("El maximo valor del arreglo es: ", divyven(a,0,9))

#########################
#Contador de palabras

def leerTexto(nombre):
    f = open(nombre, "r")
    texto = []
    for x in f:
        texto += [x]
    return texto

def contadorDV(texto):
    if len(texto) == 1:
        return len(texto[0].split(" "))
    else:
        m = len(texto) // 2
        i = contadorDV(texto[:m])
        d = contadorDV(texto[m:])
        return i + d
import time
start = time.time()

print("El numero de palabras es", contadorDV(leerTexto("elquijote.txt")))
end = time.time()
print("Tiempo: ", end - start, "sec")

#########################
#QUICK SORT
def pivot(a,i,f):
    izq = i+1
    der = f
    piv = a[i]
    while(der >= izq):
        if(a[izq] <= piv):
            izq = izq+1
        elif (piv <= a[der]):
            der = der -1
        else:
            aux = a[izq]
            a[izq] = a[der]
            a[der] = aux
            der = der -1
            izq = izq+1
    if(der!=i):
        au = a[der]
        a[der] = a[i]
        a[i] = au
    return der

def quick(a,i,f):
    if(f > i):
        piv = pivot(a,i,f)
        quick(a,i,piv-1)
        quick(a,piv+1,f)

def quicksort(a,n):
    quick(a,0,n-1)
   
quicksort(a,10)
print(a)
