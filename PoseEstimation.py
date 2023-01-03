import mediapipe as mp
import cv2
mpDraw=mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)
mpPose=mp.solutions.pose
Pose=mpPose.Pose()
while True:
    success,img=cap.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = Pose.process(imgrgb)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id , lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
    cv2.imshow("Image",img)
    cv2.waitKey(1)