import socket

client = socket.socket()

client.connect(("localhost", 9999))

name = input("Enter your name: ")
client.send(bytes(name, "utf-8"))

print(client.recv(1024).decode())