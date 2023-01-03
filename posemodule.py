import mediapipe as mp
import cv2


class PoseDetector():
    def __init__(self,mode=False,upbody=False,smooth=True,detectcon=0.5,trackcon=0.5):
        self.mode=mode
        self.upbody=upbody
        self.smooth=smooth
        self.detectcon=detectcon
        self.trackcon=trackcon

        self.mpDraw=mp.solutions.drawing_utils
        self.mpPose=mp.solutions.pose
        self.Pose=self.mpPose.Pose(self.mode,self.upbody, self.smooth,self.detectcon,self.trackcon)
        def findpose(self,img,draw=True):

            imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            results = self.Pose.process(imgrgb)
            if draw:
                if results.pose_landmarks:
                    self.mpDraw.draw_landmarks(img,results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
        for id , lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)


def main():
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)
if __name__=="__main__"    :
    main()
