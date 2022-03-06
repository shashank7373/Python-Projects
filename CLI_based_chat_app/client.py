import socket
import sys
import traceback
import threading

c_lock = threading.Lock()


def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "localhost"
    port = 9999
    try:
        soc.connect((host, port))
    except Exception:
        print("Client failed to connect to server.")
        traceback.print_exc()
        sys.exit(0)
    print("Please enter quit to exit")
    while True:
        message = input(" -> ")
        if message == "quit":
            soc.send(b'--quit--')
            break
        soc.send(message.encode("utf8"))
        c_lock.acquire()
        message_received = soc.recv(5120).decode("utf8")
        if message_received:
            print("Message received from server: {}".format(message_received))
            c_lock.release()
        

if __name__ == "__main__":
    main()