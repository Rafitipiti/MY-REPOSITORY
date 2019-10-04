 
def checkdiagonal(mat):
    ard = []
    for i in range(len(mat)):
         for j in range(len(mat)):
             if(mat[i][j] == 1):
                 ard += i,j             
    for i in range(0,len(ard)-3,2):
        x1 = ard[i]
        y1 = ard[i+1]
        for j in range(i+2,len(ard)-1,2):
            x2 = ard[j]
            y2 = ard[j+1]
            if(abs(x1 - x2) == abs(y1 - y2)):
                return False
    return True
    

def valido(arr):
    mat = [[0]*len(arr) for i in range(len(arr))]
    for i in range (len(arr)):
        if(arr[i] != -1):
            mat[arr[i]][i] = 1
    for i in range(len(arr)):
        cont = 0
        cont2 = 0
        for j in range(len(arr)):
            cont += mat[j][i]
            cont2 += mat[i][j]
        if (cont >= 2 or cont2 >= 2):
            return False
    if (checkdiagonal(mat) == False):
        return False
    return True

def pintar(arr):
    mat = [[0]*len(arr) for i in range(len(arr))]
    for i in range (len(arr)):
        if(arr[i] != -1):
            mat[arr[i]][i] = 1
    for i in mat:
        print(i, " ")
    print('\n')

def reinas(i,arr):
    if i < len(arr):
        for k in range (len(arr)):
            arr[i] = k
            if(valido(arr)):
                reinas(i+1,arr)
            arr[i] = -1
    else:
        pintar(arr)
print("Ingresa largo del tablero:")
inn = input()
inn = int(inn)
reinas(0,[-1]*inn)    
