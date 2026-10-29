
import gradio as gr
from ultralytics import YOLO

model = YOLO("model/best.pt")

def predict(image, confidence):
    if image is None:
        return None, "Please upload a PCB image."

    result = model.predict(
        source=image,
        imgsz=416,
        conf=confidence,
        device="cpu",
        verbose=False
    )[0]

    annotated = result.plot()[:, :, ::-1]
    counts = {}

    for cls_id in result.boxes.cls.tolist():
        name = result.names.get(int(cls_id), f"class_{int(cls_id)}")
        counts[name] = counts.get(name, 0) + 1

    summary = f"Detected boxes: {len(result.boxes)}"
    for name, count in counts.items():
        summary += f"\n{name}: {count}"

    return annotated, summary

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Image(type="numpy", label="Upload PCB Image"),
        gr.Slider(0.1, 0.9, value=0.25, step=0.05,
                  label="Confidence Threshold")
    ],
    outputs=[
        gr.Image(label="Annotated Prediction"),
        gr.Textbox(label="Detection Results")
    ],
    title="PCB Surface Defect Detection",
    description="Prototype trained on DeepPCB surface-defect annotations."
)

if __name__ == "__main__":
    demo.launch()
