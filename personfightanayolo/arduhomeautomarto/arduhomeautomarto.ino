#include <Servo.h>

Servo myServo;
int servoPin = 9;
char receivedData;

void setup() {
    Serial.begin(9600);
    myServo.attach(servoPin);
    myServo.write(0);  // Initial position
}

void loop() {
    if (Serial.available() > 0) {
        receivedData = Serial.read();
        
        if (receivedData == '1') {
            myServo.write(90);  // Move servo to 90° (Activate)
            Serial.println("Servo Activated");
        } 
        else if (receivedData == '0') {
            myServo.write(0);  // Reset to 0° (Initial position)
            Serial.println("Servo Reset");
        }
    }
}

