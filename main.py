import eel
import random
from random import randint
from datetime import datetime
from PIL import Image
import PIL

# Image Recognition Classification
from imageai.Detection import ObjectDetection
import os
import sys

import urllib.request

"""
from imageai.Classification import ImageClassification
import os
"""

from UserData import User
from CsvManager import csvFile
from csv import writer

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

os.makedirs(os.path.join('D:\BARobo\Tyr 8.0 IR\Workspace\Logs',  userIdS))
userFilePath = os.path.join('D:\BARobo\Tyr 8.0 IR\Workspace\Logs',  userIdS)
logFilePath = os.path.join(userFilePath, "Log.txt")
print("File Path: " + userFilePath) #TODO delete when done testing
print("File Path: " + logFilePath) #TODO delete when done testing
print("os File Path: " + os.getcwd())

# Create User
user = User(new_id, datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"), None, None, userFilePath, None)

# Print current instance of User Object (TODO: delete after testing)
print("\n State: \n")
user.print_instance()

# Create csv file
csv = csvFile(logFilePath)
csv.create()
csv.print_instance()
# Log csv header
csv.log(['time',
        'start',
        'action',
        'subtext here'])

# Log into csv
@eel.expose
def write_csv(action, msg, subtext):
    """
    time = getDateTimeNowString()
    csv.log([time, action, msg, subtext])
    # TODO: remove after testing
    print("\n Writing CSV Content")
    print([time, action, msg, subtext])
    """
    list_data = [action, msg, subtext]
    
    with open(logFilePath, 'a', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(list_data)  
        # Close the file object
        f_object.close()
        
    print("Action logged into Log.txt")



# Log User Interaction
"""
@eel.expose
def logInfo(action, msg):
    # Append to &/or create file
    f = open(logFilePath, "a+")
    # Write log to file
    f.write("\n" + getDateTimeNowString() + " - " + action + msg) 
    # Close file
    f.close()
"""


# Object Detection from Image
def detectFromImage():
    # TODO: uncomment after testing
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(userFilePath , "Image1.jpg"), output_image_path=os.path.join(execution_path , "Image2.jpg"))

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        detected_object_name = eachObject["name"]
        print("detected: \n" + detected_object_name)
        detection_probability = eachObject["percentage_probability"]
        # TODO: user.set_detected_object umshreiben zu user.update(welches attribute, daten)
        user.set_detected_object(detected_object_name, detection_probability)
    
    x = "None"
    if detected_object_name == x:
        print("No object detected.. TODO: handle this!")
    else:
        # TODO: Remove print outs
        print("State: \n")
        user.print_instance()

        # set twin objects image
        eel.set_image_from_detected(detected_object_name)

        # TODO: delete after testing
        print("\n State: \n")
        user.print_instance()


# Save Image capture
@eel.expose
def saveImage(img, key, fileName):
    print("\n saveImage called")
    print("\n img: " + img)
    print("\n key: " + str(key))
    print("\n filename: " + fileName)
   
    imagePath = os.path.join(userFilePath, fileName)
    imageFile = urllib.request.urlretrieve(img, imagePath)

    print("image retrieved from url" + str(imageFile))
    
    user.set_image_info(key, imagePath)
    print("user image key and path saved")
    # TODO: delete after testing
    print("\n State: \n")
    user.print_instance()
    # Run image detection
    detectFromImage()
    
    

@eel.expose
def restart_application():
    print("Restarting application")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
    
eel.init("www")
eel.start("index.html", size=(1296, 916))
