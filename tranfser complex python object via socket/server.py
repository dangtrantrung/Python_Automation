import pickle
import socket

from sklearn.datasets import load_iris

data=load_iris()
X,y=data.data, data.target

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',9998))
server.listen(1)
while True:
    print('Waiting for connection')
    client,addr=server.accept()
    try:
        print('Client connected...')
        data=b''
        while True:
            chunk=client.recv(4096)
            if not chunk:
                break
            data+=chunk
        received_object=pickle.loads(data)

        model= received_object['model']
        report= received_object['report'].decode('ascii')
        print(f'Client Trained Model Accuracy: {model.score(X,y)}')
        print(f'Client Trained Model - Classification Report: {report}')
    finally:
        client.close()
