# import threading,time
# import cv2
# import os
# i=0
# def func(i,frame):
#   print(time.time(),"Hello Timer!",str(i))
#   while os.path.exists("D:\Project\pythonProject\exp01"+str(i)+".jpg"):
#                 i+=1
#   cv2.imwrite('D:\Project\pythonProject\exp01' + str(i) + ".jpg", frame)#将拍摄到的图片保存在data1文件夹中
# cap = cv2.VideoCapture(0)
# t1=time.time()
# while(1):
#     ret,frame=cap.read()
#     cv2.imshow('capture',frame)
#     t2=time.time()
#     if (t2-t1)>=1:
#       s = threading.Timer(1,func,(i,frame,))
#       s.start()
#       t1=t2
#       i=i+1
#     if cv2.waitKey(1)&0xFF==ord('q'):#按键盘q就停止拍照
#         break
# cap.release()
# cv2.destroyAllWindows()

from pynput import keyboard
import cv2
def _start():
     vid = cv2.VideoCapture(0)
     while True:
         isTrue,Frame= vid.read()
         cv2.imshow('Frame',Frame)
         # if cv2.waitKey(20) & 0xFF==ord('d'):
         #   break
def on_press(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    else:
        _start()
# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
