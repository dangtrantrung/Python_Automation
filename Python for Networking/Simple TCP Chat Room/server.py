import socket
import threading

host='127.0.0.1'
port=9090
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[]
nicknames=[]

def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index =clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast(f'{nickname} left the chat room'.encode('ascii'))
            nicknames.remove(nickname)
            break
def receive():
    while True:
        client,address=server.accept()
        print(f'Connected with address: {str(address)}')
        client.send('NICK'.encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat room!'.encode('ascii'))
        client.send(f'Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

print('Server is listening...')
receive()
