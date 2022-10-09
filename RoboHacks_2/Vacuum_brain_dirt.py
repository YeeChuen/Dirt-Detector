# Author: Yee Chuen
# title: Vacumm_brain_dirt
# description: this program serve as the part of the brain for a vacuum that detects dirt

"""
constraint:
1. only works with top view image as input
2. only works with white tiles floors
"""

import os, shutil
from test_processimage import dirtdetection, checkRed, convertRedWhite
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
from test_cv2_processing import removeVH
import glob

olddir = os.getcwd()
os.chdir(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2')
curdir = os.getcwd()

newdir = curdir + "\process"
if not os.path.exists(newdir):
    os.mkdir(newdir)
os.chdir(newdir)

curimg = dirtdetection(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2\floor_image\cleanfloor.jpg')

curimg = removeVH(curimg)

print(convertRedWhite(curimg))



for filename in os.listdir(newdir):
    file_path = os.path.join(newdir, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))





