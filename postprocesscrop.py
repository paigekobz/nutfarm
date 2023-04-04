# Importing Image class from PIL module
from PIL import Image
from pathlib import Path 
import time
import os
import cv2
# Opens a image in RGB mode
import numpy


# Size of the image in pixels (size of original image)
# (This is not mandatory)
    
for i in range(14, 34):
    

    im = Image.open(r"C:/Users/pkobzar/nutpics/W36/"+str(i)+".jpeg")
    width, height = im.size
    dirName = r'C:/Users/pkobzar/nutpics/W36'
    Path(dirName).mkdir(parents=True, exist_ok=True)

        # Setting the points for cropped image
    left = 2139
    top = 1026
    right = 2574
    bottom = 1455
        
        # Cropped image of above dimension
        # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
        
        # Shows the image in image viewer
    pix = numpy.array(im1)
    
    fName = 'cropped'+str(i)+'.jpeg'
    
    file = os.path.join(dirName, fName)
    cv2.imwrite(file, pix)
    print('Image saved to', fName)