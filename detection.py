import cv2

def face(cascade, frame, x, y, w, h):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    if len(face) != 0:
            fin = [x, y, w, h]
            for i in range(4):
                if abs(fin[i] - face[0][i]) > 20:
                    fin[i] = face[0][i]
            x, y, w, h = fin
    return x, y, w, h

def eyes(cascade, frame, x, y, w, h):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    if len(eyes) == 2:
        print(eyes)
        x = eyes[0][0]
        y = eyes[0][1]
        w = eyes[0][1] + eyes[1][1] + eyes[1][3]
        h = max(eyes[0][3], eyes[1][3])
        fin = [x, y, w, h]
        for i in range(4):
            if abs(fin[i] - eyes[0][i]) > 20:
                fin[i] = eyes[0][i]
        x, y, w, h = fin
    return x, y, w, h
