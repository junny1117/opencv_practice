#트랙바

import cv2
import numpy as np

def onChange(pos):
    pass

cv2.namedWindow('win')
cv2.createTrackbar('Red','win', 0, 255, onChange)
cv2.createTrackbar('Blue','win', 0, 255, onChange)
cv2.createTrackbar('Green','win', 0, 255, onChange)
cv2.setTrackbarPos('Red', 'win', 127)
cv2.setTrackbarPos('Blue', 'win', 127)
cv2.setTrackbarPos('Green', 'win', 127)

img = np.zeros((512,512,3), np.uint8)

while True:
   redval = cv2.getTrackbarPos('Red', 'win')
   greenval = cv2.getTrackbarPos('Green', 'win')
   blueval = cv2.getTrackbarPos('Blue', 'win')

   cv2.rectangle(img,(0,0),(512,512),(blueval, greenval, redval),-1)
   cv2.imshow('win', img)
   if cv2.waitKey(1) == 27:
       break

cv2.destroyAllWindows()
