# Author: Yee Chuen Teph
# title: test_processimage
# Description: test zone for processing image

import os
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

olddir = os.getcwd()
os.chdir(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2\testzone')

# get image
image = Image.open(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2\floor_image\dirt_on_floor.jpg')

# blur image
image = image.filter(ImageFilter.BoxBlur(10))
image.save('1blurtest.jpg')

# greyscale image
image = image.convert('L')
image.save('2greyscaletest.jpg')

# contrast image
image = ImageEnhance.Contrast(image).enhance(3)
image.save('3contrasttest.jpg')

# brightness image
image = ImageEnhance.Brightness(image).enhance(2)
image.save('4brigtnesstest.jpg')

# invert image color
image = ImageOps.invert(image)
image.save('5inverttest.jpg')

# sharpness image
image = ImageEnhance.Sharpness(image).enhance(100)
image.save('6sharpnesstest.jpg')

# edge detection image
image = image.filter(ImageFilter.FIND_EDGES)
image.save('7edgedetectiontest.jpg')

image.show()

os.chdir(olddir)