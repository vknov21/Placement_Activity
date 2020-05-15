import numpy as np
from numpy import genfromtxt
from numpy import savetxt
from numpy import linalg as LA

def corrModify():
    my_data=genfromtxt('createAdultData.csv',delimiter=',').T
    corr,mat=[],[]
    #Formula for correlation is
    #       r = {  n(ΣXY) - (ΣX)(ΣY)  }/{[n(ΣX^2)-(ΣX)^2][n(ΣY^2)-(ΣY)^2]}
    for i in range(0,my_data.shape[0]):
        corr=[]
        for j in range(0,my_data.shape[0]):
            sumXY = (my_data[i]*my_data[j]).sum()
            sumX2 = (my_data[i]**2).sum()
            sumX = my_data[i].sum()
            sumY2 = (my_data[j]**2).sum()
            sumY = my_data[j].sum()
            r=(my_data.shape[1]*sumXY - sumX*sumY)/(((my_data.shape[1]*sumX2-sumX**2)*(my_data.shape[1]*sumY2-sumY**2))**(1/2))
            col=[]
            corr.append(r)
        mat.append(corr)

    for i in range(0,len(my_data)):
        my_data[i]=my_data[i]-my_data[i].sum()/my_data.shape[1]

    mat=np.array(mat)
    w,v = LA.eig(np.array(mat))
    v=v.tolist()
    p=[]
    for i in range(0,len(w)):
        p.append((w[i],v[i]))
        print(p[i])
    p.sort(reverse=True)
    w=[]
    for i in range(0,len(p)):
        w.append(p[i][1])
    w=np.array(w)
    print(w)

    print(np.matmul(w,my_data))

    #for i in range(0,len(w)):


    savetxt('createAdultPCAData.csv', np.matmul(w,my_data).T, delimiter=',',fmt='%f')

if __name__=="__main__":
    corrModify()
