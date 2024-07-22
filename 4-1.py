import cv2

def nothing(pos):
    pass

img_color = cv2.imread('sodoku.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', img_gray)
cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'Binary', 125)

while True:
    thresh = cv2.getTrackbarPos('threshold', 'Binary')
    ret, img_binary = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary', img_binary)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()