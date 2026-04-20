# romanian-traffic-sign-detector
A real-time Romanian traffic sign detector built with YOLOv8 and OpenCV. It features live webcam inference, dynamic confidence threshold adjustment via keyboard, and agnostic NMS to resolve overlapping boxes. Designed for high-FPS performance on CUDA-enabled GPUs, this project provides a clean, robust foundation for intelligent traffic tracking.

##  Features
* **Real-Time Detection:** Processes live webcam feeds at high FPS using CUDA optimization.
* **Dynamic Confidence Thresholding:** Adjust the strictness of the AI on the fly using keyboard controls (`W` to increase, `S` to decrease).
* **Agnostic Non-Maximum Suppression (NMS):** Automatically resolves overlapping bounding boxes to prevent duplicate detections.
* **Custom Trained:** Fine-tuned on a comprehensive GTSRB-style dataset adapted for object detection.

##  Prerequisites
To run this project, you need a CUDA-enabled GPU (developed and tested on an NVIDIA RTX 4060 Ti) and Python 3.8+.




