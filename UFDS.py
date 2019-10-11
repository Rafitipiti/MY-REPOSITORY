class Subconjunto:
    def __init__(self, padre, rango, num): 
        self.padre = padre 
        self.rango = rango
        self.num = num
# Una función de utilidad para encontrar el conjunto de un nodo 
# (utiliza la técnica de compresión de ruta)
def find(subconjuntos, nodo): 
    if subconjuntos[nodo-1].padre != nodo:
        subconjuntos[nodo-1].padre = find(subconjuntos, subconjuntos[nodo-1].padre) 
    return subconjuntos[nodo-1].padre 
# Una función que hace la unión de dos conjuntos u y v (usa unión por rango)
def union(subconjuntos, u, v):
    # Adjunte un árbol de rango más pequeño debajo de la raíz
    # de árbol de alto rango (Unión por rango)
    if subconjuntos[u-1].rango > subconjuntos[v-1].rango: 
        subconjuntos[v-1].padre = u
    elif subconjuntos[v-1].rango > subconjuntos[u-1].rango: 
        subconjuntos[u-1].padre = v           
    # Si los rangos son iguales, haga uno como
    # root e incrementa su rango en uno
    else: 
        subconjuntos[v-1].padre = u 
        subconjuntos[u-1].rango += 1
def dibujar(arr):
    arreglo = []
    for i in arr:
        arreglo.append(i.num)
    print(arreglo)
    arreglo.clear()
    for i in arr:
        arreglo.append(i.padre)
    print(arreglo)
def buscar(arr,n):
    print("Padre de", n, ":", find(arr,n))

arr = []
for i in range(10):
    sub = Subconjunto(i+1,0,i+1)
    arr.append(sub)

union(arr,3,7)
union(arr,3,9)
union(arr,8,2)
union(arr,3,8)
union(arr,3,4)
union(arr,3,5)
buscar(arr,4)
buscar(arr,2)
buscar(arr,1)
buscar(arr,9)
dibujar(arr)

