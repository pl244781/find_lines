import cv2 as cv
import numpy as np

def findLines(img_name):
    img = cv.imread(img_name)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 300, 400)

    cdst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)

    linesP = cv.HoughLinesP(edges, 1, np.pi/180, 50, None, 300, 450)
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(img, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 5, cv.LINE_AA)

    cv.imshow("output", img00)

    cv.waitKey(0)

    cv.destroyAllWindows()

findLines("straight.jpg")
findLines("left.jpg")
findLines("right.jpg")

