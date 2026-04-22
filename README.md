# Context-Aware-Smart-Room
A real-time intelligent system that combines computer vision and embedded sensors to understand room conditions and take automated actions.

##  Features

-  Human detection using OpenCV
-  Multi-sensor fusion (temperature, gas, light)
-  Real-time decision making
-  ESP32 hardware control
-  LED + Servo actuation

---

## 🧠 System Architecture

Camera → Python (OpenCV) → Decision Logic → ESP32 → LED & Servo

## ⚙️ Technologies Used

- Python (OpenCV, PySerial)
- ESP32 (Arduino)
- Embedded Sensors (DHT11, Gas, LDR)
- Computer Vision


## 🔧 How It Works

1. Camera detects number of people
2. ESP32 sends sensor data (temp, gas, light)
3. Python processes all inputs
4. System decides room state
5. ESP32 performs action:
   - LED ON/OFF
   - Servo movement


## 📊 States

- EMPTY → No activity
- NORMAL → Single person
- CROWDED → Multiple people
- HOT → High temperature
- DANGER → Gas detected



## 🧪 How to Run

1. Upload ESP32 code
2. Connect ESP32 via USB
3. Install Python dependencies:

pip install -r requirements.txt

4. Run:

python.py



## 📸 Demo
Video and demo images are attached!
For demo video - https://youtube.com/shorts/hg6EIxZy77o?si=Inv1QP_6sTiIceUK


---

## 🔥 Future Improvements

- Replace rule-based logic with ML model
- Add multiple LEDs (RGB)
- Dashboard visualization
- Edge AI deployment

---

## 💡 Author

Yug Shah
