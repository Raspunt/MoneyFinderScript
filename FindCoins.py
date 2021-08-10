import cv2 
import numpy as np
from camera import getFiltersCamera



class Coin():




    rangeArray = []
    def Get_Radius_Coins(self):

        frame = getFiltersCamera()[0]
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        RadiusArray = [] 
 
        bilateral_filtered_image = cv2.bilateralFilter(gray_frame, 5, 250, 175)
        # edges = cv2.Canny(bilateral_filtered_image, 200,100)

        edges  = cv2.medianBlur(gray_frame, 7)
            
        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1.1,120,
                   param1=30, param2=50,
                   minRadius=20, maxRadius=220)


        w, h = gray_frame.shape[::-1]


        if circles is not None:
            circles = np.uint16(np.around(circles))
            

            PriceArray = []
            id_circle = 0
            for i in circles[0,:]:
                id_circle = id_circle + 1
                x,y,r = i[0],i[1],i[2]

                cv2.circle(frame, (x, y), r, (0, 255, 0), 4)

     
                
                if r in range(63,69):
                    cv2.putText(frame,"100",(x-35, y) ,cv2.FONT_HERSHEY_SIMPLEX,1.1,(0,0,255),2)
                    PriceArray.append(100)

                elif r in range(51,63):
                    cv2.putText(frame,"50",(x-35, y) ,cv2.FONT_HERSHEY_SIMPLEX,1.1,(0,0,255),2)
                    PriceArray.append(50)
                
                else :
                    cv2.putText(frame,"200",(x-35, y) ,cv2.FONT_HERSHEY_SIMPLEX,1.1,(0,0,255),2)
                    PriceArray.append(200)


                
                if r not in self.rangeArray:
                    self.rangeArray.append(r)

                print(f"min {min(self.rangeArray)} max {max(self.rangeArray)} r {r}")
                print(PriceArray , "\n")

            num = 0
            for pr in PriceArray:
                num = num + pr
            cv2.putText(frame,f"Price: {num}",(400,400) ,cv2.FONT_HERSHEY_SIMPLEX,1.1,(0,0,255),2)

                
                    
                
        cv2.imshow("frame",frame)
    

    
 




   