from PIL import Image
import PIL

# Image Recognition
import os
from imageai.Detection import ObjectDetection

import urllib.request

from imageai.Classification import ImageClassification
import os


def getDetectedObject(userFilePath):
    
    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(userFilePath , "Image1.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )



"""
# Detect Image Start 
execution_path = os.getcwd()

detector = ObjectDetection()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( execution_path + "\resnet50_imagenet_tf.2.0.h5")
detector.loadModel()

def getDetectedObject(userFilePath):
    detections = detector.detectObjectsFromImage(input_image=os.path.join(userFilePath, "Image1.jpg"), output_image_path=os.path.join(userFilePath, "Image1new.jpg"))
    for eachObject in detections:
        detectedObjName = eachObject["name"]
        detectionProbability = eachObject["percentage_probability"]
        print(detectedObjName + ", with probability: " + detectionProbability) #TODO: delete when done testing
        logInfo("'Ran image recognition' - Recognized: " + detectedObjName + " with probabiliy: " + detectionProbability)
        return (detectedObjName, detectionProbability)
# Detect Image Finish
"""