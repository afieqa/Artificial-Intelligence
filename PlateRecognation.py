import os

import cv2
import imutils
import numpy as np
import pytesseract
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'
states = {"A": "Perak", "B": "Selangor", "C": "Pahang", "D": "Kelantan", "F": "Putrajaya", "J": "Johor", "K": "Kedah",
          "M": "Malacca", "N": "Negeri Sembilan", "P": "Penang", "R": "Perlis", "T": "Terengganu", "V": "Kuala Lumpur",
          "W": "Kuala Lumpur", "S": "Sabah", "L": "Labuan", "Q": "Sarawak", "Z": "Military", "U": "University"}

# Read the image file
img = cv2.imread('Dataset\T2.jpg', cv2.IMREAD_COLOR)
# Resize the image file
img = cv2.resize(img, (600, 400))

# Convert to Grayscale Image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Removing Noise from the detected image, before sending to Tesseract
gray = cv2.bilateralFilter(gray, 13, 15, 15)

# Canny Edge Detection
edged = cv2.Canny(gray, 30, 200)
# Find contours based on Edges
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None

for c in contours:

    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    # see whether it is a Rect
    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    detected = 0
    print("No contour detected")
else:
    detected = 1

if detected == 1:
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
new_image = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

text = pytesseract.image_to_string(Cropped, config='--psm 11')
stat = text[0:1]
try:
    print("This car from : ", states[stat])
except:
    print("This car cannot detect from where")
print("\nprogramming_fever's License Plate Recognition\n")
print("Detected license plate Number is:", text)
img = cv2.resize(img, (500, 300))
Cropped = cv2.resize(Cropped, (400, 200))

cv2.imshow('1. Car Image Resize', img)
cv2.imshow('2. Blur', gray)
cv2.imshow('3. edged', edged)
cv2.imshow('4. mask', new_image)
cv2.imshow('5. Cropped', Cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
