import cv2 
import numpy as np
from additional_options import getFiltersCamera,ResizeImage,Get_Price
import os


class numDec():
    

   
    

    def get_money_price(self):

        frame = getFiltersCamera()[0]
        
        
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray_frame,127,255,0)


        cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        count_Basie = 0
        PriceArray = []


        sumPrice = 0
        for rect in cnts :
            x,y,w,h = cv2.boundingRect(rect)

            # print(w,h)
            
            
            
            if w >= 60 and h >= 60 and w != 640 and h != 480 :

                count_Basie = count_Basie + 1
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                crop = frame[y:y+h, x:x+w]
                
                crop = ResizeImage(crop,150)
                price = Get_Price(crop)
                PriceArray.append(price)

                obSum = 0
                for pr in PriceArray:
                    obSum = obSum + pr
                
                sumPrice = obSum

                cv2.putText(frame, f'{price}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

 
        
        
        
        cv2.putText(frame, str(sumPrice), (400,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 80, 0), 3)
                
        cv2.imshow('frame',frame)




        
        






        
        


    