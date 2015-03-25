# Gamma_Correction

## Description
The user enters in the path to a video file. Then the program goes through the video frame by frame, and gets the average pixel value. This average is determined by getting the RGB values adding them together and dividing by three. The resulting number is from 0-255 and determines the brightness of the photo. If this average is below a certain threshold the program lightens the photo and replaces the old dark frame with the new bright frame. 

## Problems
The program is currently untested in it's current form. A problem with the Python Image Library and a certain module saying it is not installed. On the different computers I have tested it on all have showed the same problem. This means that I have not tested this current version. The problem occurs when trying to convert the frame from one file type to another. 

## Working Parts
The program properly gets the brightness of a photo and determines if it should be brightened or not. It also correctly brightens the photo to a desireable amount. 
