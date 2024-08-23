import numpy as np
import cv2

def canny_edge():
    src = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        exit()
    dst1 = cv2.Canny(src,50,100)
    dst2 = cv2.Canny(src,50,150)
    cv2.imshow('src', src)
    cv2.imshow('dst1',dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    canny_edge()
