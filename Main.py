import time
import pyautogui
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import pytesseract

print("Top left corner")
time.sleep(2)
start = pyautogui.position()
print("noted!")



print("Bottom right corner")
time.sleep(2)
finish = pyautogui.position()
print("noted!")

filename = 'image.png'

screen = np.array(ImageGrab.grab(bbox=(start.x, start.y, finish.x, finish.y)))
cv2.imwrite(filename, screen)
img = cv2.imread('image.png')
text = pytesseract.image_to_string(img, lang='rus+eng')
print("Your text:\n")
print(text)
cv2.destroyAllWindows()

