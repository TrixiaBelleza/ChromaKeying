import numpy as np
import cv2
from numpy import*
import os
# Capture video from file
b = cv2.VideoCapture('videoplayback.mp4') #background
f = cv2.VideoCapture('a.mp4')	#foreground

# get width and height
width = int(f.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(f.get(cv2.CAP_PROP_FRAME_HEIGHT))
dimension = (width,height)
# define video codec for file saving
fourcc = cv2.VideoWriter_fourcc('X','V','I','D') # four-char-code
frames_per_second = 20.0
out = cv2.VideoWriter('output.avi', fourcc, frames_per_second, dimension)

while True:

	ret_bg, frame_bg = b.read()
	ret_fg, frame_fg = f.read()
	
	frame_bg = cv2.resize(frame_bg, (width, height)) 

	frame_fg = cv2.medianBlur(frame_fg,5)
	if ret_fg == True:
		frame_bg = np.array(frame_bg) # convert to numpy array
		frame_fg = np.array(frame_fg) # convert to numpy array
		rows,cols,channels = frame_fg.shape
		for i in range(rows):
			for j in range(cols):
				if frame_fg[i,j][1] <= 255 and frame_fg[i,j][1] >= 180:
					# print(frame_fg[i,j])
					frame_fg[i,j][0] = frame_bg[i,j][0]
					frame_fg[i,j][1] = frame_bg[i,j][1]
					frame_fg[i,j][2] = frame_bg[i,j][2]
		cv2.imshow('frame_fg',frame_fg)
		out.write(frame_fg) # write frame to file
		
		if cv2.waitKey(30) & 0xFF == ord('q'):
			break

	else:
		break
b.release()
out.release()
cv2.destroyAllWindows()