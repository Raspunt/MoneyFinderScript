import cv2

import numpy as np






cap = cv2.VideoCapture(0)


def getFiltersCamera():
    ret,frame = cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    return [frame, thresh]



def ResizeImage(self,img,scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)


    
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized
