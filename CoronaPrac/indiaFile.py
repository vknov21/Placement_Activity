import numpy as np
import datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model

def dash_state(n):
    for i in range(n):
        print('—',sep='',end='')

def find(name, state_dict):
    states=[]
    for i in range(len(state_dict)):
        if(name==list(state_dict.keys())[i][:len(name)]):
            states.append(list(state_dict.keys())[i])
    return states

def draw_graph(state_name, state_data, pred):
    ##Graph for cases
    Y=np.array(list(state_data[0]))
    X=np.array(list(range(1,len(state_data[0])+1)))
    print()
    X = X[:,np.newaxis]
    Y = Y[:,np.newaxis]

    plt.scatter(X,Y)

    nb_degree = 4
    polynomial_features = PolynomialFeatures(degree = nb_degree)
    X_TRANSF = polynomial_features.fit_transform(X)

    model = LinearRegression()
    model.fit(X_TRANSF, Y)

    Y_NEW = model.predict(X_TRANSF)

    rmse = np.sqrt(mean_squared_error(Y,Y_NEW))
    r2 = r2_score(Y,Y_NEW)
    print(state_name)

    dash_state(len(state_name))
    print()
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
    elif pred>=len(state_data[0]):
        print("Predicted Value : ",predict_[0][0])
    else:
        print("Correct Value : ",state_data[0][pred+1]," |  Fitted Value : ",predict_[0][0])

    plt.plot(X, Y_NEW, color='green', linewidth=2)
    plt.title("Cases Graph for State : "+state_name)
    plt.show()

    ##Graph for Deaths
    Y=np.array(list(state_data[1]))
    X=np.array(list(range(1,len(state_data[1])+1)))
    print()
    X = X[:,np.newaxis]
    Y = Y[:,np.newaxis]

    plt.scatter(X,Y)

    nb_degree = 2
    polynomial_features = PolynomialFeatures(degree = nb_degree)
    X_TRANSF = polynomial_features.fit_transform(X)

    model = LinearRegression()
    model.fit(X_TRANSF, Y)

    Y_NEW = model.predict(X_TRANSF)

    rmse = np.sqrt(mean_squared_error(Y,Y_NEW))
    r2 = r2_score(Y,Y_NEW)
    print(state_name)

    dash_state(len(state_name))
    print()
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
    elif pred>=len(state_data[0]):
        print("Predicted Value : ",predict_[0][0])
    else:
        print("Correct Value : ",state_data[0][pred+1]," |  Fitted Value : ",predict_[0][0])

    plt.plot(X, Y_NEW, color='green', linewidth=2)
    plt.title("Deaths Graph for State : "+state_name)
    plt.show()

    ##Graph for Cures
    Y=np.array(list(state_data[2]))
    X=np.array(list(range(1,len(state_data[2])+1)))
    print()
    X = X[:,np.newaxis]
    Y = Y[:,np.newaxis]

    plt.scatter(X,Y)

    nb_degree = 3
    polynomial_features = PolynomialFeatures(degree = nb_degree)
    X_TRANSF = polynomial_features.fit_transform(X)

    model = LinearRegression()
    model.fit(X_TRANSF, Y)

    Y_NEW = model.predict(X_TRANSF)

    rmse = np.sqrt(mean_squared_error(Y,Y_NEW))
    r2 = r2_score(Y,Y_NEW)
    print(state_name)

    dash_state(len(state_name))
    print()
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
    elif pred>=len(state_data[0]):
        print("Predicted Value : ",predict_[0][0])
    else:
        print("Correct Value : ",state_data[0][pred+1]," |  Fitted Value : ",predict_[0][0])

    plt.plot(X, Y_NEW, color='green', linewidth=2)
    plt.title("Cure Graph for State : "+state_name)
    plt.show()


def main(fileName):
    my_data=np.genfromtxt(fileName,delimiter=",",dtype='unicode')#,encoding=None)
    my_data=my_data[1:,1:].T
    my_data=np.delete(my_data,1,0)
    my_data=np.delete(my_data,3,0)
    my_data=np.delete(my_data,2,0)

    #Modifying all '-' calues to 0 to get all integers
    for i in range(len(my_data)):
        my_data[i]=['0' if x=='-' else x for x in my_data[i]]
    my_data=my_data.T
    date1=my_data[0][0]
    date2=my_data[-1][0]
    step=datetime.timedelta(days=1)
    start=datetime.datetime.strptime(date1,'%d/%m/%y')
    end=datetime.datetime.strptime(date2,'%d/%m/%y')
    date_dict={}
    while(start<=end):          #Creating list of Dates
        date_dict['{}/{}/{}'.format(start.strftime('%d'),start.strftime('%m'),start.strftime('%y'))]=''
        start+=step

    state_dict={}
    for i in range(len(my_data)):
        state_dict[my_data[i][1]]=[[],[],[]]

    for i in range(len(my_data)):
        state_dict[my_data[i][1]][0].append(my_data[i][-1])         #Total Cases
        state_dict[my_data[i][1]][1].append(my_data[i][-2])         #Total Deaths
        state_dict[my_data[i][1]][2].append(my_data[i][-3])         #Total Cured
    for i in range(len(state_dict)):
        state_dict[list(state_dict.keys())[i]][0]=list(map(eval,state_dict[list(state_dict.keys())[i]][0]))            #Converting to integers
        #,list(map(eval,state_dict[list(state_dict.keys())[0]][1])))
        state_dict[list(state_dict.keys())[i]][1]=list(map(eval,state_dict[list(state_dict.keys())[i]][1]))
        state_dict[list(state_dict.keys())[i]][2]=list(map(eval,state_dict[list(state_dict.keys())[i]][2]))

    for i in range(len(state_dict)):
        state_dict[list(state_dict.keys())[i]][0]=((len(date_dict)-len(state_dict[list(state_dict.keys())[i]][0]))*[0])+state_dict[list(state_dict.keys())[i]][0]          #Merging 0's to all non-assigned for previous days
        state_dict[list(state_dict.keys())[i]][1]=((len(date_dict)-len(state_dict[list(state_dict.keys())[i]][1]))*[0])+state_dict[list(state_dict.keys())[i]][1]
        state_dict[list(state_dict.keys())[i]][2]=((len(date_dict)-len(state_dict[list(state_dict.keys())[i]][2]))*[0])+state_dict[list(state_dict.keys())[i]][2]

        state_dict[list(state_dict.keys())[i]][0]=np.array(state_dict[list(state_dict.keys())[i]][0])             #Converting to array
        state_dict[list(state_dict.keys())[i]][1]=np.array(state_dict[list(state_dict.keys())[i]][1])
        state_dict[list(state_dict.keys())[i]][2]=np.array(state_dict[list(state_dict.keys())[i]][2])
    p=len(state_dict)-1
    for i in range(p):
        if(state_dict[list(state_dict.keys())[i]][0][-1]<50):
            state_dict.pop(list(state_dict.keys())[i])
            p=p-1
            if(i==p):
                break
    state_dict.pop('Unassigned')
    k=input("Enter state name (Initials) : ")
    list_state=find(k.title(),state_dict)
    if(len(list_state)==0):
        print("Sorry! No such match")
    p=input("Predicting date (dd/mm/yy) (0 if not) : ")
    if(len(p)<2 or p[2]!='/' or p[5]!='/'):
        p=0
    else:
        start=datetime.datetime.strptime(date1,'%d/%m/%y')
        end=datetime.datetime.strptime(p,'%d/%m/%y')
        p=(end-start).days

    for i in range(len(list_state)):
        draw_graph(list_state[i].title(),state_dict[list_state[i]],p)
