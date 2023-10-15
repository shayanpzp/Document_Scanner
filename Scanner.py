import cv2
import numpy as np


width_image = 640
hight_image = 480

capture = cv2.VideoCapture(0)
capture.set(3,width_image)
capture.set(4,hight_image)
capture.set(10,150)



def processing(image):
    kernel = np.ones((5,5))

    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image_blur = cv2.GaussianBlur(image_gray, (5,5), 1)
    image_canny = cv2.Canny(image_blur, 200, 200)
    image_dialation = cv2.dilate(image_canny, kernel, iterations=2)
    image_threshold = cv2.erode(image_dialation, kernel, iterations=1)

    return image_threshold




def contours(img):
    biggest = np.array([])
    max_area = 0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area>5000:

            cv2.drawContours(image_contour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)

            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area

    return biggest




while True:
    success , image = capture.read()
    image = cv2.resize(image,(width_image,hight_image))
    image_contour = image.copy()
    image_threshold =  processing(image)
    contours(image_threshold)

    cv2.imshow("Video Capture", image)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break