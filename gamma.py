#==================================================================
# Project: Gamma Normalization                                    
# Filename: gamma.py                                              
# Description:  This program will take in a video from the user   
#               and then it will normalize the gamma levels       
#               so it is never too bright or too dark.            
#==================================================================
 
#Importing open cv and numpy for video manipulation
#Importing PIL for image manipulation for each frame
import cv2
import numpy as np
from PIL import Image
from PIL import ImageEnhance

def get_file(): #Simple gets the file for testing with single photo
    path = raw_input("Enter file Path: ")
    pic = Image.open(path, 'r')
    return pic
#END DEF
    
def get_avg_pixel(pic): 
    #this function returns the average value of all the
    #pixels in the image
    pixel = list(pic.getdata()) 
    avg = 0.0
    width, height = pic.size 
    #loops through the photo, checking the every 10th pixel, so as to 
    #speed up the process 
    for y in range(0, height-1, 5):
        for x in range(0, width-1, 5):
            pixRGB = pic.getpixel((x, y))
            R,G,B = pixRGB
            avg += (sum([R,G,B]) / 3.0) #gets the average rgb value of pixels
    avg = avg / ((width/5) * (height/5)) 
    
    #if the brightness is too bright, it wont
    #need to brighten the photo
    if avg > 50:
        avg = 0
        
    return avg
#END DEF


def lighten_photo(org_image, pic_brightness):
    
    #Gets all the pixels from org_image and stores it in pixels
    pixels = org_image.getdata()
    
    #Sets the extent of how much to brighten the photo
    #and changes it to a decimal.
    extent = 0.0
    extent += (pic_brightness / 100)
  
    #creates a new image to preserve the original
    new_image = Image.new('RGB', org_image.size)
    new_image_list = []

    #Adds the extent of the brightness to the multiplier.
    brightness_multiplier = 1.0 + extent

    #goes through and adds the changed pixels into an array
    #for the new image
    for pixel in pixels:
        #if you change all three values the same amount the color doesn't change but the brightness does. 
        new_pixel = (int(pixel[0] * brightness_multiplier),
                     int(pixel[1] * brightness_multiplier),
                     int(pixel[2] * brightness_multiplier))
        #checks to make sure every pixel is still in rgb range
        for pixel in new_pixel:
            if pixel > 255:
                pixel = 255
            elif pixel < 0:
                pixel = 0
        #Once the pixel is an acceptable pixel, places it in an array
        #to create the new image
        new_image_list.append(new_pixel)

    #uses the array of pixels to create the new image.
    new_image.putdata(new_image_list)
    new_image.save("/media/removable/Storage/Photos/brightmine.jpg")
#END DEF

photo = get_file()
brightness = get_brightness(photo)
if brightness != 0:
    lighten_photo(photo, brightness)
    