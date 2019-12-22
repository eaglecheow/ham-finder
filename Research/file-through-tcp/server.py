import random
import socket, select
from time import gmtime, strftime

image = "yuju.jpg"

HOST = "127.0.0.1"
PORT = 8888

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_clients_sockets.append(server_socket)

while True:
    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])

    for sock in read_sockets:
        if sock == server_socket:

            sockfd, client_address = server_socket.accept()
            connected_clients_sockets.append(sockfd)

        else:
            try:
                data = sock.recv(4096)

                if data:

                    txt = data.strip()
                    print("--{}--".format(txt))

                    if txt == b"GET":
                        sock.sendall(b"OK\r\n")
                    elif txt == b"GET_SIZE":
                        with open(image, "rb") as f1:
                            file_size = len(f1.read())
                            f1.seek(0)

                        print("--{}--".format(file_size))
                        sock.sendall(("SIZE {}".format(file_size)).encode())

                    elif txt == b"GET_IMG":
                        with open(image, "rb") as fp:
                            image_data = fp.read()

                        msg = image_data + b"EOF\r\r"
                        print("Sending sending...")
                        sock.sendall(msg)
                        print(msg)

            except:
                sock.close()
                connected_clients_sockets.remove(sock)
                continue

server_socket.close()