import cv2

img = cv2.imread('sodoku.jpg', cv2.IMREAD_GRAYSCALE)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

while True:
    cv2.imshow('img', img)
    cv2.imshow('th1', th1)
    cv2.imshow('th2', th2)
    cv2.imshow('th3', th3)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()