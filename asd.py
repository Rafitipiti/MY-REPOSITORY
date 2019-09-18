

def topo(arr, wa, visited, topu):
    visited[wa] = True
    for a in arr[wa]:
        if (not visited[a]):
            topo(arr, a, visited, topu)
    topu.append(wa+1)

def main():
    a,b = [int(i) for i in input().split()]
    arr = [[] for i in range (a)]
    topu = []
    visited = [False]*a
    for i in range (0,b):
        x,y = [int(i) for i in input().split()]
        x -= 1
        y -= 1
        arr[x].append(y)
    topo(arr,0, visited, topu)
    topu.reverse()
    print(topu)
    
main()
