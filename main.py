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

user = User(None, None, None, None, None, None, None)
print("os file path:  " + os.getcwd())
logFolderPath = os.path.join(os.getcwd(), 'Logs')
print("log folderpath:  " + logFolderPath)

@eel.expose
def start():
    print("Starting application")
    # Create random id
    new_id = random.randint(0, 20000)
    userIdS = str(new_id)
    # Create paths
    os.makedirs(os.path.join(logFolderPath, userIdS))
    userFilePath = os.path.join(logFolderPath, userIdS)
    print("user file path:  " + userFilePath)
    logFilePath = os.path.join(userFilePath, 'Log.txt')
    print("log file path:  " + logFilePath)
    # Set user data
    user.set_user_id(userIdS)
    user.set_start_time(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
    user.set_file_path(userFilePath)
    user.set_log_file_path(logFilePath)
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
    

# Current Time
def getDateTimeNowString():
    dtN = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return dtN


# Testing
def testOut(x):
    print(x)



# Log into csv
@eel.expose
def write_csv(action, msg, subtext):
    list_data = [action, msg, subtext]
    print("writing csv into:   " + user.get_log_file_path())
    
   
    with open(user.get_log_file_path(), 'a', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(list_data)  
        # Close the file object
        f_object.close()
        
    print("Log.txt logged")



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
    detections = detector.detectObjectsFromImage(input_image=os.path.join(user.get_file_path(), "Image1.jpg"), output_image_path=os.path.join(user.get_file_path() , "Image2.jpg"))

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
"""
from imageai.Classification import ImageClassification
# Object Detection from Image
def detectFromImage():

    execution_path = os.getcwd()

    prediction = ImageClassification()
    prediction.setModelTypeAsMobileNetV2()
    prediction.setModelPath(os.path.join(execution_path, "mobilenet_v2.h5"))
    prediction.loadModel()

    predictions, probabilities = prediction.classifyImage(os.path.join(user.get_file_path(), "Image1.jpg"), result_count=1 )
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)
        detected_object_name = eachPrediction
        print(eachPrediction)
        user.set_detected_object(detected_object_name, "80%")

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
def saveImage(img, key, fileName, detect_or_not):
    print("\n saveImage called")
    print("\n img: " + img)
    print("\n key: " + str(key))
    print("\n filename: " + fileName)
   
    imagePath = os.path.join(user.get_file_path(), fileName)
    imageFile = urllib.request.urlretrieve(img, imagePath)

    print("image retrieved from url" + str(imageFile))
    
    user.set_image_info(key, imagePath)
    print("user image key and path saved")
    # TODO: delete after testing
    print("\n State: \n")
    user.print_instance()
    # Run image detection
    if detect_or_not == "True":
        detectFromImage()
    else:
        print("second image captured, no detection done")
    

    
eel.init("www")
eel.start("index.html", mode=None, host="0.0.0.0", port=7001,shutdown_delay=100)
