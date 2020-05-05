import numpy
from sklearn import metrics

def calculate_distance(x,y):
    d=numpy.sqrt(numpy.sum((x-y)**2))
    return d
def calculate_distance_matrix(x,y):
    d=metrics.pairwise_distances(x,y)
    return d
def cal_B(D):
    (n1,n2)=D.shape
    DD=numpy.square(D)
    Di=numpy.sum(DD,axis=1)/n1
    Dj=numpy.sum(DD,axis=0)/n1
    Dij=numpy.sum(DD)/(n1**2)
    B=numpy.zeros((n1,n1))
    for i in xrange(n1):
        for j in xrange(n2):
            B[i,j]=(Dij+DD[i,j]-Di[i]-Dj[j])/(-2)
    return B
    
 
def MDS(data,n=2):
    D=calculate_distance_matrix(data,data)
    B=cal_B(D)
    Be,Bv=numpy.linalg.eigh(B)
    Be_sort=numpy.argsort(-Be)
    Be=Be[Be_sort]
    Bv=Bv[:,Be_sort]
    Bez=numpy.diag(Be[0:n])
    Bvz=Bv[:,0:n]
    Z=numpy.dot(numpy.sqrt(Bez),Bvz.T).T
    return Z

