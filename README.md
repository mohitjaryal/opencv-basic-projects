# 👁️ OpenCV Basic Projects

A collection of real-time **Computer Vision projects** built with Python, OpenCV, and MediaPipe — where your camera becomes the controller.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Google-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📁 Projects

### 🔊 1. Hand Gesture Volume Control
> `volume_control.py`

Control your system volume using just your hand — no keyboard, no mouse needed.

Uses **MediaPipe** to detect 21 hand landmarks in real time. Tracks the distance between your **thumb tip** and **index finger tip** and maps it to system volume — bring fingers close to decrease, spread them to increase. A 0.5s cooldown prevents rapid unintended jumps.

| Gesture | Action |
|---|---|
| 🤏 Fingers close | Volume Down |
| 🖐️ Fingers spread | Volume Up |

> ⚠️ Currently supports **macOS only** (uses `osascript` for volume control).

---

### 🖱️ 2. Hand Gesture Mouse Control
> `mouse_control.py`

Control your mouse cursor and clicks using hand gestures — completely touchless.

Uses **MediaPipe** hand tracking + **PyAutoGUI** to map your hand position to screen coordinates in real time.

| Gesture | Action |
|---|---|
| ☝️ Index finger up | Move cursor |
| 🤏 Pinch (thumb + index) | Left click |
| ✌️ Two fingers up | Right click / Scroll |

---

### 😊 3. Face, Eye & Smile Detection
> `face_eye_smile.py`

Real-time detection of faces, eyes, and smiles using OpenCV's Haar Cascade classifiers.

Draws bounding boxes around detected faces and overlays markers for eyes and smiles — great for understanding classical CV before diving into deep learning.

| Detected | Highlight |
|---|---|
| 👤 Face | Blue rectangle |
| 👁️ Eyes | Green rectangle |
| 😄 Smile | Red rectangle |

---

### 🚨 4. Motion Detector
> `motion_detector.py`

A lightweight real-time motion detector using frame differencing.

Compares consecutive webcam frames to detect movement — highlights motion zones with bounding boxes and optionally triggers an alert.

| Feature | Detail |
|---|---|
| 📸 Frame differencing | Detects pixel-level changes |
| 🟥 Bounding box | Highlights motion regions |
| ⏱️ Sensitivity control | Adjustable threshold |

---
Tumhara matlab hai — face detection wale project ke liye bhi aisa hi README section likhun? Jaise:

---

### 👤 5. Face Detection System
> `face_detection.py`

Detects faces, eyes in real-time using your webcam — completely automatic.
Uses **OpenCV** Haar Cascades to detect and highlight faces and eyes with bounding boxes.

| Feature | Detail |
|---|---|
| 👤 Face Detection | Green rectangle around face |
| 👁️ Eye Detection | Blue rectangle around eyes |
| 🔴 Label | "Face Detected" text above box |
| ❌ Exit | Press `x` to quit |

---
## 📂 Folder Structure

```
opencv-basic-projects/
│
├── volume_control.py      # Hand gesture volume controller
├── mouse_control.py       # Hand gesture mouse controller
├── face_eye_smile.py      # Face, eye & smile detector
├── motion_detector.py     # Real-time motion detector
├── face_detection.py      # Real-time face detector
├── requirements.txt       # Project dependencies
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `opencv-python` | Webcam capture & real-time video display |
| `mediapipe` | Hand & face landmark detection |
| `pyautogui` | Mouse and keyboard control |
| `math` | Euclidean distance calculations |
| `time` | Cooldown & frame timing |

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/mohitjaryal/opencv-basic-projects.git
cd opencv-basic-projects
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run any project**
```bash
python volume_control.py
# or
python mouse_control.py
# or
python face_eye_smile.py
# or
python motion_detector.py
```

> Press **`x`** or **`q`** to quit the webcam window.

---

## 📦 Requirements

```
opencv-python
mediapipe
pyautogui
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 📬 Connect with Me

| Platform | Link |
| --- | --- |
| 🌐 Website | [mohitjaryal.online](https://mohitjaryal.online) |
| 💼 LinkedIn | [in/mohitjaryal](https://www.linkedin.com/in/mohitjaryal) |
| 🐦 Twitter/X | [@mohitjaryal04](https://x.com/mohitjaryal04) |
| 💻 GitHub | [mohitjaryal](https://github.com/mohitjaryal) |
| 🧩 LeetCode | [mohitjaryal](https://leetcode.com/u/mohitjaryal) |
| 🧩 HackerRank | [mohitjaryal](https://hackerrank.com/u/mohitjaryal) |

---

⭐ **Star this repo if it helped you — it keeps me motivated to build and share more!**

*Made with ❤️ by [Mohit Jaryal](https://mohitjaryal.online)*
