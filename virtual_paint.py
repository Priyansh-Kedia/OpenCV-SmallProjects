import cv2 as cv

frameWidth = 640
frameHeight = 480

cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 110)

while True:
    success, frame = cap.read()
    cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.destroyAllWindows()