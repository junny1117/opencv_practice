import cv2

def detect_face(image_path):
    # Read the image
    src = cv2.imread(image_path)
    if src is None:
        print('Image load failed!')
        return

    # Load the cascade for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    if face_cascade.empty():
        print("Face cascade xml load failed!")
        return

    # Load the cascade for eye detection
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(src, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 255), 2)

        # Region of interest for the face in the image for eye detection
        roi_color = src[y:y + h, x:x + w]

        # Detect eyes in the face region
        eyes = eye_cascade.detectMultiScale(roi_color)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the output
    cv2.imshow('src', src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function with the image path
detect_face('kids.png')

