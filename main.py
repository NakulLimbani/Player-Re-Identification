import cv2
import torch
import numpy as np
import os
import shutil

# ========================
# CONFIG
# ========================
INPUT_VIDEO = "15sec_input_720p.mp4"
OUTPUT_VIDEO = "tracked_output_final_nuanced_15sec_output_720p_no_audio.mp4"
OUTPUT_VIDEO_WITH_AUDIO = "tracked_output_final_nuanced_15sec_output_720p_with_audio.mp4"
MODEL_PATH = "best.pt"  # Update if needed

# ========================
# LOAD MODEL
# ========================
model = torch.hub.load("ultralytics/yolov5", "custom", path=MODEL_PATH, force_reload=True)
model.conf = 0.3  # Confidence threshold

# ========================
# VIDEO SETUP
# ========================
cap = cv2.VideoCapture(INPUT_VIDEO)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (frame_width, frame_height))
print(f"VideoWriter opened: {out.isOpened()}")

tracker_memory = {}
next_id = 1

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]
    boxes = results.boxes

    current_detections = []
    for box in boxes:
        cls = int(box.cls)
        if cls == 2:  # Your player class
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            current_detections.append([x1, y1, x2, y2])

    current_ids = []
    assigned_ids = set()

    for det in current_detections:
        best_iou = 0
        best_id = None
        for id_, prev_box in tracker_memory.items():
            ix1 = max(det[0], prev_box[0])
            iy1 = max(det[1], prev_box[1])
            ix2 = min(det[2], prev_box[2])
            iy2 = min(det[3], prev_box[3])
            inter_area = max(0, ix2 - ix1) * max(0, iy2 - iy1)
            det_area = (det[2] - det[0]) * (det[3] - det[1])
            prev_area = (prev_box[2] - prev_box[0]) * (prev_box[3] - prev_box[1])
            union_area = det_area + prev_area - inter_area
            iou = inter_area / union_area if union_area > 0 else 0

            if iou > best_iou and iou > 0.3:
                best_iou = iou
                best_id = id_

        if best_id is not None and best_id not in assigned_ids:
            current_ids.append(best_id)
            assigned_ids.add(best_id)
            tracker_memory[best_id] = det
        else:
            current_ids.append(next_id)
            tracker_memory[next_id] = det
            next_id += 1

    for det, id_ in zip(current_detections, current_ids):
        x1, y1, x2, y2 = det
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID {id_}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    out.write(frame)

cap.release()
out.release()
print("Basic tracked video saved without audio.")

# ========================
# MERGE AUDIO BACK
# ========================
os.system(f"ffmpeg -y -i {OUTPUT_VIDEO} -i {INPUT_VIDEO} -c copy -map 0:v:0 -map 1:a:0 {OUTPUT_VIDEO_WITH_AUDIO}")
print(f"Final video with audio saved to {OUTPUT_VIDEO_WITH_AUDIO}")

