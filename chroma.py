import cv2
import numpy as np 

background = "trix_turn_around_long"
foreground = "fg_trix_turn_around_crop"

cap = cv2.VideoCapture("./foreground/" + foreground + '.mp4')
b = cv2.VideoCapture("./background/" + background + '.mp4') 

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (0,0,255)
lineType               = 2
flag                   = 0

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

  frame = cv2.resize(frame,(width,height))
  #Adjust niu to
  lower_green = np.array([40,60,60])
  upper_green = np.array([90,255,255])

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert input to gray scale
  mask = cv2.inRange(hsv, lower_green, upper_green)
  mask_inv = cv2.bitwise_not(mask)



  green = cv2.bitwise_and(frame,frame, mask = mask)
  green2 = cv2.bitwise_and(frame2,frame2, mask = mask)
  res = frame - green
  res = cv2.add(green2,res)
  cv2.imshow("Sample",res)

  out.write(res) # write frame to file

  if (flag == 0):
    cv2.putText(res,'Lower Green: {} Higher Green: {}'.format(lower_green,upper_green), 
      bottomLeftCornerOfText, 
      font, 
      fontScale,
      fontColor,
      lineType)
    cv2.imwrite("./green_array/foreground{}.jpg".format(foreground), res)
    flag +=1

  # Continue to show live feed unless "Esc" key is pressed
  key = cv2.waitKey(20)
  if key == 27:
      break
cap.release()
cv2.destroyAllWindows()
