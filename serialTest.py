#!/usr/bin/env python3
import serial
import time
import socket

HOST = "192.168.1.162"  # The server's hostname or IP address
PORT = 11000  # The port used by the server

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            data = s.recv(1024)
            if len(data) >= 1:
                tmp = data.decode()
                print("recv:",tmp)
                cmd = tmp[0]
                msg = int(cmd)
                print("To send:", msg)
                print(msg.to_bytes(1, 'big'))
                ser.write(msg.to_bytes(1, 'big'))
                line = ser.readline().rstrip()
                print(line)
                ser.reset_input_buffer()

            time.sleep(1)