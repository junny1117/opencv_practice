#카메라 영상에 시간 출력

import cv2
import time

cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print('Camera open failed')
    exit()

cv2.namedWindow('window')

while True:
    ret, frame = cap.read()
    if ret:
        now = time.localtime()
        str = '%d sec' %now.tm_sec
        cv2.putText(frame, str, (0,100), cv2.FONT_HERSHEY_SIMPLEX,\
                1,(0,0,255),3)
        cv2.imshow('window',frame)
        if cv2.waitkey(10) >= 0:
            break

cap.release()
cv2.destroyAllWindows()