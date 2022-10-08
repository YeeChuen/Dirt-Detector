# Author: Yee Chuen Teoh
# title: test image input
# description: a test file to learn how to take image as input to do stuff with the image

import os
from PIL import Image, ImageFilter, ImageEnhance    

#_____________________________________________________________________________________________________
#directory manipulation

#check directory
olddir = os.getcwd()
print("current directory: " +olddir)

#imagine using the python code directory
os.chdir(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2')
#current directory is the directory the python code file is stored
#will be used for future after processing image
#new processed image will be stored in a new created folder within this folder
curdir = os.getcwd()
print("directory of image processing program: " +curdir)

#_____________________________________________________________________________________________________
# open image, image information

#take the image from whatever directory it is from
#--> below
#img  = Image.open(path)     
# On successful execution of this statement,
# an object of Image type is returned and stored in img variable)
image = Image.open(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2\floor_image\dirt_on_floor.jpg')
# Use the above statement within try block, as it can 
# raise an IOError if file cannot be found, 
# or image cannot be opened.



#now img onject has the image stored,
#use function below to open image
#--> 
#image.show()

#available image information
# The file format of the source file.
print(image.format)

# The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
print(image.mode)

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(image.size)

# Colour palette table, if any.
print(image.palette)

#below saves the image
#-->
#image.save('new_image.png')


#_____________________________________________________________________________________________________
# Grey Scale

#create a new folder to save first process
newdir = curdir + "\process1"

#check if new directory exists
if not os.path.exists(newdir):
    os.mkdir(newdir)

#change directory to the new directory, and save the image there
os.chdir(newdir)

#make edit on the image and sace
greyscale_image = image.convert('L')
greyscale_image.save('greyscale_image.jpg')


#_____________________________________________________________________________________________________
# Edge detection

#create a new folder to save Second process
newdir = curdir + "\process2"

#check if new directory exists
if not os.path.exists(newdir):
    os.mkdir(newdir)

#change directory to the new directory, and save the image there
os.chdir(newdir)

# Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
Edge_image = image.filter(ImageFilter.FIND_EDGES)
# Saving the Image Under the name Edge_Sample.png
Edge_image.save('Edge_image.jpg')

#_____________________________________________________________________________________________________
# Blur image

#create a new folder to save Third process
newdir = curdir + "\process3"

#check if new directory exists
if not os.path.exists(newdir):
    os.mkdir(newdir)

#change directory to the new directory, and save the image there
os.chdir(newdir)

Blur_image = image.filter(ImageFilter.BoxBlur(30))
Blur_image.save('Blur_image.jpg')


#_____________________________________________________________________________________________________
# Contrast image

#create a new folder to save Third process
newdir = curdir + "\process4"

#check if new directory exists
if not os.path.exists(newdir):
    os.mkdir(newdir)

#change directory to the new directory, and save the image there
os.chdir(newdir)

Contrast_image = ImageEnhance.Contrast(image).enhance(3)
Contrast_image.save('Contrast_image.jpg')


#_____________________________________________________________________________________________________
# brightness image

#create a new folder to save Third process
newdir = curdir + "\process5"

#check if new directory exists
if not os.path.exists(newdir):
    os.mkdir(newdir)

#change directory to the new directory, and save the image there
os.chdir(newdir)

Brightness_image = ImageEnhance.Brightness(image).enhance(2)
Brightness_image.save('Brightness_image.jpg')




os.chdir(olddir)
print("new directory: " +os.getcwd())