global t
t = []
def DFSUtil(g,s,visitado):
    visitado[s[0]]= True
    print(s[0], end = " ")
    global t
    for x in g[s[0]]:
        if visitado[x[0]] == False:
            t += [(s[0],x[0],x[1])]
            DFSUtil(g, x, visitado) 
            
def DFS(g,s):
    visitado = [False]*(len(g))
    while False in visitado:
        global t
        DFSUtil(g,(s,0),visitado)
        if False in visitado:
            s = visitado.index(False)
            visitado[s] = True
    return t
