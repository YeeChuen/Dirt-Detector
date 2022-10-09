# Author: Yee Chuen Teph
# title: test_processimage
# Description: test zone for processing image

from distutils.command.clean import clean
import os
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

#olddir = os.getcwd()
#os.chdir(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2\testzone')

# get image
#image = Image.open(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2\floor_image\cleanfloor.jpg')
#original = Image.open(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2\floor_image\dirt_on_floor.jpg')
#clean = Image.open(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2\floor_image\filename.jpg')

#________________________________________________________________________________________________
# function that return an image with outlined dirt location

def dirtdetection(file):
    
    image = Image.open(file)
    # blur image
    # image = image.filter(ImageFilter.BoxBlur(2))
    # image.save('1blurtest.jpg')

    # greyscale image
    image = image.convert('L')

    # contrast image
    image = ImageEnhance.Contrast(image).enhance(3)

    # brightness image
    image = ImageEnhance.Brightness(image).enhance(2)

    number = 0
    imagename = 'process1.'+str(number)+'.jpg'
    while os.path.exists(imagename):
        number+=1
        imagename = 'process1.'+str(number)+'.jpg'
    image.save(imagename)

    return(imagename)

    # invert image color
    # image = ImageOps.invert(image)
    # image.save('5inverttest.jpg')

    # sharpness image
    # image = ImageEnhance.Sharpness(image).enhance(100)
    # image.save('6sharpnesstest.jpg')

    # edge detection image
    # image = image.filter(ImageFilter.FIND_EDGES)
    # image.save('7edgedetectiontest.jpg')




#clean = dirtdetection(clean)
#testimage = dirtdetection(r'D:\Coding Software\HackathonVSC\Hackathon\RoboHacks_2\floor_image\cleanfloor.jpg')
#testimage.show()


#________________________________________________________________________________________________
# function that change edge detection into red lines with white background

def convertRedWhite(file):
    
    image = Image.open(file)
    image = image.convert("RGB")
    
    d = image.getdata()
    
    new_image = []
    for item in d:
    
        # change all white (also shades of whites)
        # pixels to yellow
        if item[0] not in list(range(0, 10)):
            new_image.append((255, 0, 0))
        else:
            new_image.append((255, 255, 255))
            
    # update image data
    image.putdata(new_image)

    return checkRed(image)


#testimage = convertRedWhite(testimage)
#testimage.show()


#________________________________________________________________________________________________
# check if image has red

def checkRed(image):
    #print(image.getcolors())
    if(len(image.getcolors())) > 1:
        return "dirty"
    else:
        return "clean"


#________________________________________________________________________________________________
# check if image has red

#testimage = testimage.convert("RGB")
#oriimage = original.convert("RGB") 
#new = Image.new(mode="RGBA", size=(1920,1080), color=(255,255,255))
#new.show()

#print(checkRed(testimage))
#print(checkRed(original))
#print(checkRed(new))

#testmerge = Image.merge("RGB", (testimage, oriimage))

#os.chdir(olddir)