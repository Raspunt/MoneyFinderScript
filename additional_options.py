import cv2

import numpy as np






cap = cv2.VideoCapture(0)


def getFiltersCamera():
    ret,frame = cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    return [frame, thresh]



def ResizeImage(img,scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)


    
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized



rangeArray = []


    
def Get_Price(img):

    h, w, c = img.shape

    Price = 0

    if w in range(158,200) :
        Price = 200
    
    elif w in range (145,157):
        Price = 100
    
    elif w in range(130,144):
        Price = 50
    
    elif w in range(120,129):
        Price = 10

    elif w in range(110,120):
        Price = 20
    
    elif w in range(100,110):
        Price = 5


    
    if  w not in rangeArray:
        rangeArray.append(w)
    
    print(f" wigth {w} height {w} price {Price}")


    return Price
