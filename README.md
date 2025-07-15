# ⚽️ Player Re-Identification from Single Broadcast Feed — Stealth Mode ML

![Football Tracking](https://img.shields.io/badge/Player%20Tracking-Complete-green)

---

## 🟢 Overview
This project implements an end-to-end **player detection and re-identification system** on a single broadcast feed of a football match.

The system:
- Detects players in every frame.
- Assigns **unique IDs** and keeps them consistent as players move, leave, or re-enter.
- Handles occlusion, motion blur, and crowded formations.
- Produces a final video with **original commentary audio preserved**.

---

## 🎬 Demo

✅ **[Download final output video with audio](tracked_output_final_nuanced_15sec_output_720p_with_audio.mp4)** — IDs overlayed on players, original commentary included.

---

## 💡 Approach

### 🔎 Detection
- Used YOLOv11 (Ultralytics) for robust player detection.
- Filtered players only (class index `2`).

### 🟢 Re-Identification
- Used IoU-based ID assignment logic.
- Frame-by-frame memory update to reduce ID switching.

### 🎬 Output
- Overlay bounding boxes and IDs on each frame.
- Final video exported and original commentary audio merged using ffmpeg.

---

## 💾 Download model weights

The YOLOv11 model checkpoint is large (>100 MB) and is not included directly in this repo.

▶️ **[Download best.pt from Google Drive](https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view)**

After downloading, place it into the project root directory and update:

```python
MODEL_PATH = "best.pt"
```
---

🛠️ Setup
💻 Virtual environment (recommended)

```python
git clone https://github.com/NakulLimbani/Player-Re-Identification.git
cd Player-Re-Identification

# Create virtual environment
python -m venv venv

# Activate
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
---

▶️ Running

🟢 Notebook (step-by-step)
Open and run Player_Re_Identification_Single_Feed.ipynb in Jupyter or Colab to explore each step interactively.

⚡ Python script (direct)
Run main.py to execute full pipeline, including video generation and audio merging.

```python
python main.py
```
---

🗂️ Repository structure
```
├── 15sec_input_720p.mp4
├── tracked_output_final_nuanced_15sec_output_720p_with_audio.mp4
├── Player_Re_Identification_Single_Feed.ipynb
├── main.py
├── README.md
├── requirements.txt
└── archive/
    ├── tracked_output_approach_1_e2e.mp4
    ├── tracked_output_enhanced_approach_2_e2e.mp4
    └── tracked_output_final_nuanced_15sec_output_720p_no_audio.mp4

💬 Note: archive/ contains intermediate outputs for reference.
```
---

🗣️ Audio preservation

Final output video keeps the original commentary, providing a realistic viewing experience.

---

🔥 Future improvements

. Use appearance embeddings (e.g., jersey color) for stronger ID consistency.

. Integrate motion prediction (e.g., Kalman filter).

. OCR-based jersey number recognition.

---

✅ Deliverables summary

. Robust player detection and tracking logic.

. Consistent ID assignment demonstrated visually.

. Final video with commentary audio.

. Notebook and standalone script provided.

. Virtual environment instructions and minimal dependencies.

---

💬 Contact

👤 Nakul Limbani

✉️ Email: nakulramesh2@gmail.com | nl0027@srmist.edu.in

💼 LinkedIn ![LinkedIn](www.linkedin.com/in/nakul-limbani) 

💻 ![GitHub](https://github.com/NakulLimbani)

⚽️ Thank you for reviewing — enjoy tracking!

---

