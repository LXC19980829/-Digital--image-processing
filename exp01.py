import cv2
import numpy as np
import pandas as pd
from PIL import Image
import  matplotlib.pylab as plt
from skimage import io
#显示图片
# img = cv2.imread("dog1.jpg")
# print("Shape of the image:",img.shape,"\n\n")  #img.shape三个参数分别为：读入图片的高度、读入图片的宽度、读入图像通道数（默认为三通道，设置为-1则为原通道输入）
# cv2.imshow('dog',img)
# cv2.waitKey(0)

#显示视频
# Vid=cv2.VideoCapture("D:\乘风破浪\研学\学习资料\数字图像处理\myvideo.mp4")
#
# while True:
#   isTrue,Frame= Vid.read()
#   cv2.imshow('Frame',Frame)
#   if cv2.waitKey(20) & 0xFF==ord('d'):
#     break
# Vid.release()
# cv2.destroyAllWindows()

#实时采集图像
# capture = cv2.VideoCapture(0)
#
# while(True):
#     # 获取一帧
#     ret, frame = capture.read()
#     # 将这帧转换为灰度图
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) == ord('q'):
#         break

#图像放大缩小
# def FrameResize(frame,scale):
#   Height=int(frame.shape[0]*scale)
#   Width=int(frame.shape[1]*scale)
#   Dimension=(Height,Width)
#   return cv2.resize(frame,Dimension,interpolation = cv2.INTER_AREA)
#
# img=cv2.imread("pineapple.jpg")
# print("Shape of the image before resizing :",img.shape,"\n\n")
# cv2.imshow('pineapple',img)
#
# print("\n \nImage post Resizing \n \n")
# img_resize=FrameResize(img,0.50)
# cv2.imshow('resize',img_resize)
# cv2.waitKey(0)
#
# original_img = cv2.imread("pineapple.jpg")
# Resized=cv2.resize(original_img,(700,850),interpolation=cv2.INTER_LINEAR)
# cv2.imshow('Resized',Resized)
# cv2.waitKey(0)

#更改视频图像大小
# Vid=cv2.VideoCapture("D:\乘风破浪\研学\学习资料\数字图像处理\myvideo.mp4")
#
# while True:
#   isTrue,Frame= Vid.read()
#   New_Frame=FrameResize(Frame,0.50)
#   cv2.imshow('New_Frame',New_Frame)
#   if cv2.waitKey(20) & 0xFF==ord('d'):
#     break
# Vid.release()
# cv2.destroyAllWindows()

#画矩形框
# original_img=cv2.imread("dog1.jpg")
# cv2.rectangle(original_img,(150,150),(300,300),(200,100,150),thickness=2)
# cv2.imshow('original_img',original_img)
# cv2.waitKey(0)


# cv2.rectangle(original_img,(0,0),(original_img.shape[1]//2,original_img.shape[0]//2),(200,155,40),thickness=-1)
# cv2.imshow('original_img',original_img)
# cv2.waitKey(0)

# cv2.circle(original_img,(450,450),40,(25,0,100),thickness=-1)
# cv2.imshow('original_img',original_img)
# cv2.waitKey(0)
#
# cv2.line(original_img,(100,100),(150,150),255,thickness=2)
# cv2.imshow('original_img',original_img)
# cv2.waitKey(0)

# blank=np.ones((500,500,3),dtype='uint8')
#
# cv2.putText(blank,'Good luck',(blank.shape[0]//2,blank.shape[1]//2),cv2.FONT_HERSHEY_COMPLEX,1,(200,0,200),thickness=3)
# cv2.imshow('blank',blank)
# cv2.waitKey(0)

original_img=cv2.imread("640.jpg")
# cv2.imshow('original_img',original_img)
# Crop_img=original_img[200:350,325:450]
# cv2.imshow('Crop_img',Crop_img)
# cv2.waitKey(0)

def rotate(img,angle,center=None):
  w,h=img.shape[:2]
  if center==None:
    center=(w//2,h//2)
    #center is the center of image from which we have to rotate if it is None then it is cconsider as the center of the original image.
  rotMat=cv2.getRotationMatrix2D(center,angle,1.0)
  dim=(w,h)
  return cv2.warpAffine(img,rotMat,dim)

Rotated_img=rotate(original_img,45,(60,60))
cv2.imshow('Rotated_img',Rotated_img)
cv2.waitKey(0)

flip_img=cv2.flip(original_img,-1)
cv2.imshow('flip_img',flip_img)
cv2.waitKey(0)