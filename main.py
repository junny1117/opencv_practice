import cv2
def test():
    img = cv2.imread('test.png')
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    cv2.waitKey()
test()
