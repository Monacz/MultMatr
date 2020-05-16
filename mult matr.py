import time
import numpy as np

def SetRandomMatrix(n,m):
    a=[[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j]=np.random.randint(1,100+1)
    return a


def multiplyMatrix(a,b):
    m,n,q = len(a),len(b),len(b[0])


    
    bt = [[0 for i in range(n)] for j in range(q)]
    for i in range(q):
        for j in range(n):
            bt[i][j] = b[j][i];
    c=[[0 for i in range(q)] for j in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j] += a[i][k] * bt[j][k];
    return c



a=SetRandomMatrix(500,400)
b=SetRandomMatrix(400,600)

ti=time.time();
c1=multiplyMatrix(a,b)
print('Run time of my code: ',time.time()-ti)

ti=time.time();
c2=np.dot(a,b)
print('Run time of numpy: ',time.time()-ti)
