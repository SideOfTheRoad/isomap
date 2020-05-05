
import numpy

def floyd(D,n_neighbors=15):
    Max=numpy.max(D)*1000
    n1,n2=D.shape
    k=n_neighbors
    D1=numpy.ones((n1,n1))*Max
    D_arg=numpy.argsort(D,axis=1)
    for i in range(n1):
        D1[i,D_arg[i,0:k+1]]=D[i,D_arg[i,0:k+1]]
    for k in xrange(n1):
        for i in xrange(n1):
            for j in xrange(n1):
                if D1[i,k]+D1[k,j]<D1[i,j]:
                    D1[i,j]=D1[i,k]+D1[k,j]
    return D1
