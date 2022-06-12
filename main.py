import cv2
import os,time
from obj import  detect
cam = cv2.VideoCapture("http://192.168.43.117:8080/video")

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,2)
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "detect.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        detect(img_name)
        time.sleep(3)
        os.remove(img_name)

cam.release()

cv2.destroyAllWindows()