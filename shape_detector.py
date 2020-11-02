import cv2 as cv
from fns import *

image = cv.imread("shape.png")
cv.imshow("Output",image)

# Converting the image to grayscale so as to simplify it 
# by changing the dimension
imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("gray", imageGray)

# Blurring the image to reduce noise
imageBlur = cv.GaussianBlur(imageGray, (7,7), 1)
cv.imshow("blur", imageBlur)

# Edge detection using Canny
imageCanny = cv.Canny(imageBlur, 50, 50)
cv.imshow("canny", imageCanny)

imageCopy = image.copy()
getContours(imageCanny, imageCopy)

cv.imshow("Copied", imageCopy)


cv.waitKey(0)
cv.destroyAllWindows()