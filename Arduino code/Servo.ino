#include <Servo.h> 

Servo Servo1; 
Servo Servo2;
float a=0,b=0,c=0,d=0;
float maxx=0,x=0;

void setup() { 
  
   Servo1.attach(5); 
   Servo2.attach(6); 
}
void loop(){
  
   //HM(a,b,c,d) 
   Servo1.write(a);
   Servo2.write(b); 
   delay(1000); 
   Servo1.write(c);
   Servo2.write(d); 
   delay(1000); 
   //מקורי 20 20 135 175
}
