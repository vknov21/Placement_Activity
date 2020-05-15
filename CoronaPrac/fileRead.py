import numpy as np
import datetime
from numpy import genfromtxt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model

def find(name, ctr_dict):
    ctr=[]
    if len(name)>3:
        name=name[:3]
    i=len(name)
    data={}
    while i>0:
        for j in range(len(ctr_dict)):
            if(name[:i]==list(ctr_dict.keys())[j][:i]):
                data[list(ctr_dict.keys())[j]]=''
        if(len(data)>0):
            break
        i-=1
    print(list(data.keys()))
    if(len(data)==1):
        return list(data.keys())[0]
    elif(len(data)>0):
        print("Choose any of them : ")
        for i in range(len(data)):
            print('  ',i,' : ',list(data.keys())[i])
        ent=int(input("Enter number corresponding to name : "))
        return list(data.keys())[ent]
    else:
        print("No result!")
        exit()

def main(fileName):
    fp=open(fileName,'r')
    my_data=fp.readlines()
    #my_data=my_data.split('\n')
    for i in range(len(my_data)):                   #Creating data in array format of rows and cols
        my_data[i]=my_data[i].strip('\n')
        my_data[i]=my_data[i].split(',')

    for i in range(len(my_data)):               #if the size exceeds the req ',' has been used from name of country #Correction
        while(len(my_data[i])>len(my_data[0])):
            my_data[i][0]=' '.join((my_data[i][0],my_data[i][1]))
            del my_data[i][1]

    for i in range(4,len(my_data[0])):          #Getting no. of date cols
        if(my_data[0][i][-2:]!='20'):
            break
    size=i
    for i in range(len(my_data)):               #Removing all unnnecessaries
        del my_data[i][size+1:]
        del my_data[i][0:4]

    #separating country code and date
    my_data=np.array(my_data)
    my_data=np.delete(my_data,1,0)
    my_data[0][-1]='COUNTRY+CODE'
    dte=my_data[0][0:-1]
    date_dict={}
    for i in range(len(dte)):       #Dictionary of Date being unique
        date_dict[i]=dte[i]
    my_data=np.delete(my_data,0,0)
    size=my_data.shape[0]-1
    i=0

    while i<my_data.shape[0]:
        if(my_data[i][-1] in ('','MAC','HKG','CHN')):       #Removing all without code and China
            my_data=np.delete(my_data,i,0)
            size=size-1
            #if(i>=size):
        i+=1
        #print(i, size, end='\t')
    #my_data=my_data.T
    ctr_dict={}
    for i in range(my_data.shape[0]):
        ctr_dict[my_data[i][-1]]=np.array([0]*len(date_dict))
    country=my_data[:,-1]
    my_data=np.delete(my_data,-1,-1)
    print(my_data.shape)
    my_data=my_data.astype(np.int)
    for i in range(my_data.shape[0]):
        ctr_dict[country[i]]=ctr_dict[country[i]]+my_data[i]
    country=list(ctr_dict.keys())

    for i in range(len(ctr_dict)):
        if ctr_dict[country[i]][-1]<=100:
            ctr_dict.pop(country[i])

    country=list(ctr_dict.keys())
    world=[0]*len(ctr_dict[country[0]])

    np.array(world)
    for i in range(len(ctr_dict)):
        world=world+ctr_dict[country[i]]
    ctr_dict['WORLD']=world
    date1='22/01/20'
    start=datetime.datetime.strptime(date1,'%d/%m/%y')

    k=input("Enter country name (Initials, eg. IND for India) : ")
    name=find(k.upper(),ctr_dict)

    p=input("Predicting date (dd/mm/yy) (0 if not) : ")
    if(len(p)<2 or p[2]!='/' or p[5]!='/'):
        p=0
    else:
        start=datetime.datetime.strptime(date1,'%d/%m/%y')
        end=datetime.datetime.strptime(p,'%d/%m/%y')
        p=(end-start).days

    draw_graph(name.upper(),ctr_dict[name.upper()],p)


def draw_graph(name,ctr_dict,pred):
    Y=np.array(list(ctr_dict))
    X=np.array(list(range(1,len(ctr_dict)+1)))

    X = X[:,np.newaxis]
    Y = Y[:,np.newaxis]

    plt.scatter(X,Y)

    nb_degree = 10
    polynomial_features = PolynomialFeatures(degree = nb_degree)
    X_TRANSF = polynomial_features.fit_transform(X)

    model = LinearRegression()
    model.fit(X_TRANSF, Y)

    Y_NEW = model.predict(X_TRANSF)

    rmse = np.sqrt(mean_squared_error(Y,Y_NEW))
    r2 = r2_score(Y,Y_NEW)

    print('RMSE: ', rmse)
    print('R2: ', r2)

    predict=[[pred]]
    X_NEW = polynomial_features.fit_transform(X)
    Y_NEW = model.predict(X_NEW)
    predict_ = polynomial_features.fit_transform(predict)
    clf = linear_model.LinearRegression()
    clf.fit(X_NEW,Y_NEW)
    predict_=clf.predict(predict_)
    if pred==0:
        None
    elif pred>=len(ctr_dict):
        print("Predicted Value : ",predict_[0][0])
    else:
        print("Correct Value : ",ctr_dict[pred+1]," |  Fitted Value : ",predict_[0][0])
    plt.plot(X, Y_NEW, color='green', linewidth=2)
    plt.title("Cases Graph for Country : "+name)
    plt.show()
