import cv2
import sys

videoPath = ''
filename = ''
frame = 0


if len(sys.argv) == 4:
    videoPath = sys.argv[1]
    filename = sys.argv[2]
    frame = int(sys.argv[3])
else:
    print("WRONG ARGUMENTS")
    quit()

vidcap = cv2.VideoCapture(videoPath)

count = 0
while True:
    success, image = vidcap.read()
    if not success:
        print("NOT FOUND")
        break;
    count += 1
    if count >= frame:
        W = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)
        H = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        cv2.imwrite(filename, image)
        print('SCREEN RECORDED')
        print(int(W))
        print(int(H))
        quit()