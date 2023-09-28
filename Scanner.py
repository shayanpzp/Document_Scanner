import cv2


frame_width = 640
frame_height = 480

capture = cv2.VideoCapture(0)
capture.set(3,frame_width)
capture.set(4,frame_height)
capture.set(10,150)

while True:
    success , image = capture.read()
    cv2.imshow("Video Capture", image)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break