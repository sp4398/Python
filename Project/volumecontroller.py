import cv2
import mediapipe as mp
import math 
import hypot
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

cap=cv2.VideoCapture(0)
mphands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solution.drawing_utils
device=AudioUtilities.GetSpeakers()
interface=devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
volume=cast (interface,POINTER(IAudioEndpointVolume))

volMin,volMax=volume.GetVolumeRange()[:2]

while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)

    lmList=[]
    if results.multi_hands_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id,lm in enumerate(handlandmark.landmark):
                h,w,_=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
            mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
    if lmList!=[]:
        