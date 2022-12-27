import numpy as np
import time
import cv2
import math

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, img = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    img = img[0:500,200:380]
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray,169,25)

    lines = cv2.HoughLines(edges,1,np.pi/180,50)

    niveis = []

    try:
        for line in lines:
            for rho,theta in line:
                a = np.cos(theta)
                b = np.sin(theta)
                if b == 1:
                    x0 = a*rho
                    y0 = b*rho
                    x1 = int(x0 + 1000*(-b))
                    y1 = int(y0 + 1000*(a))
                    x2 = int(x0 - 1000*(-b))
                    y2 = int(y0 - 1000*(a))

                    
                    
                    nivel = (469-y2)*0.0217
                    if nivel > 1 and nivel < 10:
                        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
                        niveis.append(nivel)
            
        if len(niveis) > 0:
            print(niveis[0])
        niveis = None

    except:
        print("esperando linha...")
        
    cv2.line(gray,(0,469),(400,469),(0,0,255),1)
    cv2.imshow("output", img)
    cv2.imshow("edges",edges)

    key = cv2.waitKey(10)
    if key == 27:
        cv2.imwrite('teste.jpg', img)
        break

cv2.destroyAllWindows() 
cv2.VideoCapture(0).release()