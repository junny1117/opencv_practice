#웹캠 활용, 영상반전
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
delay = round(1000 / fps)

print(w, h, fps, fourcc, delay)

outputVideo = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))
if not outputVideo.isOpened():
    print('File open failed')
    exit()

while True:
    ret, frame = cap.read()
    if ret:
        inversed = ~frame
        outputVideo.write(inversed)
        cv2.imshow('frame', frame)
        cv2.imshow('inversed' , inversed)
        if cv2.waitKey(15) == 27:
            break
    else:
        print('error 발생')
        exit()

cap.release()
cv2.destroyAllWindows()