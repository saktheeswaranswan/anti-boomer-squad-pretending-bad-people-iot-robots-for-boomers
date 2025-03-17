import cv2
import mediapipe as mp
import serial
import time

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Initialize Serial Communication (Change COM port accordingly)
arduino = serial.Serial('COM3', 9600)  # Use '/dev/ttyUSB0' for Linux
time.sleep(2)  # Wait for connection to establish

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Check if pose is detected
    if results.pose_landmarks:
        arduino.write(b'0')  # If detected, reset servo
        print("Pose detected: Servo in initial position")
    else:
        arduino.write(b'1')  # If no pose, turn servo ON
        print("No pose detected: Activating servo")

    # Display output
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow("Pose Estimation", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
arduino.close()

