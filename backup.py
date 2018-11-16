import numpy as np
import cv2
from numpy import*
# Capture video from file
b = cv2.VideoCapture('videoplayback.mp4')
f = cv2.VideoCapture('a.mp4')
upper_green = [40, 100, 100]
lower_green = [80, 255, 255]

g = lambda fground,bground : copyto(fground,bground,'no',fground>=[155, 186, 83])
while True:

	ret_bg, frame_bg = b.read()
	ret_fg, frame_fg = f.read()
	frame_fg = cv2.resize(frame_fg, (500, 350)) 
	frame_bg = cv2.resize(frame_bg, (500, 350)) 
	frame_fg = cv2.medianBlur(frame_fg,5)
	if ret_bg == True:


		frame_bg = np.array(frame_bg) # convert to numpy array
		frame_fg = np.array(frame_fg) # convert to numpy array
		cv2.imshow('before',frame_fg)

		# # for i in range(0:)
		g(frame_fg, frame_bg)
		cv2.imshow('frame_fg',frame_fg)
		cv2.imshow('frame_bg',frame_bg)
		# cv2.imshow('bck', frame_bg)
		#print(frame[1,1])

		if cv2.waitKey(30) & 0xFF == ord('q'):
			break

	else:
		break

b.release()
cv2.destroyAllWindows()