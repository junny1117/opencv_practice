#키보드 이벤트 I 이미지 반전

import cv2

img= cv2.imread('test.png')
cv2.namedWindow('img')
cv2.imshow('img', img)

while True:
    keycode = cv2.waitKey()
    if (keycode == 105 or keycode == 73 or keycode == ord('i') or \
            keycode==ord('i')):
        img = ~img
        cv2.imshow('img', img)
    elif keycode == 27 or keycode == ord('q') or keycode == ord('Q'):
        break

cv2.destroyAllWindows()
