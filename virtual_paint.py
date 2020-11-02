import cv2 as cv
from fns import *

frameWidth = 640
frameHeight = 480

cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 110)

colors = [
    [28,50,65,90,202,179],
]

while True:
    success, frame = cap.read()
    cv.imshow("Frame", frame)

    detectColor(frame, colors)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# To be completed, drawing contours according to paint
# Refer to this link https://youtu.be/WQeoO7MI0Bs?t=7452

cap.release()
cv.destroyAllWindows()