import cv2 
import numpy as np
from camera import getFiltersCamera



class Coin():

    rangeArray = []
    def Get_Price(self,img):

        h, w, c = img.shape

        print(w,h)
        # return 0
        Price = 0

        if w in range(155,200) :
            Price = 200
        
        elif w in range (150,154):
            Price = 100
        
        elif w in range(100,149):
            Price = 50

        # if w not in self.rangeArray:
        #     self.rangeArray.append(w)
        
        
        # print(f"min {min(self.rangeArray)} max {max(self.rangeArray)} w {w}")
        

    

        return Price




         

           

                
                    
                
        

    
 




   