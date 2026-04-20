from ultralytics import YOLO

# This line is REQUIRED on Windows to prevent the multiprocessing crash
if __name__ == '__main__':
    
    # 1. Load the model
    model = YOLO('yolov8n.pt') 

    # 2. Train the model
    results = model.train(
        data=r"C:\Users\morar\Downloads\sign_detectionV3\data.yaml", 
        epochs=45,          
        imgsz=640,          
        batch=32,           
        name='traffic_signs_v135', 
        device=0            
    )