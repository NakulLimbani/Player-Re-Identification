# Player-Re-Identification
Assignment submission for Stealth Mode ML — Player Re-Identification.

# ⚽ Player Re-Identification — Stealth Mode ML Internship Assignment

![Tracked Players Example](https://user-images.githubusercontent.com/your-sample-image.png) <!-- Optional banner image if you want -->

---

## 🟢 Overview

This repository contains my submission for the Stealth Mode Machine Learning Internship assignment focused on **player re-identification** in soccer videos.

The task was to build a system that:
- Detects players throughout a match.
- Assigns **consistent unique IDs** to each player.
- Maintains those IDs even when players leave or re-enter the scene.
- Handles challenges such as occlusion, motion blur, and clutter.

---

## 🎥 Demo

✅ **[Download final output video with audio](final_tracked_with_audio.mp4)** — Player IDs overlayed with original commentary.

---

## 💡 Approach

### 🔎 Detection
- Used YOLOv11 (Ultralytics) model for robust player detection.
- Filtered only **players** (class index: 2) in each frame.

### 🟢 Re-Identification
- Implemented **Hungarian assignment algorithm** (global assignment) to reduce ID switching.
- Used IoU and spatial proximity as matching criteria.
- Basic tracker memory updated frame by frame.

### 🎬 Output
- Generated frame-by-frame output video with bounding boxes and assigned IDs.
- Merged final output video with **original commentary audio** using ffmpeg.

---

## 🚩 Results

- IDs mostly stable across frames.
- Occasional ID fluctuations acknowledged and explained.
- Video duration and audio match original input exactly.

---

## 🔥 Future Improvements

- Integrate **appearance embeddings** (e.g., jersey color or deep Re-ID features).
- Add motion prediction (e.g., Kalman filter).
- Use OCR to extract jersey numbers for robust ID assignment.

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
