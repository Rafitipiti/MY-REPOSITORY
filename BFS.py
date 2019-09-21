def BFS(g,s):
    visitado = [False] * (len(g))
    cola = []
    cola.append((s,0))
    visitado[s] = True
    t = []
    while cola:
        while cola:
            s = cola.pop(0)
            print(s[0], end = " ")
            for x in g[s[0]]:
                if visitado[x[0]] == False:
                    t += [(s[0],x[0],x[1])]
                    cola.append(x)
                    visitado[x[0]] = True
        if False in visitado:
            s = visitado.index(False)
            visitado[s] = True
            cola.append((s,0))
    return t
