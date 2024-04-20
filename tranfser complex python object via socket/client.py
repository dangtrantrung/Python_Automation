import pickle

import socket

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data=load_iris()
X,y=data.data, data.target

X_train,X_test,y_train, y_test=train_test_split(X,y,test_size=0.5)
model=RandomForestClassifier()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
report=classification_report(y_test, y_pred)
print(report)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9998))
print('Client connected to server')

try:
    #myobject={'key1':'value1','key2':'value2'}
    # serialized=pickle.dumps(myobject)
    # serialized=pickle.dumps(model)
    serialized1=pickle.dumps(report.encode('ascii'))
    # client.sendall(serialized)
    client.sendall(serialized1)
    print('client.sendall(report)')

finally:
    client.close()
