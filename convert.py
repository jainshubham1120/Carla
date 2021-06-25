import numpy as np
import cv2
import os
import h5py
from natsort import natsorted, ns


#f= cv2.imread('F:/Carla/WindowsNoEditor/PythonAPI/examples/sem/004316.png')
#print(f.shape)
#i = np.save('rgb/a.py', f)
#r = cv2.imread('F:/Carla/WindowsNoEditor/PythonAPI/examples/rgb/a.py.npy')
#d1 = np.load('sem/a.npy')
#print(len(d1))
#print(data.shape)
#np.savez_compressed('rgb/NPZ', data)




def sa(filename, img):
    return cv2.imwrite(filename, img)




f = cv2.imread('F:/Carla/WindowsNoEditor/PythonAPI/examples/sem/000051.png')
print(f.shape)
print(f.dtype)
print(f)
f0 = f[:,:,0]
#print(f0.shape)
f1 = f[:,:,1]
f2 = f[:,:,2]
print(f2)
cv2.imshow('f0', f0)
cv2.imshow('f1', f1)
cv2.imshow('f2', f2)
#gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
#print(gray)
#print(gray.shape)
#cv2.imshow('f', gray)
#cv2.imwrite("f2_", f2)
sa('f2_', f2)
cv2.waitKey(0)
'''
'''

'''

image_folder1 = 'rgb'
image_folder2 = 'sem'
video_name = 'test.avi'
images1 = [img1 for img1 in natsorted(os.listdir(image_folder1), key=lambda y: y.lower())if img1.endswith(".png")]
images2 = [img2 for img2 in natsorted(os.listdir(image_folder2), key=lambda y: y.lower())if img2.endswith(".png")]

for i in range(len(images1)):
    frame1 = cv2.imread(os.path.join(image_folder1, images1[i]))
    frame2 = cv2.imread(os.path.join(image_folder2, images2[i]))
    cv2.imshow('Vid 1',frame1)
    cv2.imshow('Vid 2',frame2)
    cv2.waitKey(200)

cv2.waitKey(0)
cv2.destroyAllWindows()






















import cv2
import os
from natsort import natsorted, ns
image_folder1 = 'rgb'
image_folder2 = 'sem'
video_name = 'video_sem.avi'
images = [img for img in natsorted(os.listdir(image_folder), key=lambda y: y.lower())
 if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

height1, width1, layers1 = frame1.shape
height2, width2, layers2 = frame2.shape

video1 = cv2.VideoWriter(video_name, 0, 1, (width1,height1))
video2 = cv2.VideoWriter(video_name, 0, 1, (width2,height2))

for image in images1:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

cv2.destroyAllWindows()
video.release()

'''
'''
#"F:/Carla/WindowsNoEditor/PythonAPI/examples/test.avi"
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width  = 640 # float width
height = 480 # float height    
# Make a video writer to see if video being taken as input inflict any changes you make
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out_video = cv2.VideoWriter('output.avi', fourcc, 2.0, (width, height))
#cap.isOpened()
while True:
    ret,frame = cap.read()
    if ret:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('frame',  gray)
        out_video.write(gray)
        #cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        break


cap.release()
out_video.release()
cv2.destroyAllWindows()
'''




'''
import sys
import random
import time
import argparse
import open3d as o3d

#print(o3d.__version__)
#print(cv2.__version__)
'''
'''
pcd = o3d.io.read_point_cloud('037307.ply')
o3d.visualization.draw_geometries([pcd])
'''



'''


'''
