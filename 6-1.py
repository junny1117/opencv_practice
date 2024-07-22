#히스토그램 구현, 평활화, 스트레칭
import cv2
import numpy as np 

def calcGrayHist(img):
    channels = [0]
    histSize = [256]
    histRange = [0,256]
    hist = cv2.calcHist([img], channels, None, histSize, histRange)
    return hist

def getGrayHistImage(hist):
    histMax = np.max(hist)
    imgHist = np.full((100,256), 255, dtype=np.uint8)
    for x in range(256):
        pt1 = (x,100)
        pt2 = (x,100 - int(hist[x,0]*100/histMax))
        cv2.line(imgHist, pt1, pt2, 0)
    return imgHist

def histogram_equalization(img):
    equalizedHistImage = cv2.equalizeHist(img)
    return equalizedHistImage

def histogram_stretching(img):
    gmin = float(np.min(img))
    gmax = float(np.max(img))
    stretchedHistImage = ((img - gmin)*256/(gmax-gmin)).astype(np.uint8)
    return stretchedHistImage

if __name__ == '__main__':
    src = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
    if src is None: 
        print('image load falied')
        exit()


while True:
    cv2.imshow('src', src)
    cv2.imshow('srcHist', getGrayHistImage(calcGrayHist(src)))
    ehi = histogram_equalization(src)
    cv2.imshow('ehi', ehi)
    cv2.imshow('eqHist', getGrayHistImage(calcGrayHist(src)))
    shi = histogram_stretching(src)
    cv2.imshow('shi', shi)
    cv2.imshow('stHist', getGrayHistImage(calcGrayHist(src)))
    if cv2.waitKey() == 27:
        break

cv2.destroyAllWindows()