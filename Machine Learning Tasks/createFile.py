import numpy as np
from numpy import asarray
from numpy import savetxt

def checkType(strVal):
    try:
        if type(eval(strVal))==int:
            return "int"
        elif type(eval(strVal))==float:
            return "int"
        else:
            return "str"
    except:
        return "str"


if __name__=="__main__":
    fp=open("adult.data","r")

    line=fp.readline()
    line=line.strip('\n')
    line=line.split(',')
    dataType=[]

    for i in range(0,len(line)):
        dataType.append(checkType(line[i]))

    ###     INITIALIZATION      ###
    ls=[[] for i in range(len(line))]
    cols=[{} for i in range(len(line))]
    fp=open("adult.data","r")
    line=fp.readline()
    cnt=0
    print(line)
    while line!='' and line!=['']:
        line=line.strip('\n')
        line=line.split(',')
        if(line==['']):
            fp.readline()
            continue
        if line[1].strip()=='Never-worked':
            cnt+=1

        for i in range(0,len(line)):
            if dataType[i]=='int' and i!=3:
                if i==0:            #For AGE column with interval 10
                    for j in range(1,11):
                        if(j*10>eval(line[i])):
                            ls[i].append(j)
                            break
                elif i==2:            #For FnlWgt column with interval 10000
                    for j in range(1,201):
                        if(j*10000>eval(line[i])):
                            ls[i].append(j)
                            break
                elif i==10:              #For Cap_Gain col with interval 5000
                    for j in range(1,41):
                        if(j*5000>eval(line[i])):
                            ls[i].append(j)
                            break
                elif i==11:             #For Cap_Loss col with interval 500
                    for j in range(1,41):
                        if(j*500>eval(line[i])):
                            ls[i].append(j)
                            break
                elif i==12:
                    for j in range(1,18):   #For Hrs_Week col with interval 10
                        if(j*10>eval(line[i])):
                            ls[i].append(j)
                            break
                else:
                    ls[i].append(eval(line[i]))
            elif i==3:
                ls[i].append(eval(line[4]))
                if(line[i].strip() in cols[i].values()):
                    None
                else:
                    cols[i][len(cols[i])+1]=line[i].strip()
            else:
                if(line[i].strip=="<=50K"):
                    ls[i].append(1)
                elif(line[i].strip==">50K"):
                    ls[i].append(2)
                elif(line[i].strip() in cols[i].values()):
                    ls[i].append(list(cols[i].values()).index(line[i].strip())+1)
                else:
                    ls[i].append(len(cols[i])+1)
                    cols[i][len(cols[i])+1]=line[i].strip()
        line=fp.readline()
    ls=np.array(ls).T
    ls=np.delete(ls, 3, 1)
    savetxt('createAdultData.csv', ls, delimiter=',',fmt='%d')
