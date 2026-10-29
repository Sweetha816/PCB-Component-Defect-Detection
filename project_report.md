# Project Report
## AI-Based Component Placement Error Detection in PCB Assembly

### Abstract
This project uses a lightweight YOLOv8n object detector to localize defects annotated in PCB images.

### Dataset
- Source: DeepPCB public dataset
- Training pairs prepared: 1,000
- Training images: 800
- Validation images: 200
- Training epochs: 5
- Training device: CPU
- Image size: 416 x 416

### Methodology
PCB images and bounding-box annotations were prepared in YOLO format. A pretrained YOLOv8n model was fine-tuned, evaluated, and used to generate sample predictions.

### Evaluation
Precision: 0.7951
Recall: 0.7303
mAP50: 0.8066
mAP50-95: 0.4854


### Demonstration
The app.py file provides a PCB image-upload interface and returns an annotated image with predicted boxes.

### Limitations
DeepPCB annotations describe PCB surface defects. They do not by themselves validate missing-component or wrong-orientation detection. The six model classes remain generic until the official class mapping is verified. Five epochs represent a prototype, not production-ready performance.

### Future Work
Verify class names, improve training, report per-class metrics and confusion matrix, and add validated reference-board comparison for component-placement errors.

### Reference
https://github.com/tangsanli5201/DeepPCB
