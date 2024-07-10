#마우스 이벤트, 그림판

import cv2
import numpy as np

oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx,oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags == cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx,oldy),(x,y),(0,0,255),2)
            oldx, oldy = x,y
        elif flags == cv2.EVENT_FLAG_RBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 0), 10)
            oldx, oldy = x, y
    elif event == cv2.EVENT_RBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_RBUTTONDOWN: %d, %d' % (x, y))
    elif event == cv2.EVENT_RBUTTONUP:
        print('EVENT_RBUTTONUP: %d, %d' % (x, y))



img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

while True:
    cv2.imshow('img', img)
    if cv2.waitKey(1) ==27:
        break

cv2.destroyAllWindows()