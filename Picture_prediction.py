import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("models/last.pt")

# Images for prediction
image_paths = ["test_images/4.jpg"]

# Run prediction
results = model.predict(source=image_paths,project="predictions",name="prediction",save=True,show=True,conf=0.3)

# Keep window open
cv2.waitKey(0)