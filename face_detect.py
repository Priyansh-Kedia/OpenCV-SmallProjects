import cv2 as cv

faceCascade = cv.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

image = cv.imread('lena.png')
grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(grayImage, 1.1, 4)

# Detect multiscale returns x, y , w and h of the face

# Now we shall draw rectangles aroung the faces found
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x+w,y+h), (255, 0, 0), 2)

cv.imshow("Faces", image)
cv.waitKey(0)
cv.destroyAllWindows()