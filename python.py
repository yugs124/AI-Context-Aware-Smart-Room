import cv2
import serial
import time

ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
while True:

    # -------- CAMERA --------
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    people = len(faces)

    # -------- SENSOR DATA FROM ESP --------
    if ser.in_waiting:
        line = ser.readline().decode(errors='ignore').strip()

        try:
            temp, hum, gas, light = map(float, line.split(","))
        except:
            continue

        # -------- DECISION LOGIC --------

        if people == 0:
            state = "EMPTY"

        elif gas > 1500:
            state = "DANGER"

        elif temp > 32:
            state = "HOT"

        elif people == 1:
            state = "NORMAL"

        else:
            state = "CROWDED"

        print(f"People:{people} Temp:{temp} Gas:{gas} → {state}")

        # -------- SEND TO ESP --------
        ser.write((state + "\n").encode())

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()