# Face Recognition Project

## Project Description & Objective
This project was created to demonstrate a face recognition task to match faces given two input images. If a match is found, then it is shown as having green colored bounding box around the matched face. All the other faces are also shown having red bounding boxes and each of them have their respective distance values compared to the face to be matched. Input and output parameters are as follows:

```
Input 1: An image file containing only the face to be searched.
Input 2: Another image with a variety of different faces.
Output: The image for input 2 will be shown with all the detected faces surrounded by a bounding box. 
If a match occurs, then the matched face is shown as having a green bounding box to highlight.
```

#### Prerequisites
To successfully run the project, it is required to have the following software and their respective versions installed:
* Python 3.6 or higher (https://www.python.org/downloads/)
* Flask 1.0 or higher (http://flask.pocoo.org/)
* OpenCV library
* Numpy Library
* face_recognition Library


## How the Code Works
The project was designed to offer a web user interface that works inside the localhost. To create a simple web UI, Flask was used. The Flask project has the following structure:
```
static/images Folder: Contains the two input images as well as the output image after the script is executed.
templates Folder: Contains the HTML files for displaying different pages.
faceCompare.py File: The script to execute the web UI and perform face recognition
```
### Recognizing faces using face_recognition library


