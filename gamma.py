###################################################################
# Project: Gamma Normalization                                    #
# Filename: gamma.py                                              #
# Description:  This program will take in a video from the user   #
# 				and then it will normalize the gamma levels       #
#				so it is never too bright or too dark.            #
##################################################################
 

 
from PIL import Image
from PIL import ImageEnhance

def get_file():
    path = raw_input("Enter file Path: ")
    return path
#END DEF
    
def get_avg_pixel(pic):    
    pixel = pic.getdata()
    avg = 0.0
    for y in range(0,pic.height()):
        for x in range(0,pic.width()):
            pixRGB = pic.getpixel(x,y)
            R,G,B = pixRGB
            avg += (sum([R,G,B]) / 3.0)
    avg = avg / (pic.width() * pic.height())
    return avg
#END DEF

def change_brightness(filename):
    #function changes brightness depending on the average pixel value
    
    #load the original image into a list
    org_image = Image.open(filename, 'r')
    pixels = org_image.getdata()
    
    pic_brightness = get_avg_pixel(org_image)
    action = 'darken'
    if(pic_brightness > 50):
        action = 'lighten'
    

    #initialize the new image
    new_image = Image.new('RGB', org_image.size)
    new_image_list = []

    brightness_multiplier = 1.0 
    if action == 'lighten':
        brightness_multiplier += (extent/100.0)
    else:
        brightness_multiplier -= (extent/100.0)

    #for each pixel, append the brightened or darkened version to the new image list
    for pixel in pixels:
        new_pixel = (int(pixel[0] * brightness_multiplier),
                     int(pixel[1] * brightness_multiplier),
                     int(pixel[2] * brightness_multiplier))
        #check the new pixel values are within rgb range
        for pixel in new_pixel:
            if pixel > 255:
                pixel = 255
            elif pixel < 0:
                pixel = 0

        new_image_list.append(new_pixel)

    #save the new image
    new_image.putdata(new_image_list)
    new_image.save("/media/removable/Storage/Photos/brightmine.jpg")

path = get_file()
change_brightness(path)
