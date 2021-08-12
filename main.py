import cv2
import numpy as np
from numDec import numDec



nd = numDec()


while True:


    
    nd.get_money_price()




    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

