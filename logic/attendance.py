import face_recognition
import os

import sqlite3

KNOWN_FACES_DIR = 'data/employees'
UNKNOWN_FACES_DIR = 'data/temp'
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'hog'  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model


# Returns (R, G, B) from name
def name_to_color(name):
    import cv2
    # Take 3 first letters, tolower()
    # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
    color = [(ord(c.lower()) - 97) * 8 for c in name[:3]]
    return color


def saveImage():
    import cv2
    face_cascade = cv2.CascadeClassifier('data/image_models/haarcascade_frontalface_default.xml')

    video = cv2.VideoCapture(0)
    i = 1
    while True:
        if i > 3:
            break
        check, frame = video.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=9)
        key = cv2.waitKey(1)
        frameR = None
        if key == ord('x'):
            cv2.imwrite('data/temp/image.jpg', frame)
            i = 4
        for x, y, w, h in faces:
            frameR = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 125, 150), 2)

        cv2.imshow('Press X to take the pic ', frame if frameR is None else frameR)

        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def takeImage():
    print('here')
    import cv2
    face_cascade = cv2.CascadeClassifier('data/image_models/haarcascade_frontalface_default.xml')

    video = cv2.VideoCapture(0)
    i = 1
    while True:
        check, frame = video.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=9)
        key = cv2.waitKey(1)
        frameR = None

        for x, y, w, h in faces:
            cv2.imwrite('data/temp/image.jpg', frame)
            frameR = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 125, 150), 2)

            video.release()
            cv2.destroyAllWindows()
            return matchImage()

        if key == ord('q'):
            break
        cv2.imshow('Look into the camera',frame)
    video.release()
    cv2.destroyAllWindows()
    return False


def matchImage():
    import cv2
    print('Loading known faces...')
    known_faces = []
    known_names = []

    # We oranize known faces as subfolders of KNOWN_FACES_DIR
    # Each subfolder's name becomes our label (name)
    for name in os.listdir(KNOWN_FACES_DIR):

        # Next we load every file of faces of known person
        for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
            # Load an image
            image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')

            # Get 128-dimension face encoding
            # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
            encoding = face_recognition.face_encodings(image)[0]

            # Append encodings and name
            known_faces.append(encoding)
            known_names.append(name)

    print('Processing unknown faces...')
    # Now let's loop over a folder of faces we want to label
    for filename in os.listdir(UNKNOWN_FACES_DIR):

        # Load image
        print(f'Filename {filename}', end='')
        image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')

        # This time we first grab face locations - we'll need them to draw boxes
        locations = face_recognition.face_locations(image, model=MODEL)

        # Now since we know loctions, we can pass them to face_encodings as second argument
        # Without that it will search for faces once again slowing down whole process
        encodings = face_recognition.face_encodings(image, locations)

        # We passed our image through face_locations and face_encodings, so we can modify it
        # First we need to convert it from RGB to BGR as we are going to work with cv2
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # But this time we assume that there might be more faces in an image - we can find faces of dirrerent people
        print(f', found {len(encodings)} face(s)')
        for face_encoding, face_location in zip(encodings, locations):

            # We use compare_faces (but might use face_distance as well)
            # Returns array of True/False values in order of passed known_faces
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)

            # Since order is being preserved, we check if any face was found then grab index
            # then label (name) of first matching known face withing a tolerance
            match = None
            if True in results:  # If at least one is true, get a name of first of found labels
                match = known_names[results.index(True)]
                print(f' - {match} from {results}')
                return match
    return False


def saveTime():
    con = sqlite3.connect('payroll.db')

    cur = con.cursor()
    cur.execute("""INSERT INTO logged_times VALUES ('admin','12345',0)""")
    con.commit()

    cur.execute("SELECT * FROM logged_times")

    print(cur.fetchall())
    con.close()

