import cv2
import numpy as np
from PIL import Image
from getRange import get_limits


yellow = [0, 255, 255]

colors = {"red": (0, 0, 255), "blue": (255, 0, 0), "green": (0, 255, 0), "yellow": (0, 255, 255), "orange": (0, 165, 255)}
    
print("Choose a color:")

for i, color in enumerate(colors.keys()):
    print(f"{i + 1}. {color}")

index = input("Enter the number corresponding to your choice: ")
colorChoice = list(colors.values())[int(index) - 1]

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    hsvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color = colorChoice)

    mask = cv2.inRange(hsvimage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cap.destroyAllWindows()
