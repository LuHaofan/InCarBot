import socket
from CameraModule import CameraModule
import struct
import pickle
import cv2 as cv

HOST = "192.168.0.243"
PORT = 10089

cam = CameraModule()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server up and waiting for connection")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            left = cam.getLeft()
            #cv.imshow("Left", left)
            right = cam.getRight()
            #cv.imshow("Right", right)
            
            if left is not None:
                a = pickle.dumps(left)
                message = struct.pack("Qi",len(a), 0)+a
                conn.sendall(message)
                
            
            if right is not None:
                a = pickle.dumps(right)
                message = struct.pack("Qi",len(a), 1)+a
                conn.sendall(message)
                
            if cv.waitKey(1) & 0xFF == ord('q'):
                cam.close()
                break
        s.close()
                
            
        