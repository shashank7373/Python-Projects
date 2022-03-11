import socket
import threading

nickname = input("Please input your nickname: ")

HOST = "localhost"
PORT = 65345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("An error occurred")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input()}"
        client.send(message.encode("ascii"))

rec_thread = threading.Thread(target=receive)
rec_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()