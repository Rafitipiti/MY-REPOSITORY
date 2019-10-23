
def fibo(n, C):
    if(n < 2):
        C[0] = 1
        C[1] = 1 
    else:
       fibo(n-1,C)
       C[n] = C[n-1] + C[n-2]

def fibodp(n):
    C = [0]*(n+1)
    fibo(n,C)
    return C[n]


def main():
    n = 100
    print(fibodp(n))
    
main()
