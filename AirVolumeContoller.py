import cv2
import mediapipe as mp
import time
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
from Handtrackingmodule import HandDetector
cap = cv2.VideoCapture(0)
detector=HandDetector(detectioncon=0.35)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
while True:
    success, img = cap.read()
    img=detector.findHands(img)
    lmlist=detector.findpositon(img,sid=4)
    if len(lmlist)!=0:
        xsq=(lmlist[8][1]-lmlist[4][1])**2
        ysq=(lmlist[8][2]-lmlist[4][2])**2
        dist=(xsq+ysq)**0.5
        vol=np.interp(dist,[20,250],[-65.25,0])
        #currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(vol, None)


    cv2.imshow("Image",img)
    cv2.waitKey(1)