from flask import Flask, render_template, request
import cv2
from ultralytics import YOLO

app = Flask(__name__)

# Initialize YOLO model
model = YOLO("yolov8n.pt")

# Flag to indicate whether to stop detection
stop_detection_flag = False

# Function to stop object detection
def stop_object_detection():
    global stop_detection_flag
    stop_detection_flag = True

# Function to run the object detection script with stop option
def run_object_detection_with_stop():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error opening video file!")
        exit(1)

    global stop_detection_flag
    stop_detection_flag = False

    while True:
        ret, frame = cap.read()
        if not ret or stop_detection_flag:
            break

        # Uncomment to display the video frame by frame
        results = model(frame, conf=0.4, show=True)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Video reading complete!")

# Routes
@app.route('/')
def index():
    return render_template('index.html', show_stop_button=False)

@app.route('/run_detection', methods=['POST'])
def run_detection():
    run_object_detection_with_stop()
    return render_template('index.html', message='Object detection complete!', show_stop_button=True)

@app.route('/stop_detection', methods=['POST'])
def stop_detection():
    stop_object_detection()
    return "Object detection stopped!"

if __name__ == '__main__':
    app.run(debug=False)

