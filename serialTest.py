#!/usr/bin/env python3
import serial
import time
import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 11000  # The port used by the server

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    # data = list(range(255))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1)
            # time.sleep(1)
            # print(f"Received {data!r}")
            ser.write(data)
            line = ser.readline().rstrip()
            print(line)