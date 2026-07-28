# 🍌 Saba Counting System

An ML-powered Saba banana counting system using **YOLO Instance Segmentation**, **OpenCV**, and **Firebase Realtime Database** for real-time detection, counting, and monitoring.

The system detects Saba bananas through a camera, counts objects, estimates price, and sends data to Firebase for monitoring.

---

## ✨ Features

- 🍌 Real-time Saba detection
- 🤖 YOLO Instance Segmentation
- 🔢 Object counting
- 💰 Automatic price estimation
- ☁️ Firebase Realtime Database
- 🌐 Web monitoring dashboard
- 📡 ESP8266 sensor integration

---

## 🛠️ Technologies

- Python
- Ultralytics YOLO
- OpenCV
- Firebase Realtime Database
- Firebase Admin SDK
- HTML / CSS / JavaScript
- ESP8266

---

## 📂 Project Structure

```
Saba-Counting-System/
│
├── Counting_firebase.py       # Main detection system
├── Picture_prediction.py      # Image prediction testing
├── Training.py                # YOLO training script
├── SabaWeb.html               # Web dashboard
│
├── models/
│   └── last.pt                # YOLO model (not included)
│
├── firebase/
│   └── saba_key.json          # Firebase key (not included)
│
├── .env                       # Configuration file (not included)
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/JayceeMolina/Saba-Counting-System.git

cd Saba-Counting-System
```

Install dependencies:

```bash
pip install ultralytics opencv-python firebase-admin python-dotenv
```

---

## 🔐 Configuration

Sensitive files are excluded from GitHub.

Create:

```
.env
```

Example:

```env
FIREBASE_KEY_PATH=firebase/saba_key.json
DATABASE_URL=your_firebase_database_url
MODEL_PATH=models/last.pt
```

Add your Firebase Admin SDK key:

```
firebase/saba_key.json
```

Add your Firebase Web configuration:

```
firebase-config.js
```

---

## 🤖 YOLO Model

The trained model is not included.

Place your model here:

```
models/last.pt
```

Example:

```python
model = YOLO("models/last.pt")
```

---

## 📚 Dataset Training

Dataset is not included.

Required structure:

```
dataset/
├── data.yaml
├── train/
└── valid/
```

Train model:

```python
from ultralytics import YOLO

model = YOLO("yolo11n-seg.pt")

results = model.train(
    data="dataset/data.yaml", # Dataset YAML file
    epochs=100,               # Training cycles
    imgsz=640                 # Image size
)
```

---

## ▶️ Run System

Start detection:

```bash
python Counting_firebase.py
```

The system will:

1. Open camera
2. Detect Saba bananas
3. Count objects
4. Calculate price
5. Send data to Firebase

---

## 🌐 Dashboard

Open:

```
SabaWeb.html
```

Displays:

- Current count
- Estimated price
- Total count

---

## 📊 Firebase Structure

```
saba_detection
│
├── count
├── price
└── total_count

sensor
└── distance_cm
```

---

## 🚫 Ignored Files

The following are excluded:

```
.env
firebase/*.json
firebase-config.js
*.pt
runs/
saba_counter_instance_seg-2-20250302T171218Z-001/
```

These contain private credentials, large models, or datasets.

---

## 👨‍💻 Author

**Jaycee Molina**
Computer Engineer

GitHub:
https://github.com/JayceeMolina
