import socket
import threading

HOST = "localhost"
PORT = 65345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = list()
nicknames = list()

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            client.close()
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f"{nickname} left the chat.".encode("ascii"))
            break

def receive():
    while True:
        (client, address) = server.accept()
        print(f"Connected with {str(address)}")
        
        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)
        
        print(f"Nickname of the client {nickname}")
        client.send("Connected to the server.".encode("ascii"))
        broadcast(f"{nickname} joined the chat!".encode("ascii"))
        
        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()

receive()