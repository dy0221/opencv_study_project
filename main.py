import cv2
import mediapipe as mp
import my_package
import serial

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

#For serial input
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    timeout=0.005
)

# For webcam input:
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(
  model_selection=0, min_detection_confidence=0.5) as face_detection:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Processes an RGB image and returns a list of the detected face location data.
    results = face_detection.process(image)
    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  
    tx_buffer = [0,0,0,0,0]
    tx_buffer[0] = 0xff
    tx_buffer[1] = 0xff
    if results.detections:
      for detection in results.detections:
        nose_location = mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.NOSE_TIP)
        # print(nose_location)
        result,x,y = str(nose_location).split(': ')
        x = x[:-3]
        y = y[:-2]
        x = my_package.map(float(x) , 0 , 1, 640, 0)
        y = my_package.map(float(y) , 0 , 1, 480, 0)
        checksum = my_package.checksum(x,y)
        # print("x = {}, y = {}".format(int(x),int(y)))
        tx_buffer[2] = int(x)
        tx_buffer[3] = int(y)
        tx_buffer[4] = checksum
        print(tx_buffer)
        for i in range(len(tx_buffer)):
          ser.write(tx_buffer[i])
        # mp_drawing.draw_detection(image, detection)
    # Flip the image horizontally for a selfie-view display.
    # cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()

