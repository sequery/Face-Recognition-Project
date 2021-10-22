# Face Recognition

Face Recognition using OpenCV in Python

### Prerequisites

Numpy</br>
OpenCV

#### Note: Please install opencv-contrib-python package instead of opencv-contrib as it contains the main modules and also contrib modules.

## Running the tests

Run train.py script on commandline to train recognizer on training images and also predict test_img:<br>
##### python train.py
1.Place some test images in trainImages folder that you want to predict in train.py file</br>
2.Place Images for training the classifier in trainingImages folder. If you want to train clasifier to recognize multiple people then add each persons folder in separate label markes as 0, 1, 2, etc. and then add their names along with labels in train.py/main.py file in 'name' variable.</br>
3.To generate test images for training classifier use imageconverter.py file.</br>
4.To do test run via train.py give the path of image in test_img variable</br>
5.Use "main.py" script for predicting faces realtime via your webcam. (But ensure that you run train.py first since it generates training.yml file that is being used in "main.py" script.