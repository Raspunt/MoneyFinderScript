import cv2 
import numpy as np
from camera import getFiltersCamera
import imutils


class numDec():


    def get_crop(self):

        frame = getFiltersCamera()[0]
        
        
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray_frame,127,255,0)


        cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)


        count_Basie = 0
        for rect in cnts :
            x,y,w,h = cv2.boundingRect(rect)
            print(w,h)

            if w > 60 and h > 60 and w != 640 and h != 480 :
                count_Basie = count_Basie + 1
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                crop = frame[y:y+h, x:x+w]
                # cv2.imshow(f'crop{count_Basie}',crop)

                cv2.imwrite(f'crops/crop{count_Basie}.png',crop) 

            

        
        


        cv2.imshow('frame',frame)


        
        


    