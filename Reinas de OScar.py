#reinas

n = 8
t = [-1]*n #posicion = fila, valor = columna
opciones = []

def isLegal(t, c, f):
    for i in range(f):
        if t[i] == c: return False
        if abs(f-i) == abs(c-t[i]): return False
    return True
        
def reinasBT(t, f):
    if f<n:
        for i in range(n):
            if isLegal(t, i, f):
                t[f] = i
                reinasBT(t, f+1)
                t[f] = -1
    else:
        print(t)
        
reinasBT(t, 0)

for i in opciones:
    print(i)
                
        
