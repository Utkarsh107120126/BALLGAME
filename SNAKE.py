import numpy as np
import cv2
import random
img = np.zeros((1600,1600,3),dtype='uint8')
ce=[200,250,9]
b=-1
Q=[[255,255,255],[255,255,0],[255,0,255],[0,255,0],[128,0,120],[255,0,0],[0,69,255]]
i=0
P=Q[i]
while 1:
    cv2.imshow('BALL',img)
    img = np.zeros((1600,1600,3),dtype='uint8')
    cv2.circle(img,(ce[0],ce[1]),ce[2],(P[0],P[1],P[2]),-1)
    k=cv2.waitKey(1)
    if k==ord('a'):
        b=0
    if k==ord('d'):  
        b=1
    if k==ord('w'):
        b=3
    if k==ord('s'):
        b=2
    if b==1:
        ce[0]+=10
    if b==0:
        ce[0]-=10
    if b==2:
        ce[1]+=10
    if b==3: 
        ce[1]-=10
    if ce[0]>1600:
        ce[0]=0
    if ce[0]<0:
        ce[0]=1600
    if ce[1]>900:
        ce[1]=0
    if ce[1]<0:
        ce[1]=900
    if k==27:
        break
    if k==ord('g'):
        i=random.randrange(len(Q))
        P=Q[i]
    if k==ord('+'):   
        ce[2]+=2
    if k==ord('-'):
        ce[2]-=2
    if k==ord('p'):
        b=-1
    if k==ord('f'):
        ce=[200,250,9]
        b=-1
    if k==ord('j'):
        ce[1]+=100
 