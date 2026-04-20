import cv2
from ultralytics import YOLO

# 1. Load your model
model_path = r"C:\Users\morar\Downloads\sign_detectionV3\sign_detectionV3\best.pt"
my_model = YOLO(model_path)

conf_threshold = 0.50 

cap = cv2.VideoCapture(0)

print("--- CONTROLS ---")
print("W or UP ARROW:    Increase Threshold (+10%)")
print("S or DOWN ARROW:  Decrease Threshold (-10%)")
print("'q':              Quit")
print("----------------")

while True:
    success, frame = cap.read()
    if not success:
        break

    results = my_model.predict(source=frame, imgsz=1280, conf=conf_threshold)

    annotated_frame = results[0].plot()

    cv2.putText(
        annotated_frame, 
        f"Threshold: {int(conf_threshold * 100)}%", 
        (20, 50), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        1, (0, 255, 0), 2
    )

    cv2.imshow("Live Traffic Sign Detection", annotated_frame)

    # 6. Listen for key presses
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    
    # Check for 'w' or Up Arrow (Windows specific code 82)
    elif key == ord('w') or key == 82: 
        conf_threshold = min(1.0, conf_threshold + 0.10)
        print(f"Threshold increased to: {conf_threshold:.2f}")
        
    # Check for 's' or Down Arrow (Windows specific code 84)
    elif key == ord('s') or key == 84: 
        conf_threshold = max(0.01, conf_threshold - 0.10)
        print(f"Threshold decreased to: {conf_threshold:.2f}")

cap.release()
cv2.destroyAllWindows()