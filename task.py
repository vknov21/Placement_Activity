import numpy as np
from numpy import genfromtxt
from numpy import savetxt

def corrModify():
    my_data=genfromtxt('createAdultData.csv',delimiter=',').T
    corr=[]
    #Formula for correlation is
    #       r = {  n(ΣXY) - (ΣX)(ΣY)  }/{[n(ΣX^2)-(ΣX)^2][n(ΣY^2)-(ΣY)^2]}
    for i in range(0,my_data.shape[0]-1):
        sumXY = (my_data[i]*my_data[-1]).sum()
        sumX2 = (my_data[i]**2).sum()
        sumX = my_data[i].sum()
        sumY2 = (my_data[-1]**2).sum()
        sumY = my_data[-1].sum()
        r=(my_data.shape[1]*sumXY - sumX*sumY)/(((my_data.shape[1]*sumX2-sumX**2)*(my_data.shape[1]*sumY2-sumY**2))**(1/2))
        col=[]
        corr.append(r)
    print(corr)
    for i in range(0,len(corr)):
        if abs(corr[i])<0.1:
            col.append(i)
    col.reverse()
    print(col)
    my_data=my_data.T
    for i in range(0,len(col)):
        my_data=np.delete(my_data, col[i], 1)
    print(len(corr))
    savetxt('createAdultCorrData.csv', my_data, delimiter=',',fmt='%d')

    my_data=genfromtxt('createAdultTest.csv',delimiter=',')
    for i in range(0,len(col)):
        my_data=np.delete(my_data, col[i], 1)
    print(len(corr))
    savetxt('createAdultCorrTest.csv', my_data, delimiter=',',fmt='%d')

def test(givenData, testData, ProbY):
    mul=1
    sum=0
    for i in range(0, len(testData)):
        mul=mul*(givenData[i].count(testData[i])/len(givenData[i]))
        sum=sum+(givenData[i].count(testData[i])/len(givenData[i]))
    mul=mul*ProbY
    return mul/sum

if __name__=="__main__":
    ###     Read Adult Data given       ####
    corrModify()
    fpCr=open("createAdultCorrData.csv","r")
    totVal=[]
    line=fpCr.readline()
    val=[]

    while line!='' and line!=['']:
        line=line.strip('\n')
        line=line.split(',')
        if(line==['']):
            fpCr.readline()
            continue
        for i in range(0,len(line)):
            val.append(eval(line[i]))
        totVal.append(val)
        line=fpCr.readline()
        val=[]
    totVal = np.array(totVal)
    totVal_Less_50 = np.array(list(totVal[i] for i in range(len(totVal)) if totVal[i,-1]==1)).T           #For Y<=50
    totVal_Big_50 = np.array(list(totVal[i] for i in range(len(totVal)) if totVal[i,-1]==2)).T              #For Y>50
    totVal=totVal.T

    print(totVal_Big_50.shape)
    ###     Read Testing Data       ###
    fpTst=open("createAdultCorrTest.csv","r")
    totValTst=[]
    line=fpTst.readline()
    val=[]

    while line!='' and line!=['']:
        line=line.strip('\n')
        line=line.split(',')
        if(line==['']):
            fpTst.readline()
            continue
        for i in range(0,len(line)):
            val.append(eval(line[i]))
        totValTst.append(val)
        line=fpTst.readline()
        val=[]
    totValTst = np.array(totValTst)

    print(totValTst[0,:-1])

    testRes=[totValTst.T[-1],[]]
    print(testRes)

    for i in range(totValTst.shape[0]):
        Prob_X_given_Y_1 = test(np.ndarray.tolist(totVal_Less_50), totValTst[i,:-1], len(totVal_Less_50)/len(totVal))
        Prob_X_given_Y_2 = test(np.ndarray.tolist(totVal_Big_50), totValTst[i,:-1], len(totVal_Big_50)/len(totVal))
        if(Prob_X_given_Y_1>Prob_X_given_Y_2):
            testRes[1].append(1)
        elif(Prob_X_given_Y_1==Prob_X_given_Y_2):
            testRes[1].append(0)
        else:
            testRes[1].append(2)
        print(i,totValTst.shape[0]),
    k=len(testRes[0])
#    totVal_Less_50 = np.array(list(totVal[i] for i in range(len(totVal)) if totVal[i,-1]==1)).T
    #print(len(testRes[0]), len(testRes[1]))
    p=len(list([i] for i in range(len(testRes[0])) if testRes[1][i]==testRes[0][i]))

    print('Success rate : ', p/len(testRes[0])*100)
