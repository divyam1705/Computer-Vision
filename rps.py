import cv2
import mediapipe
import time
import os
import random
import sys
import Handtrackingmodule as htm
wCam,hCam=1080,1000

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
detector=htm.HandDetector(detectioncon=0.75)
mylist=os.listdir("fingerimages")
overlaylist=[]
for impath in mylist:
    image=cv2.imread(f"fingerimages/{impath}")
    overlaylist.append(image)
tips=[4,8,12,16,20]
rps=["rock","paper","scissors"]
imid=[0,5,2]
def ranrps():
    return random.randint(0,2)
flag=False
y=0
c=0
while True:

    success,img=cap.read()
    img = detector.findHands(img)
    lmlist=detector.findpositon(img,draw=False)

    h,w,c=overlaylist[0].shape

    count=0

    if(len(lmlist)!=0):
        for i in tips:
            if lmlist[i][2]<lmlist[i-2][2]:
                count+=1
    keyPressed = cv2.waitKey(3)
    #if keyPressed == ord('s') :
    if count ==0:
        #cv2.waitKey(2000)
        flag=True
        x=ranrps()


    if flag==True and count>0:

        cv2.putText(img, f"Computer Chooses {rps[x]}", (270, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
        img[0:h, 760:w + 760] = overlaylist[imid[x]]
        if(y==imid[x]):
            cv2.putText(img, "DRAW", (270, 400), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

        elif (y==2 and imid[x]==5) or (y==0 and imid[x]==2) or (y==5 and imid[x]==0):
            cv2.putText(img, "YOU WIN", (270, 400), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

        else:
            cv2.putText(img, "YOU LOSE", (270, 400), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)




    if count==3:
        y=2
        img[0:h, 0:w] = overlaylist[2]
    elif count ==5:
        y=5
        img[0:h, 0:w] = overlaylist[5]
    elif count==1 or count ==4:
        y=0
        img[0:h, 0:w] = overlaylist[0]
    img=cv2.flip(img,0)
    cv2.imshow("Image",img)
    cv2.waitKey(1)