import cv2
import time
import handDetection as hd

cap = cv2.VideoCapture(0)
tipIds = [4, 8, 12, 16, 20]
detector = hd.handDetector(detectionCon=0.7)
pTime = 0
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if len(lmList) != 0:
        fingers = []

        if lmList[tipIds[0]][1] < lmList[tipIds[0] -1 ][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)
        cv2.putText(img, str(totalFingers), (480, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)
        
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (143, 134, 123), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)