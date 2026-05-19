# 👁️ OpenCV Basic Projects

A collection of real-time **Computer Vision projects** built with Python, OpenCV, and MediaPipe — where your camera becomes the controller.

---

## 🔊 Hand Gesture Volume Control

Control your system volume using just your hand — no keyboard, no mouse needed.

The project uses **MediaPipe** to detect 21 hand landmarks in real time via webcam. It tracks the distance between your **thumb tip** and **index finger tip** and maps that to a volume command — bring fingers close to decrease volume, spread them apart to increase it. A 0.5s cooldown prevents rapid unintended jumps.

| Gesture | Action |
|---|---|
| 🤏 Fingers close | Volume Down |
| 🖐️ Fingers spread | Volume Up |

> ⚠️ Currently supports **macOS only** (uses `osascript` for volume control).

---

## 📁 Folder Structure

```
opencv-basic-projects/
│
├── volume_control.py      # Hand gesture volume controller
├── main.py                # Entry point
├── requirements.txt       # Project dependencies
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Google-orange)

| Library | Purpose |
|---|---|
| `opencv-python` | Webcam capture & real-time video display |
| `mediapipe` | Hand landmark detection (21 points) |
| `math` | Euclidean distance calculation |
| `os` | System volume commands |
| `time` | Cooldown between volume changes |

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

**3. Run the project**
```bash
python volume_control.py
```

> Press **`x`** to quit the webcam window.

---

## 📦 Requirements

```
opencv-python
mediapipe
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

⭐ **If this repo helped you, consider giving it a star — it motivates me to keep learning and sharing!**

*Made by [Mohit Jaryal](https://mohitjaryal.online)*
