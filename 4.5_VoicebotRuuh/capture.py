import cv2
from playsound import playsound
import time
def capture():
        camera = cv2.VideoCapture(cv2.CAP_DSHOW)
        #playsound("siri_start.mp3", True)
        for i in range(10):
                return_value, image = camera.read()
                if(i==5):
                        playsound("camera_start.mp3", True)
                        cv2.imwrite('opencv'+str(i)+'.png', image)
                        playsound("camera_end.mp3", True)
        camera.release()
        #print("released")
#while(1):
#        capture()


