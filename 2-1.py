#영상 반전

import cv2

cap = cv2.VideoCapture('test.avi')

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        inversed = ~frame
        cv2.imshow('frame', frame)
        cv2.imshow('inversed' , inversed)
        if cv2.waitKey(15) == 27:
            break
    else:
        print('error 발생')
        exit()

cap.release()
cv2.destroyAllWindows()