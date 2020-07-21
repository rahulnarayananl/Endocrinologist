import pickle
import os
import sys
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train():
    dataset = pd.read_csv('pima.csv')
    X = dataset[['F','D','E','B','C']]
    Y = dataset[['I']]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 101)
    
    from sklearn.svm import SVC
    model = SVC(kernel='linear')
    svc=model.fit(X_train,Y_train.values.ravel())
    
    with open('svc.pkl','wb') as m:
        pickle.dump(svc,m)
    test(X_test,Y_test)


def test(X_test,Y_test):
    with open('svc.pkl','rb') as mod:
        p=pickle.load(mod)
    pre=p.predict(X_test)
    print("\nACCURACY OF SVM CLASSIFIER :")
    print (accuracy_score(Y_test,pre)) 


def find_data_file(filename):
    if getattr(sys, "frozen", False): 
        datadir = os.path.dirname(sys.executable)
    else:
        datadir = os.path.dirname(__file__)
    return os.path.join(datadir, filename)


def check_input(data) ->int :
    df=pd.DataFrame(data=data,index=[0])
    with open(find_data_file('svc.pkl'),'rb') as model:
        p=pickle.load(model)
    op=p.predict(df)
    return op[0]
if __name__=='__main__':
    train()    