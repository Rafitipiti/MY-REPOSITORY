def dibujar(t):
    print(" ",t[0],t[1],t[2],t[3],"+")
    print(" ",t[4],t[5],t[6],t[1],"+")
    print("---------")
    print(t[4],t[5],t[2],t[1],t[7])


def columnaValida(a,b,x,y,z):
    if x == -1 or y == -1 or z == -1:
        return True
    elif a == -1 or b == -1:
        return z - (x + y) % 10 <= 1
    else:
        return (a+b) // 10 + (x + y) % 10 == z
    

def isLegal(t,i,c):
  t1 = [x for x in t]
  t1[c] = i
  t2 = [x for x in t1 if x != -1]
  if len(set(t2)) < len(t2):
        return False    
  elif -1 in t1:
        if c == 0:            
            return columnaValida(t1[1],t1[5],t1[0],t1[4],t1[5])        
        elif c == 1:
            return columnaValida(t1[2],t1[6],t1[1],t1[5],t1[2]) and columnaValida(t1[3],t1[1],t1[2],t1[6],t1[1])                   
        elif c == 2:
            return columnaValida(t1[2],t1[6],t1[1],t1[5],t1[2]) and columnaValida(t1[3],t1[1],t1[2],t1[6],t1[1])                   
        elif c == 3:
            return columnaValida(0,0,t1[3],t1[1],t1[7])
        elif c == 4:
            if i == 1:
                return True
            else:
                return False
        elif c == 5:
            return columnaValida(t1[1],t1[5],t1[0],t1[4],t1[5]) and columnaValida(t1[2],t1[6],t1[1],t1[5],t1[2])
        elif c == 6:
            return columnaValida(t1[3],t1[1],t1[2],t1[6],t1[1])
        elif c == 7:
            return columnaValida(0,0,t1[3],t1[1],t1[7])        
  else:
    return 1000*(t1[0]+t1[4]) + 100*(t1[1]+t1[5]) + 10*(t1[2]+t1[6]) + (t1[3]+t1[1]) == 10000*t1[4] + 1000*t1[5] + 100*t1[2] + 10*t1[1] + t1[7]
            

def backtracking(c,t):
  if c < len(t):
    for i in range(9,-1,-1):
      if isLegal(t,i,c):
        t[c] = i
        backtracking(c+1,t)
        t[c] = -1
  else:
    dibujar(t)

backtracking(0, [-1]*8)
