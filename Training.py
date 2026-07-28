from ultralytics import YOLO

# Load YOLO segmentation model
model = YOLO("your_model.pt")

# Train model using dataset configuration
results = model.train(data="dataset/data.yaml",epochs=100,imgsz=640)# Dataset configuration file (classes, paths, labels), Number of training cycles, Image size used during training