#include <Servo.h> 

Servo Servo_front_right; 
Servo Servo_back_right;
Servo Servo_front_left; 
Servo Servo_back_left;

int a=90,b=90,c=90,d=90;

void setup() { 
  Servo_front_right.attach(3); 
  Servo_back_right.attach(12);
  Servo_front_left.attach(9); 
  Servo_back_left.attach(5);
  // intialize and check legs are aligned
  Servo_front_right.write(a);
  Servo_back_right.write(b);
  Servo_front_left.write(c);
  Servo_back_left.write(d); 
  delay(3000); 
}


void loop(){
  Servo_front_right.write(a);
  Servo_back_right.write(b);
  Servo_front_left.write(c);
  Servo_back_left.write(d); 
  delay(1000); 
   //HM(a,b,c,d) 
  Servo_front_right.write(a);
  Servo_back_right.write(b+50);
  Servo_front_left.write(c-50);
  Servo_back_left.write(d); 
  delay(1000);
  //Servo_front_right.write(c-50);
  delay(1000);
 
  Servo_front_right.write(c-50);
  Servo_front_right.write(a+50);
  Servo_back_right.write(b+50);
  Servo_back_left.write(d+50); 
  delay(4000); 
  Servo_front_right.write(a-50);
  Servo_back_right.write(b-50);
  Servo_front_left.write(c+50);
  Servo_back_left.write(d+50); 
  delay(2000); 
  //exit(1);
}
