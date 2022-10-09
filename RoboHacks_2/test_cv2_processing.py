# Author: Yee Chuen Teoh
# title: test_cv2_processing
# description: test zone for learning opencv on pyton for processing image

import cv2
import numpy as np
import os


def removeVH(file):
    image = cv2.imread(file)
    image = cv2.resize(image, (540, 540))   
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Remove horizontal
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,1))
    detected_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(image, [c], -1, (255,255,255), 2)

    # Test Remove Vertical
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,25))
    detected_lines2 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
    cnts = cv2.findContours(detected_lines2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(image, [c], -1, (255,255,255), 2)

    # Repair the image
    #repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,6))
    #result = 255 - cv2.morphologyEx(255 - image, cv2.MORPH_CLOSE, repair_kernel, iterations=1)

    # below shows the image, change the second image word

    number = 0
    imagename = 'process2.'+str(number)+'.jpg'
    while os.path.exists(imagename):
        number+=1
        imagename = 'process2.'+str(number)+'.jpg'

    cv2.imwrite(imagename,image)

    return(imagename)



#image = removeVH(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2\floor_image\4brigtnesstest.jpg')
#cv2.imwrite('filename.jpg',image)