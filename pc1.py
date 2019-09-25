
#divide y venceras



#backtracking
def mostrar(arr):
    print(arr)

def islegal(arr,i,c):
    if(i > 0):
        print(i)

def backtrack(arr,i,c):
    if c < len(arr):
        for i in range(len(arr),-1,-1):
            if(islegal(arr,i,c)):
                arr[c]=i
                backtrack(arr,i,c+1)
                arr[c]=-1
    else:
        mostrar(arr)

#fuerza bruta

def mostrar(elem, arrp):
    conte = 0
    contp = 0    
    arrf = []
    for i in range(len(arrp)):
        if(i%2 == 0):
            for i in range(arrp[i]):
                arrf.append(elem[conte])
                conte = conte + 1            
        else:
            if(contp != 3):
                arrf.append(".")
                contp = contp - 1

    if(arrf[len(arrf)-1] != "."):
        for i in arrf:
            print(i, end = "")
        print('\n')

def check(arrp):
    conta = 0
    for i in range (len(arrp)-1):
        if(arrp[i] == "."):
            conta = conta +1
        if(arrp[i] == "." and arrp[i+1] == "."):
            return False
    if(conta == 3):
        return True
    else:
        return False

def insert(elem, arrp):
    auxi = 0
    for i in range (len(arrp)):
        if(arrp[i] != "."):
            arrp[i] = elem[auxi]
            auxi = auxi + 1
    print(arrp)
    print('\n')
   
def otrafun(elem):
    tamato = len(elem) + 3
    arrp = [0]*tamato
    ini = 1
    fin = tamato - 2
    cont = 3
    arrp[0]=elem[0]
    arrp[len(arrp)-1] = elem[len(elem)-1]
    for i in range (ini, fin-1):
        arrp[i] = "."     
        for j in range(i+2, fin):
            arrp[j] = "."
            for k in range(j+2, fin+1):
                arrp[k] = "."
                if (check(arrp)):
                    insert(elem,arrp)
                arrp[k] = 0
            arrp[j] = 0
        arrp[i] = 0
    

    
def generarIP(elem):
    if(len(elem) < 4):
        return False
    else:
        arr = []
        cont = 3
        arrp = [1]*7
        arrp[len(arrp)-1] = arrp[len(arrp)-1] + (len(elem)-4)
        arrf = mostrar(elem, arrp)
        
        for i in range(3,0,-1):
            aux = arrp[i*2]
            arrp[i*2] = arrp[(i*2)-2]
            arrp[(i*2)-2] = aux
            arrf = mostrar(elem, arrp)

def main():
    conti = 0
    archivo = open("archivo.txt",'r')
    for line in archivo:
        if (conti == 0):
            casos = line[0]
            print(casos)
            conti = conti + 1
        else:
            elem = line 
            generarIP(elem)
            otrafun("1111")
    
   # for i in range(casos):
     #   elem = "1111"
     #   generarIP(elem)
    #archivo1 = write("archivo1.txt",'w')
    
main()


#matriz = [int (i) for i in input().split()]
#print(elem, end = '\n')
#len(elem)
