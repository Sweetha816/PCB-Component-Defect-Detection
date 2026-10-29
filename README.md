# AI-Based PCB Defect Detection

A CPU-trained YOLOv8n prototype that localizes annotated PCB surface defects.

## Project Files
- model/best.pt: trained model weights
- app.py: image prediction demo
- results/: sample prediction image
- project_report.md: project report
- presentation.pptx: project presentation
- requirements.txt: required libraries

## Dataset
DeepPCB: https://github.com/tangsanli5201/DeepPCB

The dataset is not included in this repository. Follow the source licence and terms.

## Run the Demo
Install dependencies:
pip install -r requirements.txt

Run:
python app.py

## Limitations
The model was trained for five epochs using 800 training images and 200 validation images. The six classes are named generically until their official mapping is verified. This prototype detects annotated PCB surface defects; it does not establish reliable detection of missing or incorrectly oriented components.
