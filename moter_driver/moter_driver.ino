#include <Adafruit_PWMServoDriver.h>

#include <Wire.h>
#include<Servo.h>
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x47);
Servo myservo1;

void advance(){
  pwm.setPWM(0,0,4095);
  pwm.setPWM(1,0,2000);
  pwm.setPWM(2,0,4095);
  pwm.setPWM(3,0,2000);
  pwm.setPWM(4,0,4095);
  pwm.setPWM(5,0,2000);
  pwm.setPWM(6,0,4095);
  pwm.setPWM(7,0,2000);
}

void turnR(){
  pwm.setPWM(0,0,4095);
  pwm.setPWM(1,0,2000);
  pwm.setPWM(2,0,4095);
  pwm.setPWM(3,0,2000);
  pwm.setPWM(4,0,3000);
  pwm.setPWM(5,0,2000);
  pwm.setPWM(6,0,3000);
  pwm.setPWM(7,0,2000);
}

void turnL(){
  pwm.setPWM(0,0,0);
  pwm.setPWM(1,0,2000);
  pwm.setPWM(2,0,0);
  pwm.setPWM(3,0,2000);
  pwm.setPWM(4,0,4095);
  pwm.setPWM(5,0,1000);
  pwm.setPWM(6,0,4095);
  pwm.setPWM(7,0,1000);
}

void stopp(){
  pwm.setPWM(1,0,0);
  pwm.setPWM(3,0,0);
  pwm.setPWM(5,0,0);
  pwm.setPWM(7,0,0);
}

void back(){
  pwm.setPWM(0,0,0);
  pwm.setPWM(1,0,2000);
  pwm.setPWM(2,0,0);
  pwm.setPWM(3,0,2000);
  pwm.setPWM(4,0,0);
  pwm.setPWM(5,0,2000);
  pwm.setPWM(6,0,0);
  pwm.setPWM(7,0,2000);
}

void setup(){
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(60);
  stopp();
}
void loop(){
//  stopp();
//    advance();
//    delay(2000);
//    back();
//    delay(2000);
    turnL();
    delay(5000);
//    turnR();
//    delay(5000);
}
