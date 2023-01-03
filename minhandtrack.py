import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)
mphands=mp.solutions.hands
hands=mphands.Hands()
mpdraw=mp.solutions.drawing_utils
while True:
    success,img=cap.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgrgb)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                if id==4:
                    cv2.circle(img,(cx,cy),8,(255,0,255),cv2.FILLED)
            mpdraw.draw_landmarks(img, handlms,mphands.HAND_CONNECTIONS)

    cv2.imshow("Image",img)
    cv2.waitKey(1)