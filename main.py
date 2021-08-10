import cv2
import numpy as np
from FindCoins import Coin
from numDec import numDec


c = Coin()

nd = numDec()


while True:

    nd.get_crop()



    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
