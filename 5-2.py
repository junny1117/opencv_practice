#트랙바 이용 명암비 조절

import cv2
import numpy as np 

def level_change(pos):
     alpha = (pos-10)/10
     dst2 = np.clip(src + (src - 128.)*alpha, 0, 255).astype(np.uint8)
     cv2.imshow('Twindow', dst2)

if __name__ == '__main__':
    src = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
    if src is None: 
        print('image load falied')
        exit()

s=2.0
dst = cv2.multiply(src, s)

cv2.namedWindow('Twindow')
cv2.createTrackbar('level', 'Twindow', 0,20, level_change)

while True:
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    if cv2.waitKey() == 27:
            break
            
    cv2.destroyAllWindows()