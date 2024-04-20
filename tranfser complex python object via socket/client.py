import pickle
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9998))

try:
    myobject={'key1':'value1','key2':'value2'}
    serialized=pickle.dumps(myobject)
    print(serialized)
    client.sendall(serialized)
finally:
    client.close()
