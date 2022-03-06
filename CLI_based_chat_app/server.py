import socket
import sys
import threading
import traceback

s_lock = threading.Lock()


def server_socket():
    host = "localhost"
    port = 9999
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created")
    try:
        soc.bind((host, port))
    except Exception as msg:
        print("Counld not bind to host {}, port {} : {}".format(host, port, msg))
        sys.exit(0)
    soc.listen(6)
    print("Server is now listening..")
    try:
        while True:
            (conn, ip) = soc.accept()
            c_host, c_port = str(ip[0]), str(ip[1])
            print("Connected with client {} : {}".format(c_host, c_port))
            try:
                client_thread = threading.Thread(target=client_process, args=(conn, c_host, c_port, ), )
                client_thread.start()
            except Exception:
                print("Failed to create a client thread")
                traceback.print_exc()
            else:
                client_thread.join()
    except KeyboardInterrupt:
        print("Server closed manually. Bye..")
        soc.close()


def client_process(connection, host, port):
    is_active = True
    while is_active:
        client_input = receive_input(connection, 5120)
        if "QUIT" in client_input:
            print("Client is requesting to exit.")
            connection.close()
            print("Connect {} : {} closed".format(host, port))
            is_active = False
        else:
            #s_lock.acquire()
            processed_input = process_input(client_input)
            print("Process result : {}".format(processed_input))
            connection.sendall(str(processed_input)[::-1].encode("utf8"))
            #s_lock.release()


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    if client_input_size > max_buffer_size:
        print("The input size {} is greater than {}".format(client_input_size, max_buffer_size))
    decoded_input = client_input.decode("utf8")
    result = process_input(decoded_input)
    return result


def process_input(decoded_input):
    print("Processing the input received from client : {}".format(decoded_input))
    return "Processed input : {}".format(decoded_input.upper())


if __name__ == "__main__":
    server_socket()