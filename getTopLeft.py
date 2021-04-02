import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

templatePath = ''
videoPath = ''
frame = 0

if len(sys.argv) == 4:
    templatePath = sys.argv[1]
    videoPath = sys.argv[2]
    frame = int(sys.argv[3])
else:
    print("WRONG ARGUMENTS")
    print("USAGE: [templatePath] [videoPath] [frame]")
    quit()

vidcap = cv2.VideoCapture(videoPath)

template = cv2.imread(templatePath, 0)  # open template only once
count = 0

while True:
    method = cv2.TM_CCOEFF_NORMED
    success, image = vidcap.read()
    if not success:
        print("NOT FOUND")
        break

    count += 1
    if count < frame:
        continue

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, method)
 
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        treshold = min_val
    else:
        top_left = max_loc
        treshold = max_val
    
    print('treshold:')
    print(treshold)
    print('top:')
    print(int(top_left[0]))
    print('left:')
    print(int(top_left[1]))
    quit()

