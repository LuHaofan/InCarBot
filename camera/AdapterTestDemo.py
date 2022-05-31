import RPi.GPIO as gp
import os
from picamera import PiCamera
import time

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)
#cam = PiCamera()
#cam.resolution = (320, 240)

def main():
    '''
    print('Start testing the camera A')
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    capture(1)
    
    print('Start testing the camera B') 
    i2c = "i2cset -y 1 0x70 0x00 0x05"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, False)
    gp.output(12, True)
    capture(2)
    
    print('Start testing the camera C')
    i2c = "i2cset -y 1 0x70 0x00 0x06"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)
    capture(3)
    '''
    time.sleep(1)
    print('Start testing the camera D')
    i2c = "i2cset -y 1 0x70 0x00 0x07"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, True)
    gp.output(12, False)
    capture(4)
    
def capture(idx):
    cmd = "libcamera-still -o capture_%d.jpg" % idx
    os.system(cmd)
    #cam.start_preview()
    #time.sleep(1)
    #cam.capture("./capture_%d.jpg" % idx)

if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
