import cv2
import imutils
import numpy as np
import pytesseract
import RPi.GPIO as GPIO
import time
import datetime
import credentials
from PIL import Image
GSTREAMER_PIPELINE = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=21/1 ! nvvidconv flip-method=0 ! video/x-raw, width=960, height=616, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink'
video=cv2.VideoCapture(GSTREAMER_PIPELINE, cv2.CAP_GSTREAMER)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12, GPIO.OUT)

while True:
        check,frame=video.read()
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("s"):
             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to grey scale
             gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
             edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
             cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,              cv2.CHAIN_APPROX_SIMPLE)
             cnts = imutils.grab_contours(cnts)
             cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
             screenCnt = None
             for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.018 * peri, True)
                if len(approx) == 4:
                  screenCnt = approx
                  break
             if screenCnt is None:
               detected = 0
               print ("No contour detected")
               continue
             else:
               detected = 1
             if detected == 1:
               cv2.drawContours(frame, [screenCnt], -1, (0, 255, 0), 3)
             mask = np.zeros(gray.shape,np.uint8)
             new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
             new_image = cv2.bitwise_and(frame,frame,mask=mask)
             (x, y) = np.where(mask == 255)
             (topx, topy) = (np.min(x), np.min(y))
             (bottomx, bottomy) = (np.max(x), np.max(y))
             Cropped = gray[topx:bottomx+1, topy:bottomy+1]
             text = pytesseract.image_to_string(Cropped, config='--psm 11')
             print("Detected Number is:",text[:10])
             text=text[:10]
             cv2.imshow("Frame", frame)
             if(text=="MH12DE1433" or text==" MH 12DE 1433" ):
                 print("yoo boy")
                 GPIO.output(12, False)
                 time.sleep(5)
                 picname=datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
                 cv2.imwrite(picname+".jpg",frame)
                 credentials.multi_part_upload("agnobucket", picname+".jpg",picname+".jpg")
                 json_document={"link":credentials.COS_ENDPOINT+"/"+"agnobucket"+"/"+picname+".jpg"}
                 new_document = credentials.my_database.create_document(json_document)
                 GPIO.output(12, True)
             cv2.waitKey(0)
        
cv2.destroyAllWindows()
