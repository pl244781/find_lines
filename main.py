import cv2 as cv
import numpy as np

def findLines(img_name):
    img = cv.imread(img_name)

    scale_percent = 25
    width = int(img.shape[1] * scale_percent / 100)
    length = int(img.shape[0] * scale_percent / 100)
    dim = (width, length)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 200, 450)
    blur = cv.blur(edges, (15, 15))

    linesP = cv.HoughLinesP(blur, rho = 1, theta = np.pi/180, threshold = 550, minLineLength = 900, maxLineGap = 100)
    if linesP is not None:
        for i in range(len(linesP)):
            l = linesP[i][0]
            cv.line(img, (l[0], l[1]), (l[2], l[3]), (0, 255, 0), 5, cv.LINE_AA)

    '''l1 = linesP[0][0][0]
    l2 = linesP[0][0][1]
    l3 = linesP[0][0][2]
    l4 = linesP[0][0][3]
    cv.arrowedLine(img, (l1, l2), (l3, l4),(0, 0, 0), 5, cv.LINE_AA)
    cv.arrowedLine(img, (l1+l2))'''

    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    blur = cv.resize(blur, dim, interpolation=cv.INTER_AREA)
    edges = cv.resize(edges, dim, interpolation=cv.INTER_AREA)

    cv.imshow("output", img)

    new_name = img_name[:len(img_name) - 4] + "_output.jpg"
    cv.imwrite(new_name, img)

    cv.waitKey(0)

    cv.destroyAllWindows()

findLines("straight.jpg")
findLines("left.jpg")
findLines("right.jpg")

