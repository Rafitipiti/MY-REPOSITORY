import math
def f(d,p,C,S):
    if p <= 0:
        C[0] = 0
        return
    f(d,p-1,C,S)
    conteo = math.inf
    moneda = 0
    for di in d:
        if di <= p:
            if C[p-di] < conteo:
                conteo = C[p-di]
                moneda = di        
    C[p] = conteo + 1
    S[p] = moneda
        
def monedas(d, n):
    C = [-1] * (n + 1)
    S = [0] * (n + 1)
    f(d,n,C,S)
    return C, S
monto = 19
c, s = monedas([1, 5, 10, 20, 25, 50], monto)
print(c)
print(s)
contar = [0] * (monto + 1)
while monto > 0:
    print(s[monto],monto)
    contar[s[monto]] += 1
    monto -= s[monto]
