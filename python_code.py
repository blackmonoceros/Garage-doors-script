'''
Python Code
Below is the Python code that sends commands to the Arduino via the serial port.

'''

import serial
import time

# Serial port settings
arduino_port = "COM3"  # Change to the appropriate port (e.g., /dev/ttyUSB0 on Linux)
baud_rate = 9600       # Must match Arduino settings

# Initialize connection to Arduino
try:
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    print("Connected to Arduino on port:", arduino_port)
except Exception as e:
    print("Failed to connect to Arduino:", e)
    exit()

# Function to send commands
def send_command(command):
    try:
        arduino.write((command + '\n').encode())  # Send command
        print(f"Sent command: {command}")
        time.sleep(1)  # Wait for execution
    except Exception as e:
        print("Error sending command:", e)

# Example usage
while True:
    user_input = input("Type 'OPEN' to open the door or 'CLOSE' to close it: ").strip().upper()
    if user_input in ["OPEN", "CLOSE"]:
        send_command(user_input)
    elif user_input == "EXIT":
        print("Closing the program...")
        break
    else:
        print("Unknown command. Please try again.")

# Close the connection
arduino.close()