import socket

serv = socket.socket()
print("Server created successfully")

serv.bind(("localhost", 9999))

serv.listen(3)
print("waiting for connections..")

while True:
    (client, ip_addr) = serv.accept()
    
    name = client.recv(1024).decode()
    
    print("Successfully connected with {} at (IP -> {}, Port -> {})".format(
        name, ip_addr[0], ip_addr[1]))
    
    client.send(bytes("Welcome to CLI chat tool", "utf-8"))
    
    client.close()
