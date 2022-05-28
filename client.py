
import socket
import time
HOST = "localhost"  # The server's hostname or IP address
PORT = 11000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1)
        # time.sleep(1)
        print(f"Received {data!r}")
        # s.sendall(f"ACK {data!r}".encode('utf-8'))
        # time.sleep(1)

