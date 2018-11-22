import cv2
import numpy as np 

background = "bg"
foreground = "harot"


cap = cv2.VideoCapture("./foreground/" + foreground + '.mp4')
b = cv2.VideoCapture("./background/" + background + '.mp4') 



width = int(b.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(b.get(cv2.CAP_PROP_FRAME_HEIGHT))
dimension = (width,height)
# define video codec for file saving
fourcc = cv2.VideoWriter_fourcc('X','V','I','D') # four-char-code
frames_per_second = 20.0
out = cv2.VideoWriter('result_' + foreground + '.avi', fourcc, frames_per_second, dimension)



while(cap.isOpened()):
  ret, frame = cap.read()
  ret2, frame2 = b.read()

  #Adjust niu to
  lower_green = np.array([20,60,60])
  upper_green = np.array([100,255,255])

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert input to gray scale
  mask = cv2.inRange(hsv, lower_green, upper_green)
  mask_inv = cv2.bitwise_not(mask)


  green = cv2.bitwise_and(frame,frame, mask = mask)
  green2 = cv2.bitwise_and(frame2,frame2, mask = mask)
  res = frame - green
  res = cv2.add(green2,res)
  cv2.imshow("Sample",res)
  
  out.write(res) # write frame to file

  # Continue to show live feed unless "Esc" key is pressed
  key = cv2.waitKey(20)
  if key == 27:
      break
cap.release()
cv2.destroyAllWindows()
