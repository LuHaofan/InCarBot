#include <Servo.h>
// Servo 10, range 80~120
// Servo 9, range 0~150
// Servo 11, range 80~150
Servo myservo;
int pos = 100;

void setup(){
  myservo.attach(11);
}

void loop(){
  for (pos = 80; pos <= 150; pos+=5){
    myservo.write(pos);
    delay(100);
  }
//    pos = 160;
//    myservo.write(pos);
  for (pos = 150; pos >= 80; pos-=5){
    myservo.write(pos);
    delay(100);
  }
}
