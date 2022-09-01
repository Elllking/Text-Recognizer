import time
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os
import pyt
import pytesseract

filename = 'image.png'

while(True):
	screen = np.array(ImageGrab.grab(bbox=(424, 111, 983, 199)))
	cv2.imwrite(filename, screen)
	img = cv2.imread('image.png')
	text = pytesseract.image_to_string(img, lang='rus+eng')
	print(text)
	cv2.destroyAllWindows()
	time.sleep(2)
