# coding=utf-8

import cv2
import numpy as np
import pygame
import time, sys, os

#if you get error while importing the google how to install <Package Name> in python 3.6

THRESHOLD = 40
camera = cv2.VideoCapture(0)

es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,4))
kernel = np.ones((5,5), np.uint8)
background = None

# Write test video
fps = 2 #camera.get(cv2.CAP_PROP_FPS)
pygame.mixer.init()
cameraSound = pygame.mixer.Sound("snapshotsound.ogg")
size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
		int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('C:\\basic_motion_detection.avi',
				  cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'),
				  fps, size)

initial = int(time.time())
final = initial + 4

while (final-initial):
	#start timer on the frames
	ret, frame = camera.read()
	Text = "Starting in " + str(final-initial) + "..."
	cv2.putText(frame,Text,(60,30),cv2.FONT_HERSHEY_TRIPLEX,1,(0,100,255),2)
	cv2.imshow("contours",frame)
	
	if cv2.waitKey(int(45)) &0xff == ord('q'):
		break
	
	elif int(time.time()) == (initial + 1):
		initial = initial + 1
		print(str(final-initial) + "...")
		
	
while (True):
	ret, frame = camera.read()
	# The first frame as the background
	if background is None:
		background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		background = cv2.GaussianBlur(background, (21,21), 0)
		continue

	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray_frame = cv2.GaussianBlur(gray_frame, (21,21), 0)

	# Compare the difference between each frame of image and the background
	#print(background.shape, gray_frame.shape)
	diff = cv2.absdiff(background, gray_frame)
	diff = cv2.threshold(diff, THRESHOLD, 255, cv2.THRESH_BINARY)[1]
	diff = cv2.dilate(diff, es, iterations=2)
	# Calculate the outline of the target in the image
	image, cnts, hierarchy = cv2.findContours(diff.copy(),
						  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	print ("Detecting " + str(len(cnts)) + " Moving Objects")
	if len(cnts) > 0:
		cameraSound.play()

	for c in cnts:
		if cv2.contourArea(c) < 1500:
			continue
		# Calculate the bounding box
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

	cv2.imshow("contours", frame)
	videoWriter.write(frame)
	cv2.imshow("dif", diff)
	# cv2.imwrite('didff.jpg', diff)
	
	keypress = cv2.waitKey(45)
	if keypress:
		if keypress &0xff == ord('q'):
			break
		elif keypress &0xff == ord('r'):			
			#reset the camera
			background = None

cv2.destroyAllWindows()
camera.release()
