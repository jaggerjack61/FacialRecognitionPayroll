

def saveImage(path):
    import cv2
    face_cascade = cv2.CascadeClassifier('data/image_models/haarcascade_frontalface_default.xml')

    video = cv2.VideoCapture(0)
    i = 1
    while True:
        if i > 3:
            break
        check, frame = video.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=9)
        for x, y, w, h in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 125, 150), 2)
            if key == ord('x'):
                cv2.imwrite(path+'/img'+str(i)+'.jpg', frame)
                i = i+1

        cv2.imshow('Press X to take the pic '+str(i)+'/3', frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


