#### FACE COMPARISON PROJECT ####
#### BY: CAN OZCIVELEK       ####
#### ON: 23/06/2019          ####

#### Importing necessary libraries
from flask import Flask, render_template, request, url_for
import os
import cv2
import numpy as np
import face_recognition


app = Flask(__name__)

#### Defining home route displaying index.html
@app.route("/")
def home():
    return render_template('index.html')


#### Defining folder paths to images
IMAGES_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER

#### Defining Upload method to take 2 images as inputs and
#### process them to see if there's a match.
@app.route("/", methods=['GET', 'POST'])
def upload():
    #### Two text fields to take two image inputs
    text1 = request.form['path1']
    text2 = request.form['path2']

    #### Defining full file path and names
    full_filename1 = os.path.join(app.config['UPLOAD_FOLDER'], text1)
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], text2)
    full_filename3 = os.path.join(app.config['UPLOAD_FOLDER'], 'final.jpg')

    known_image = cv2.imread(full_filename1)
    unknown_image = cv2.imread(full_filename2)

    #### Using face_recognition library to encode faces and define face locations
    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    face_locations = face_recognition.face_locations(unknown_image)
    face_distances = face_recognition.face_distance([known_encoding], unknown_encoding)

    print("Faces are being compared...")

    #### For each detected face, draw a bounding box
    for (top, right, bottom, left), face_encoding in zip(face_locations, known_encoding):

        for i, face_distance in enumerate(face_distances):
            print("Face distance: {:.2}".format(face_distance))

        #### Compare faces
        matches = face_recognition.compare_faces([known_encoding], unknown_encoding)

        #### Calculate face distances based on their facial landmark values
        #### The distance is based on euclidean distance
        face_distances = face_recognition.face_distance([known_encoding], face_encoding)
        #### Define best match index based on the closest match (least distant)
        best_match_index = np.argmin(face_distances)
        #### Define bm variable to hold the distance value
        bm = np.min(face_distances)

        #### Draw rectangles around faces
        cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 0, 255), 3)

        #### Add a label inside each box and show the distance values
        cv2.rectangle(unknown_image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(unknown_image, "{:.2}".format(face_distance), (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


    bmi = face_locations[best_match_index]
    x1 = bmi[3]
    x2 = bmi[1]
    y1 = bmi[0]
    y2 = bmi[2]

    #### If a match is found, then print a message and draw a green colored
    #### bounding box around the mathced face
    if matches[0] == True:
        print("It's a match!")

        if matches[best_match_index]:
            # Draw a bounding box for the matched face
            cv2.rectangle(unknown_image, (x1, y1), (x2, y2), (0, 255, 0), 3)

    else:
        print("Couldn't find a match!")

    #### Save the final image inside the static/images path
    cv2.imwrite(IMAGES_FOLDER + '/final.jpg', unknown_image)

    #### Show the face being searched and the final image after processing
    return render_template("index.html", user_image1 = full_filename1,
                                         user_image2 = full_filename3)





if __name__ == '__main__':
    app.run(debug=True)
