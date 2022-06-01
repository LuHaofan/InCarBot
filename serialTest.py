#!/usr/bin/env python3
import serial
import time
import socket
import subprocess

HOST = "192.168.1.253"  # The server's hostname or IP address
PORT = 11000  # The port used by the server

if __name__ == '__main__':
    proc = subprocess.Popen(["ls /dev/ | grep ttyUSB"], stdout=subprocess.PIPE, shell = True)
    (out, err) = proc.communicate()
    usb = out.decode().rstrip()
    ser = serial.Serial('/dev/'+usb, 9600, timeout=1)
    ser.reset_input_buffer()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            data = s.recv(1024)
            if len(data) >= 1:
                tmp = data.decode()
                print("recv:",tmp)
                cmd = tmp[0]
                if cmd == 'a':
                    msg = 10
                else:
                    msg = int(cmd)
                print("To send:", msg)

                ser.write(msg.to_bytes(1, 'big'))
                line = ser.readline().rstrip()
                print(line)
                #line = ser.readline().rstrip()
                #print("Second Line", line)
                ser.reset_input_buffer()

            time.sleep(0.05)
