import cv2 as cv
import numpy as np

image = cv.imread("lena.png")
imageHSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)

windowName = "Trackbars"
HUE_MIN = "Hue min"
HUE_MAX = "Hue max"
SAT_MIN = "Sat min"
SAT_MAX = "Sat max"
VAL_MIN = "Val min"
VAL_MAX = "Val max"

def empty(self):
    pass

cv.namedWindow(windowName)
cv.resizeWindow(windowName, 640, 240)
cv.createTrackbar(HUE_MIN, windowName, 0, 179, empty)
cv.createTrackbar(HUE_MAX, windowName, 179, 179, empty)
cv.createTrackbar(SAT_MIN, windowName, 0, 255, empty)
cv.createTrackbar(SAT_MAX, windowName, 255, 255, empty)
cv.createTrackbar(VAL_MIN, windowName, 0, 255, empty)
cv.createTrackbar(VAL_MAX, windowName, 255, 255, empty)

while True:
    h_min = cv.getTrackbarPos(HUE_MIN, windowName)
    h_max = cv.getTrackbarPos(HUE_MAX, windowName)
    s_min = cv.getTrackbarPos(SAT_MIN, windowName)
    s_max = cv.getTrackbarPos(SAT_MAX, windowName)
    v_min = cv.getTrackbarPos(VAL_MIN, windowName)
    v_max = cv.getTrackbarPos(VAL_MAX, windowName)

    lower = np.array([h_min,s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    
    mask = cv.inRange(imageHSV, lower, upper)
    imageResult = cv.bitwise_and(image, image, mask=mask)
    cv.imshow("mask", mask)
    cv.imshow("final image", imageResult)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.destroyAllWindows()