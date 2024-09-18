import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
import mediapipe as mp # for arduino
import controller as cnt # for arduino

total='objectname'
posX=0
posY=0
m='ahh'
obj_direction_x=0

model=YOLO('yolov8s.pt')

cap=cv2.VideoCapture(0)

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")
# print(class_list)
count=0
while True:
    
    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    video_width=1020
    video_height=500
    half_width=int(video_width/2)
    half_height=int(video_height/2)
    frame=cv2.resize(frame,(video_width,video_height))
    results=model.predict(frame)
    #print(results)
    a=results[0].boxes.boxes
    # print(len(a))
    # if (len(a)>0):
    #     print('ase')
    # else:
    #     print('empty')
    px=pd.DataFrame(a).astype("float")
    # print(px)
    if (len(a)>0):
        print('ase')
        # print(half_width)
        for index,row in px.iterrows():
            x1=int(row[0])
            y1=int(row[1])
            x2=int(row[2])
            y2=int(row[3])            


           

            _id=int(row[5])
            c=class_list[_id]
            # print(len(c))
            # if len(c)>0:
            #     print('okay')
            # else:
            #     print('Empty list')
   
            m=c
            mid_point_X=(x1+x2)/2
            mid_point_Y=(y1+y2)/2
            # cnt.led(total,obj_direction_x)
            if (m=='bottle' or m=='cup' or m=='fire hydrant'):
                total='bottle'
                cnt.led(total,obj_direction_x)
                posX=mid_point_X
                posY=mid_point_Y
                # print(c)
                # print(mid_point)
                var=30
                print("positon Y==",posY)
                # print("positon X==",posX)
                if(posY>half_height+20):
                    obj_direction_x='catch'   
                                  
                elif(posX>=half_width-var and posX<=(half_width+var) and posY<half_height):
                    obj_direction_x='forward'
             
                elif(posX>half_width+var and posX<video_width and posY<half_height):
                    obj_direction_x='right'  
                elif(posX<half_width-var and posX>0 and posY<half_height):
                    obj_direction_x='left'
                   
                
                else:
                    obj_direction_x='none'
                    total='none'
                    posX=-990
                    posY=-990
                    cnt.led(total,obj_direction_x)
         
            elif (m!='bottle' or m!='cup' or m!='fire hydrant'):
                 m='none'
                 total='none'
                 cnt.nothing(total)
                 cnt.led(total,obj_direction_x)
            else:
                total='ab'
                cnt.nothing(total)
                # print('not')
                posX=-2   
                posY=-990
                cnt.led(total,obj_direction_x)
        

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.putText(frame,str(c),(x1,y1),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)

    else:
        print('empty')
        total='ab'
        cnt.nothing(total)
        # print('not')
        posX=-2  
        posY=-990 
        cnt.led(total,obj_direction_x)

    
    
    cnt.led(total,obj_direction_x)
    cv2.line(frame, (half_width, 0), (half_width,int(video_height)),(0,250,0), 3)
    cv2.line(frame, (0,half_height), (int(video_width),half_height),(0,250,0), 3)
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
