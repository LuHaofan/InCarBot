import socket
import struct
import time
import pickle
import cv2
HOST = "192.168.0.243"  # The server's hostname or IP address
PORT = 10089  # The port used by the server

data = b""
payload_size = struct.calcsize("Qi")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        while len(data) < payload_size:
            packet = s.recv(4*1024)
            if not packet: break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size, side = struct.unpack("Qi", packed_msg_size)
        while len(data) < msg_size:
            data += s.recv(4*1024)
        frame_data= data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        if side == 0:
            cv2.imshow("Left", frame)
        elif side == 1:
            cv2.imshow("Right", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    s.close()