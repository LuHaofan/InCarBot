import RPi.GPIO as gp
import os
from picamera import PiCamera
from time import sleep
import cv2 as cv
import numpy as np

class CameraModule():
    adapter_info = {
                    "Right":{
                            "i2c_cmd":"i2cset -y 1 0x70 0x00 0x05",
                            "gpio_sta":[1,0,1],
                        },
                    "Left":{
                            "i2c_cmd":"i2cset -y 1 0x70 0x00 0x07",
                            "gpio_sta":[1,1,0],
                        },
                     }
    camera = cv.VideoCapture(0)
    camera.set(cv.CAP_PROP_FPS, 30)
    width = 1024
    height = 768 
    
    def __init__(self):
       gp.setwarnings(False)
       gp.setmode(gp.BOARD)
       gp.setup(7, gp.OUT)
       gp.setup(11,gp.OUT)
       gp.setup(12,gp.OUT)
       
    def choose_channel(self,key):
        channel_info = self.adapter_info[key]
        if channel_info == None:
            print("Can't get this info")
        os.system(channel_info["i2c_cmd"]) # i2c write
        gpio_sta = channel_info["gpio_sta"] # gpio write
        gp.output(7, gpio_sta[0])
        gp.output(11, gpio_sta[1])
        gp.output(12, gpio_sta[2])
        
    def select_channel(self,key):
        channel_info = self.adapter_info[key]
        if channel_info == None:
            print("Can't get this info")
        gpio_sta = channel_info["gpio_sta"] # gpio write
        gp.output(7, gpio_sta[0])
        gp.output(11, gpio_sta[1])
        gp.output(12, gpio_sta[2])
        
    def init(self,width,height):
        for cam in self.adapter_info.keys():
            print("Initializing Camera", cam)
            self.height = height
            self.width = width
            self.choose_channel(cam)
            self.camera.set(3, self.width)
            self.camera.set(4, self.height)
            ret, frame = self.camera.read()
            print(ret, frame)
            if ret == True:
                print("camera %s init OK" % cam)
                pname = "image_"+ cam +".jpg"
                cv.imwrite(pname,frame)
                sleep(1)
                
    def preview(self):
        #self.camera.set(cv.CAP_PROP_EXPOSURE, -4)
        while True:
            frame = self.getRight()
            cv.imshow("Right", frame)
            
            frame = self.getLeft()
            cv.imshow("Left", frame)
            
            if cv.waitKey(1) & 0xFF == ord('q'):
                del frame
                self.camera.release()
                cv.destroyAllWindows()
                break
            
    def getLeft(self):
        self.choose_channel("Left")
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        if ret == True:
            return frame
        else:
            print("Fail to get Left frame")
            return None
            
    def getRight(self):
        self.choose_channel("Right")
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        ret, frame = self.camera.read()
        if ret == True:
            return frame
        else:
            print("Fail to get Right frame")
            return None
                
    def close(self):
        self.camera.release()
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
        cv.destroyAllWindows()
        
if __name__ == "__main__":
    cam = CameraModule()
    cam.preview()
    '''
    while True:
        left = cam.getLeft()
        cv.imshow("Left", left)
        if cv.waitKey(1) & 0xFF == ord('q'):
            del left
            self.camera.release()
            cv.destroyAllWindows()
            break
    '''
    #cam.init(1024, 768)
    #cam.init(1024,768)
    #cam.preview()
    #cam.capture("Left")
    #sleep(1)
    #cam.choose_channel("Right")
    #cam.capture("Right")
    cam.close()
    
   