**DLive Detect: Real-Time Object Detection with Deep Learning**

**Project Overview**
DLive Detect is a Flask-based web application that performs real-time object detection using the YOLOv8 model. This project aims to demonstrate the capabilities of deep learning in identifying objects accurately and efficiently in real-world scenarios.
The system leverages the YOLOv8 model to process images and videos, detect objects, and display the results via a user-friendly interface. The application can be easily extended to various practical use cases such as surveillance, autonomous systems, and more.

**Features**
Real-time object detection using YOLOv8.
User-friendly web interface built with HTML, CSS, and JavaScript.
Easy upload of images or videos for object detection.
Supports customizable configurations for detection thresholds and classes.

**File Structure**
miniproject/
├── yolo8n.pt               # YOLOv8 model weights
├── app.py                  # Flask application code
├── templates/              # HTML templates for the web interface
│   ├── index.html          # Upload page
│   └── result.html         # Results display page

**Technologies Used**
Python: Flask framework for backend development.
YOLOv8: Object detection model for identifying objects in images and videos.
HTML, CSS, JavaScript: For building the front-end web interface.

**Installation**

**Clone the Repository:**
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

**Install Dependencies:**
pip install -r requirements.txt
Add YOLO Model Weights: Place the yolo8n.pt file in the project directory.

**Run the Application:**
python app.py
Access the Web App: Open your browser and navigate to http://127.0.0.1:5000.

**How It Works**
Users upload an image or video on the index.html page.
The application processes the input using the YOLOv8 model.
Detected objects are highlighted with bounding boxes and displayed on the result.html page.

**Future Scope**
Extend support for live camera feeds.
Implement additional pre-processing and post-processing features.
Optimize detection speed for large-scale deployments.
Add multi-language support for the web interface.

**Contributors**
Your Name - Jashwanth Reddy Kolla
Email - jashwanthreddykolla@gmail.com
