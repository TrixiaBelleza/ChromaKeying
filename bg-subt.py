import cv2
import numpy as np 

cap = cv2.VideoCapture('a.mp4')

while(cap.isOpened()):
  ret, frame = cap.read()
  lower_green = np.array([45,100,80])
  upper_green = np.array([80,255,255])

  # This will be used for intensity slicing
  minratio = 0.05
  maxratio = 1.0

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert input to gray scale
  mask = cv2.inRange(hsv, lower_green, upper_green)
  res = cv2.bitwise_and(frame,frame, mask = mask)
  res = frame - res
  # cv2.imshow("masked", res)
  # cv2.imshow("frame", frame)
  cv2.imshow("Sample", res)
  
  # Continue to show live feed unless "Esc" key is pressed
  key = cv2.waitKey(20)
  if key == 27:
      break
cap.release()
cv2.destroyAllWindows()