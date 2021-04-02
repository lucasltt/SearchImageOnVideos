import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

templatePath = ''
videoPath = ''
tolerancia = 0.55
maxFrames = 0
iniFrames = 0
width = 0
height = 0
top = 0
left = 0

if len(sys.argv) == 9:
    templatePath = sys.argv[1]
    videoPath = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])
    iniFrames = int(sys.argv[5])
    maxFrames = int(sys.argv[6])
    top = int(sys.argv[7])
    left = int(sys.argv[8])
else:
    print("WRONG ARGUMENTS")
    print("USAGE: [templatePath] [videoPath] [width] [height] [initalFrame] [endFrame] [top] [left]")
    quit()

vidcap = cv2.VideoCapture(videoPath)
W = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)
H = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)

if H != height:
    print("UNMATCHED RESOLUTION")
    quit()

if W != width:
    print("UNMATCHED RESOLUTION")
    quit()

template = cv2.imread(templatePath, 0)  # open template only once
count = 0
while True:
    method = cv2.TM_CCOEFF_NORMED
    success, image = vidcap.read()
    if not success:
        print("NOT FOUND")
        break

    count += 1
    if count < iniFrames:
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


    #bottom_right = (top_left[0] + w, top_left[1] + h)
    #cv2.rectangle(img,top_left, bottom_right, 255, 2)
 
    if treshold >= tolerancia:
        if top * tolerancia <= top_left[0] <= top * (tolerancia + 1):
            if left * tolerancia <= top_left[1] <= left * (tolerancia + 1):
                #plt.subplot(121),plt.imshow(res,cmap = 'gray')
                #plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
                #plt.subplot(122),plt.imshow(image,cmap = 'gray')
                #plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
                #plt.show()
                print('FOUND')
                quit()

    if maxFrames > 0:
        if maxFrames < count:
            #cv2.imwrite('res.png', image)
            print('MAX FRAMES')
            quit()

