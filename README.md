# manufacturing-steel-defect-detection
## Project Overview

This project focuses on detecting and classifying defects on steel surfaces using Deep Learning and Computer Vision.

The project was developed in multiple stages, starting with image classification using CNN and VGG16, followed by YOLO-based object detection and finally deployment using Streamlit.

## Defect Classes

The system detects 6 types of steel surface defects:

* Crazing
* Inclusion
* Patches
* Pitted Surface
* Rolled-in Scale
* Scratches

## Project Workflow

Steel Defect Dataset
        ↓
Data Preprocessing
        ↓
Train / Validation / Test Split
        ↓
Data Augmentation
        ↓
CNN Classification
        ↓
VGG16 Transfer Learning
        ↓
Freeze VGG16 Base Model
        ↓
Fine-Tuning
        ↓
YOLO Object Detection
        ↓
Image Detection
        ↓
Video Detection
        ↓
Streamlit Deployment

## 1. Data Preprocessing

The steel surface images were prepared for Deep Learning.

Steps performed:

* Loaded images using OpenCV
* Converted images to the required color format
* Resized images
* Normalized pixel values
* Encoded the defect classes
* Prepared the dataset for model training

## 2. Train, Validation and Test Split

The dataset was divided into:

* Training set
* Validation set
* Test set

Stratified splitting was used to maintain the distribution of defect classes across the datasets.

## 3. Data Augmentation

Data augmentation was applied to the training images to improve model generalization.

The augmentation process introduced variations such as:

* Rotation
* Zoom
* Shifting
* Flipping

This helps the model learn more robust visual features.

## 4. CNN Classification

A Sequential CNN model was initially developed to classify steel surface defects.

The CNN learns important image features such as:

* Edges
* Textures
* Shapes
* Surface patterns

The final classification layer predicts one of the six defect classes.

## 5. VGG16 Transfer Learning

VGG16 pretrained on ImageNet was used to improve the classification model.

The pretrained VGG16 network was used as the base model for extracting visual features.

Initially, the VGG16 base model was frozen and a custom classification head was added.

VGG16 Base Model
       ↓
Flatten
       ↓
Dense Layer
       ↓
Softmax Output
       ↓
6 Defect Classes

## 6. Fine-Tuning

After transfer learning, selected layers of the VGG16 network were unfrozen.

The model was then fine-tuned using the steel defect dataset.

Fine-tuning allows the pretrained network to learn features that are more specific to steel surface defects.

## 7. YOLO Object Detection

After classification, YOLO was used to perform object detection.

Unlike image classification, YOLO can identify both:

* What type of defect is present
* Where the defect is located

Steel Image
     ↓
YOLO
     ↓
Defect Detection
     ↓
Bounding Box
     ↓
Defect Name
     ↓
Confidence Score

The trained YOLO model is stored as:

steel_defect_best.pt

## 8. Image Detection

The YOLO model can process steel surface images and display:

* Bounding boxes
* Defect names
* Confidence scores

This allows the location of defects on the steel surface to be visually identified.

## 9. Video Detection

The YOLO model is also used for video-based defect inspection.

The video is processed frame by frame.

Steel Inspection Video
        ↓
Video Frames
        ↓
YOLO Detection
        ↓
Bounding Boxes
        ↓
Defect Names
        ↓
Processed Video

This enables continuous detection of defects throughout the inspection video.

## 10. Streamlit Deployment

A Streamlit web application was developed to provide an easy interface for the trained YOLO model.

Users can upload:

* Steel defect images
* Steel inspection videos

The application performs detection and displays the results with bounding boxes, defect names, and confidence scores.

## Technologies Used

* Python
* TensorFlow / Keras
* CNN
* VGG16
* YOLO
* PyTorch
* OpenCV
* NumPy
* Pillow
* Streamlit
* 
## Project Structure
manufacturing-steel-defect-detection/
│
├── app.py
├── steel_defect_best.pt
├── requirements.txt
└── README.md

## How to Run Locally

Install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

The application will open in the browser and allow image or video upload for steel defect detection.

## Key Features

* Steel surface defect classification
* CNN-based classification
* VGG16 transfer learning
* VGG16 fine-tuning
* YOLO object detection
* Defect localization using bounding boxes
* Image detection
* Video detection
* Streamlit web application
* Web-based deployment


## Results

The developed system successfully progresses from traditional CNN-based image classification to VGG16 transfer learning and fine-tuning, followed by YOLO-based object detection.

The final system is capable of:

* Classifying steel surface defects
* Detecting multiple defects in an image
* Localizing defects using bounding boxes
* Processing inspection videos frame by frame
* Displaying predictions through a Streamlit interface

## Conclusion

This project demonstrates an end-to-end **Computer Vision pipeline for automated steel surface defect inspection**.

The project starts with CNN-based image classification, progresses to **VGG16 Transfer Learning and Fine-Tuning**, and finally uses **YOLO Object Detection** to locate defects in images and videos.

The trained detection model is integrated into a **Streamlit application**, providing a practical interface for automated steel quality inspection.
