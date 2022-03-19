import cv2 as cv
import numpy as np

def findLines(img_name):
    img = cv.imread(img_name)

    scale_percent = 25
    width = int(img.shape[1] * scale_percent / 100)
    length = int(img.shape[0] * scale_percent / 100)
    dim = (width, length)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 225, 450, 3)

    blur = cv.blur(edges,(5,5))

    linesP = cv.HoughLinesP(blur, 10, np.pi/180, 8420, None, 1365, 1700)
    if linesP is not None:
        for i in range(len(linesP)):
            l = linesP[i][0]
            cv.line(img, (l[0], l[1]), (l[2], l[3]), (0, 255, 0), 15, cv.LINE_AA)

    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

    cv.imshow("output", img)

    new_name = img_name[:len(img_name) - 4] + "_output.jpg"
    cv.imwrite(new_name, img)

    cv.waitKey(0)

    cv.destroyAllWindows()

findLines("straight.jpg")
findLines("left.jpg")
findLines("right.jpg")
