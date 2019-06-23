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
face_recognition library was created by Adam Geitgey and offers methods to recognize or manipulate faces. It is built using dlib's recognition methods also using deep learning. The performance is rated at 99.38% accuracy on the Labeled Faces in the Wild benchmark. The project starts by importing relevant libraries followed by defining a method to return index.html which is basically the homepage. After that, a variable called IMAGES_FOLDER is defined to hold the path to the input images (/script/images/). Later, the method upload() is defined. This is where the images are uploaded and processed to finally return the resulting image. 2 textfields are placed to take file inputs. The user must enter a valid image name that already exists inside the scripts/images directory. As previously stated, the first textfield should take an image to be searched, the second one should take another image to perform searching. Once the inputs are entered, the [submit button](Screenshots/project_ss1.jpg) is clicked to trigger the method to perform recognition.

#### Face Comparison
Making use of the face_encodings() function provided by the face_recognition library, both input images are processed to store each detected face's encodings inside a list. Face locations (coordinates) and distances are also stored on separate lists to be later used. Then a for loop is constructed to iterate through each detected face within the second input image (where the search is taking place) and a match variable is created to store the closest match. By default, a match is found if the distance between two faces is below 0.6. But it can be tweaked to be more or less sensitive. The distance is calculated based on the facial landmarks. Facial landmarks are very important when it comes to facial recognition or manipulation operations. Simply put, facial landmarks are specific points on a face such as the eyes, nose, lips, chin etc. When we have such specific features, it becomes easy to compare them against one another. And the distance variable holds the euclidian distance between two compared faces. If that distance is less then the specified value (in this case 0.6) then a match is found. best_match_index holds the index of the closest matched face and bm variable would hold that distance value. All detected faces are then surrounded by red bounding boxes with their distance values labeled. After that, the best matched face's location is determined to enable that face to be highlited in green. Finally, the resulting image is saved inside the script/images folder via cv2.imwrite() function as "final.jpg" and it's [shown](Screenshots/project_ss2.jpg) after the Submit button is clicked.

![alt text](https://github.com/canozcivelek/face-recognition/blob/master/Screenshots/landmarks.jpeg)
_Facial Landmarks_


