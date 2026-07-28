import cv2
import firebase_admin
from firebase_admin import credentials, db
from ultralytics import YOLO
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

firebase_key = os.getenv("FIREBASE_KEY_PATH")
database_url = os.getenv("DATABASE_URL")

cred = credentials.Certificate(firebase_key)

firebase_admin.initialize_app(cred, {
    "databaseURL": database_url
})

model_path = os.getenv("MODEL_PATH")

model = YOLO(model_path)

cap = cv2.VideoCapture(0)

total_count = 0
distance_cm = 100
object_detected_time = None
object_saved = False

def reset_total_count(event):
    global total_count

    if event.data == 0:
        total_count = 0
        print("🔄 Total count reset by frontend!")

db.reference("saba_detection/total_count").listen(reset_total_count)

def update_distance(event):
    global distance_cm
    global object_detected_time
    global object_saved

    if event.data is not None:

        new_distance = float(event.data)

        # Object enters detection range
        if new_distance < 21 and distance_cm >= 21:
            object_detected_time = time.time()
            object_saved = False

        # Object leaves detection range
        elif new_distance >= 21:
            object_detected_time = None
            object_saved = False

        distance_cm = new_distance

        print(f"📏 Distance updated: {distance_cm} cm")

db.reference("sensor/distance_cm").listen(update_distance)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # YOLO inference
        results = model.predict(frame,conf=0.3)

        # Count detected saba
        num_objects = len(results[0].boxes)

        # Calculate price
        price = total_count * 2

        # Update Firebase realtime values
        db.reference("saba_detection/count").set(num_objects)
        db.reference("saba_detection/price").set(price)

        # Save total count once after 3 seconds
        if object_detected_time is not None and not object_saved:

            elapsed_time = time.time() - object_detected_time

            if elapsed_time >= 3:

                total_count += num_objects

                db.reference("saba_detection/total_count").set(total_count)
                print(f"✅ Saved {num_objects} saba "f"(Total: {total_count})")
                object_saved = True

        # Draw YOLO results
        annotated_frame = results[0].plot()

        # Display information
        cv2.putText(annotated_frame,f"Saba: {num_objects}",(50, 50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.putText(annotated_frame,f"Price: PHP {price}",(50, 90),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.putText(annotated_frame,f"Total Count: {total_count}",(50,130),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.putText(annotated_frame,f"Distance: {distance_cm:.1f} cm",(50,170),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

        # Show camera
        cv2.imshow("YOLO Saba Counting",annotated_frame)

        # Exit using Q
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    else:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()