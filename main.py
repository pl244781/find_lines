import cv2 as cv
import numpy as np

def findLines(img_name):
    img = cv.imread(img_name)

    scale_percent = 25
    width = int(img.shape[1] * scale_percent / 100)
    length = int(img.shape[0] * scale_percent / 100)
    dim = (width, length)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 345, 350, None, 3)
    blur = cv.blur(edges, (25, 25))

    linesP = cv.HoughLinesP(blur, rho = 1, theta = np.pi/180, threshold = 1500, minLineLength = 820, maxLineGap = 1)
    if linesP is not None:
        for i in range(len(linesP)):
            l = linesP[i][0]
            cv.line(img, (l[0], l[1]), (l[2], l[3]), (0, 255, 0), 3, cv.LINE_AA)

    l1x1 = linesP[0][0][0]
    l1y1 = linesP[0][0][1]
    l1x2 = linesP[0][0][2]
    l1y2 = linesP[0][0][3]

    l2x1 = linesP[60][0][0]
    l2y1 = linesP[60][0][1]
    l2x2 = linesP[60][0][2]
    l2y2 = linesP[60][0][3]

    l1p1 = (l1x1, l1y1)
    l1p2 = (l1x2, l1y2)
    l2p1 = (l2x1, l2y1)
    l2p2 = (l2x2, l2y2)

    lst1 = (l1p1, l1p2)
    slst1 = sorted(lst1, key = lambda x:x[1])
    lst2 = (l2p1, l2p2)
    slst2 = sorted(lst2, key = lambda x:x[1])

    cv.arrowedLine(img, (int((slst1[0][0] + slst2[0][0])/2), int((slst1[0][1] + slst2[0][1])/2)), (int((slst1[1][0] + slst2[1][0])/2), int((slst1[1][1] + slst2[1][1])/2)), (0, 0, 0), 5, cv.LINE_AA)

    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

    cv.imshow("output", img)

    new_name = img_name[:len(img_name) - 4] + "_output.jpg"
    cv.imwrite(new_name, img)

    cv.waitKey(0)

    cv.destroyAllWindows()

findLines("straight.jpg")
findLines("left.jpg")
findLines("right.jpg")
