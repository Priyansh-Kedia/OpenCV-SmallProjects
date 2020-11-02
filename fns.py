import cv2 as cv

def getContours(image, copyImage):
    """
    Heirarchy tells if the shape is inside of another shape.
    This is how the heirarchy is defined. It gives the values in 
    this format [Next, Previous, First_Child, Parent].
    """
    contours, heirarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv.contourArea(contour)
        
        if area > 500.0:
            cv.drawContours(copyImage, contour, -1, (255,0,0),3)
            perimeter = cv.arcLength(contour, True)
            
            # Approximates to the nearest polygon
            approx = cv.approxPolyDP(contour,0.02*perimeter, True)
            objectCoordinates = len(approx)

            # Returns the x, y and height width of the polygon
            x, y, w, h = cv.boundingRect(approx)

            if objectCoordinates == 3:
                objectShape = "Triangle"
            elif objectCoordinates == 4:
                ratio = w / float(h)
                if ratio >= 0.95 and ratio <= 1.05:
                    objectShape = "Square"
                else: objectShape = "Rectangle"
            else: objectShape = "Circle"    

            

            # Draw rectangles around the images
            cv.rectangle(copyImage, (x,y), (x+w, y+h), (0,255,0), 2)
            cv.putText(copyImage, objectShape, (x + (w//2), y + (h//2)),cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))


    