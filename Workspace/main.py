import eel
import random
from random import randint
from datetime import datetime
from PIL import Image
import PIL

# Image Recognition Classification
from imageai.Detection import ObjectDetection
import os

import urllib.request

"""
from imageai.Classification import ImageClassification
import os
"""

from UserData import User
from CsvManager import csvFile

# Current Time
def getDateTimeNowString():
    dtN = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return dtN


# Testing
def testOut(x):
    print(x)

# Create random id
new_id = random.randint(0, 20000)
userIdS = str(new_id)

# Create User Directory
"""
os.makedirs(os.path.join('D:\BARobo\Tyr 8.0 IR\Workspace\Logs',  userIdS))
userFilePath = os.path.join('D:\BARobo\Tyr 8.0 IR\Workspace\Logs',  userIdS)
logFilePath = os.path.join(userFilePath, "Log.txt")
"""
userFilePath = 'D:/BARobo/Tyr 8.0 IR/Workspace/Logs/testUser'
logFilePath = 'D:/BARobo/Tyr 8.0 IR/Workspace/Logs/testUser/Log.txt'
print("File Path: " + userFilePath) #TODO delete when done testing
print("File Path: " + logFilePath) #TODO delete when done testing

# Create User
user = User(new_id, datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"), None, None, userFilePath, None)

# Print current instance of User Object (TODO: delete after testing)
user.print_instance()

# Create csv file
csv = csvFile(logFilePath)
csv.create()
csv.print_instance()
csv.log([datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"),
        'logged file',
        'testing if logging works',
        'subtext here'])


# Log User Interaction
@eel.expose
def logInfo(msg):
    # Append to &/or create file
    f = open(logFilePath, "a+")
    # Write log to file
    f.write("\n" + getDateTimeNowString() + " - " + msg) 
    # Close file
    f.close()
    testOut("LOGG: " + str(msg))

logInfo("Running - " + userIdS)


# Object Detection

def detectFromImage():
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        detectedObjName = eachObject["name"]
        detectionProbability = eachObject["percentage_probability"]
        print(detectedObjName, detectionProbability)
        user.set_detected_object(detectedObjName, detectionProbability)
        eel.set_image_from_detected(detectedObjName)
        user.print_instance()
    return (detectedObjName, detectionProbability)


# Save Image capture
@eel.expose
def saveImage(img, key, name):
    imagePath = os.path.join(userFilePath, name)
    imageFile = urllib.request.urlretrieve(img, imagePath)
    user.set_image(key, imagePath)
    user.print_instance()
    detectFromImage()
    obj = user.get_detected_object('name')
    print(obj)
    eel.set_image_from_detected()
    eel.set_capture_next_page()
    
@eel.expose
def set_images():
    eel.set_image_from_detected()
    eel.set_capture_next_page()
    print("eel called 1")
    
@eel.expose
def get_name_from_detected():
    object_name = user.get_detected_object('name')
    print("eel called 2")
    return object_name

@eel.expose
def get_image_capture():
    image_captured = user.get_image(1.1)
    print("eel called 3")
    return image_captured
    

eel.init("www")
eel.start("index.html", size=(1280, 800))
