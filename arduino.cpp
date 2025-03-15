/******************************************************************************
Arduino Code
First, write the code for the Arduino. Make sure you have the Servo library 
installed (if using a servo motor) or connect a relay.
*******************************************************************************/

#include <Servo.h>

Servo doorServo; // If using a servo motor
const int relayPin = 7; // If using a relay

void setup() {
  Serial.begin(9600); // Initialize serial port
  doorServo.attach(9); // Connect servo motor to pin 9
  pinMode(relayPin, OUTPUT); // Set relay pin as output
  digitalWrite(relayPin, LOW); // Ensure the relay is off
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Read command

    if (command == "OPEN") {
      doorServo.write(90); // Open the door (for servo motor)
      digitalWrite(relayPin, HIGH); // Turn on relay
      delay(1000); // Time to open
      digitalWrite(relayPin, LOW); // Turn off relay
    } else if (command == "CLOSE") {
      doorServo.write(0); // Close the door (for servo motor)
    }
  }
}