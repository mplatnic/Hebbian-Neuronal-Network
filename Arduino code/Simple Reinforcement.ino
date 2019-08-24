// Machine learning crawling Robot using Simple Reinforcement Learning
// inspired by: jim demello
// Servo setup: the servos must be oriented so that if the arm is rotating counter-clockwise to the left of the servo, then up is 0 degrees
// and down is 180 degrees, for both servos. Then when the arm is in it's highest postion, servo 1 (the servo closest to the
// body of the robot, will be at 0 degrees and servo 2 will be at 40 degrees.)
// Sonar: the ultrasonic module should be placed facing the rear of the robot as it measures movement of the robot away from some
// solid structure like a wall.
// TODO: 1. smooth servo arm movements (simultaneous moves) - done
// 2. lower servo starting positions - done
// 3. try using wheel encoder rather than ultrasonic module for greater precision and so that robot does not have to
// measure distance from another object.
// goal: move between two arm positions that produce the greatest distance, without using arrays to store results.
// algorithm: this is a positive reinforcement unsupervised learning algorithm
// It chooses random servo positions for two arm positions -
// and then moves the arm from the first to the second position, gets distance moved and then if it is greater than
// 2cms, it keeps the arm positions that produce the greatest distance.


#include
Servo servo1,servo2;

#ifdef __arm__
// should use uinstd.h to define sbrk but Due causes a conflict
extern "C" char* sbrk(int incr);
#else // __ARM__
extern char *__brkval;
#endif // __arm__

int freeMemory() { // this routine reports on free ram space
  char top;
  #ifdef __arm__
  return &top - reinterpret_cast(sbrk(0));
  #elif defined(CORE_TEENSY) || (ARDUINO > 103 && ARDUINO != 151)
  return &top - __brkval;
  #else // __arm__
  return __brkval ? &top - __brkval : &top - __malloc_heap_start;
  #endif // __arm__
}

float distance;
float sonarTime;
int TRIGGER=7,ECHO=8; // sonar pins
//int state=0;
//int numberSuccesses = 0;
int episodes = 0;
int spos1 = 0; // servo1 position
int spos2 = 0; // servo2 position
int spos3 = 0; // servo1 position
int spos4 = 0; // servo2 position
int spos1High =0; // servo1 highest position
int spos2High =0;
int spos3High =0;
int spos4High =0;
int distanceHigh=0;
float distDifference=0,distPrevious=0,distCurrent=0;

void setup (){
  Serial.begin(9600);
  servo1.attach( 9, 600, 2400 );
  servo2.attach( 6, 600, 2400 );
  myServo(servo1,0,1,8,1); // set servos to zero position  
  delay(1000);
  myServo(servo2,0,1,8,1); // (Servo servo,int newAngle,int angleInc,int incDelay,int servoNum)
  delay(1000);
  pinMode(TRIGGER, OUTPUT); // setup sonar
  pinMode(ECHO, INPUT);
  randomSeed(analogRead(0)); // get real random number seed
  distPrevious = getDistance(); //get initial distance
  Serial.println(distPrevious);
  delay(1000);
  // exit(0); // exit here to just test sonar
} // end setup

float getDistance() { // routine to measure distance = call and average it 5 times
  int numberTriggers = 5;
  int average = 0;
  for(int i=0;i
    digitalWrite(TRIGGER, LOW);
    delayMicroseconds(5);
    digitalWrite(TRIGGER, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER, LOW);
    sonarTime = pulseIn(ECHO, HIGH);
    distance = sonarTime / 58.00;
    average = average + distance;
  // Serial.print(sonarTime);Serial.print(" ");Serial.print(distance);Serial.println("cm");
    delay(100);
    } // end for i

  average = average / numberTriggers;
  Serial.println(average);
  return average;
  }// end get ultrasonic distance routine

void doTraining() {
  Serial.println("Do doTraining...");
  episodes = 40;
  for (int episode=0;episode
  {
    spos1 = random(160);
    spos2 = random(160);
    spos3 = random(160);
    spos4 = random(160);
    myServo(servo1,spos1,1,7,1);  // (Servo servo,int newAngle,int angleInc,int incDelay,int servoNum)
    myServo(servo2,spos2,1,7,1);
    myServo(servo1,spos3,1,7,1);
    myServo(servo2,spos4,1,7,1);
    distCurrent = getDistance(); // get distance - note this is not always accurate so sometimes robot will just claw the air
    distDifference = distCurrent - distPrevious;   //NOT USED
    distPrevious = distCurrent;                    //NOT USED
    Serial.print(" episode = ");Serial.print(episode);
    // Serial.print(" state = ");Serial.print(state);
    Serial.print(" spos1 = ");Serial.print(spos1);
    Serial.print(" spos2 = ");Serial.print(spos2);
    Serial.print(" spos3 = ");Serial.print(spos3);
    Serial.print(" spos4 = ");Serial.print(spos4);
    Serial.print(" distance = ");Serial.println();
    if ( distCurrent > distanceHigh) { // if current distance is greater than previous then replace positions
      //HERE SHOULD BE DISTDIFFERENCE > DISTANCE HIGH 
      spos1High = spos1; // servo position 1
      spos2High = spos2; // servo position 2
      spos3High = spos3; // servo position 3
      spos4High = spos4; // servo position 4
      distanceHigh = distCurrent;   //SHOULD BE DISTDIFFERENCE
      // distPrevious = distCurrent;
    }
  } // end each episode
Serial.print("spos1High = ");Serial.println(spos1High);
Serial.println(" ");
} // end doTraining

void doLearnedBehavior() {
  Serial.println("Do Learned behavior... ");
  myServo(servo1,0,1,8,1);
  myServo(servo2,0,1,8,1);
  delay(2000);
  for (int i=0;i<30;i++) {
    Serial.print(" spos1High= "); Serial.print(spos1High);
    Serial.print(" spos2High = ");Serial.print(spos2High);
    Serial.print(" spos3High = ");Serial.print(spos3High);
    Serial.print(" spos4High = ");Serial.println(spos4High);
    myServo(servo1,spos1High,1,7,1);
    myServo(servo2,spos2High,1,7,1);
    myServo(servo1,spos3High,1,7,1);
    myServo(servo2,spos4High,1,7,1);
  } // doLearned
} // end loop

void loop(){ // main loop reads success table and performs actions
  int freespace = freeMemory(); Serial.print("free memory= "); Serial.println(freespace);
  doTraining(); // trial and error training with distance reinforcement
  freespace = freeMemory(); Serial.print("free memory= "); Serial.println(freespace);
  doLearnedBehavior(); // do longest step 10 times to make robot crawl
  myServo(servo1,0,1,8,1);
  myServo(servo2,0,1,8,1);
  Serial.print("end program ");
  delay(2000);
  exit(0); // quit program
} // end main loop

void myServo(Servo servo,int newAngle,int angleInc,int incDelay,int servoNum) {
  int curAngle = 0;
  curAngle = servo.read();
  if (curAngle < newAngle) {
    for(int angle=curAngle;angle < newAngle;angle += angleInc) {
    servo.write(angle);
    delay(incDelay); }
  }
  else if (curAngle > newAngle) {
  for(int angle=curAngle;angle > newAngle;angle -= angleInc) {
    servo.write(angle);
    delay(incDelay); }
  }
} // end of myServo function
