#include <stdio.h>
#include <Servo.h>
#include "string.h"

#include <Wire.h>
#include "./Adafruit_PWMServoDriver.h"
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x47);
char buf[1];
Servo horizontal;
Servo vertical;
Servo grab;
int hzn = 90;
int vtc = 120;
int gb = 90;
/*
void advance() // going forward 
{
pwm.setPWM(0,0,4095); pwm.setPWM(1,0,1000); pwm.setPWM(2,0,4095); pwm.setPWM(3,0,1000); pwm.setPWM(4,0,4095); pwm.setPWM(5,0,1000); pwm.setPWM(6,0,4095); pwm.setPWM(7,0,1000);
Serial.println("forward");
}*/

void advance(){
  pwm.setPWM(0,0,4095);
  pwm.setPWM(1,0,2000);
  pwm.setPWM(2,0,4095);
  pwm.setPWM(3,0,2000);
  pwm.setPWM(4,0,4095);
  pwm.setPWM(5,0,2000);
  pwm.setPWM(6,0,4095);
  pwm.setPWM(7,0,2000);
  Serial.println("forward");
}
void turnR() //turn right
{ pwm.setPWM(0,0,4095); pwm.setPWM(1,0,2000); pwm.setPWM(2,0,4095); pwm.setPWM(3,0,2000); pwm.setPWM(4,0,0); pwm.setPWM(5,0,2000); pwm.setPWM(6,0,0); pwm.setPWM(7,0,2000);
}
void turnL() //turn left
{
pwm.setPWM(0,0,0); pwm.setPWM(1,0,2000); pwm.setPWM(2,0,0); pwm.setPWM(3,0,2000); pwm.setPWM(4,0,4095); pwm.setPWM(5,0,2000); pwm.setPWM(6,0,4095); pwm.setPWM(7,0,2000);
}
void stopp() //stop
{ pwm.setPWM(1,0,0); pwm.setPWM(3,0,0); pwm.setPWM(5,0,0); pwm.setPWM(7,0,0);
}
void back() //back
{
pwm.setPWM(0,0,0); pwm.setPWM(1,0,2000); pwm.setPWM(2,0,0); pwm.setPWM(3,0,2000); pwm.setPWM(4,0,0); pwm.setPWM(5,0,2000); pwm.setPWM(6,0,0); pwm.setPWM(7,0,2000);Serial.println("back");
}
void armL()
{
  if(hzn>=1)
  {
    hzn-=1;
    horizontal.write(hzn);
  }
}
void armR()
{
  if(hzn<=149)
  {
    hzn+=1;
    horizontal.write(hzn);
  }
}

void armU()
{
  if(vtc<=119){
      vtc+=1;
      vertical.write(vtc);
  }
}

void armD()
{
  if(vtc>=79){
      vtc-=1;
      vertical.write(vtc);
  }
}

void armRelease()
{
  if(gb<=149){
    gb+=1;
    grab.write(gb);
  }
}

void armGrab()
{
  if(gb>=89){
    gb-=1;
    grab.write(gb);
  } 
}

void reconfig()
{
  hzn = 90;vtc = 120;gb = 90;
  grab.write(gb);
  vertical.write(vtc);
  horizontal.write(hzn);
  delay(1000);
}

void setup() {
  Serial.begin(9600);
  horizontal.attach(9);
  vertical.attach(10);
  grab.attach(11);
  grab.write(gb); 
  vertical.write(vtc);
  horizontal.write(hzn);
  pwm.begin(); 
  pwm.setPWMFreq(60);
 
  delay(1000);
  stopp(); //Car stops
}


void loop() {
  if (Serial.available() > 0) {
    Serial.readBytes(buf, 1);
    
    if (buf[0] == byte(0))
        stopp();
    else if(buf[0] == byte(1))
        advance();
    else if(buf[0] == byte(2))
        back();
    else if(buf[0] == byte(3))
        turnL();
    else if(buf[0] == byte(4))
        turnR();
    else if(buf[0] == byte(5))
        armD();
    else if(buf[0] == byte(6))
        armU();
    else if(buf[0] == byte(7))
        armR();
    else if(buf[0] == byte(8))
        armL();
    else if(buf[0] == byte(9))
        armRelease();
    else if(buf[0] == byte(10))
        armGrab();   
    delay(50);
    Serial.print("You sent me: ");
    Serial.println(buf[0]);  
    Serial.print(hzn);
    Serial.print(vtc);
    Serial.print(gb);
  }
  else {
    stopp(); //Car stops
  }
}
