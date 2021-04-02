# Search Logos on Videos
A collection of tree simple python scripts that helps finding logos/watermarks on a video file using opencv library. Created for learning pourposes in order to try to clasify some videos based on the producer.

## takeScreen.py
Used to create a bitmap image of a single frame of the video.

#### Parameters
1. videoPath = Full Path of the video
2. filename = Output filename of the image.
3. frame = Frame Number to process

## getTopLeft.py
Used to get to top/left/treshold position of the logo on the specified video frame.
This will be used in order to avoid false positives on the final detection.

#### Parameters
1. templatePath = Path of the image/logo to find on the frame
2. videoPath = Full Path of the video
3. frame = Frame Number to process


## videoParser.py
Used to process the video file and find the logo on a range of frames. Uses opencv matchTemplate method.

#### Parameters
1. templatePath = Path of the image/logo to find on the video
2. videoPath = Full Path of the video
3. width = Horizontal Size of the video in pixels
4. height = Vertical Size of the video in pixels
5. initFrames = Initial frame to start looking for the logo
6. maxFrame = Final fram to end looking for the logo
7. top = Expected Top Position of the logo (provided by getTopLeft.py)
8. left = Expected Left Position of the logo (provided by getTopLeft.py)
