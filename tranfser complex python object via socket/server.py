import pickle
import socket

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
        print(f'Received: {received_object}')
    finally:
        client.close()
