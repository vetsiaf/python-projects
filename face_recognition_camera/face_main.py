import cv2
import numpy as np
import face_recognition
import os
#place images in folder 'Images' and rename them according to persons name

path='images'
images=[]#encoded
classNames=[]#only names
myList=os.listdir(path)
#print(myList)
for i in myList: #get everything from file,and add to the list
    current_img=cv2.imread(f'{path}/{i}')
    #append the encodings of images in the list
    images.append(current_img)
    #add fotos in the list, but only the names
    classNames.append(os.path.splitext(i)[0])
#print(classNames)

def getEncodings(images):
    enc_list=[]
    for img in images:
                    #convert every images to rgb and added to the returned list
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        enc_list.append(encode)
    return enc_list

KnownListEncoded=getEncodings(images) #encoded img from images list to function from
                                      #further encodings
print('Process Completed. Images Encoded')

cap=cv2.VideoCapture(0)

while True:
    success, img = cap.read()
                #resize and convert
    imgS=cv2.resize(img, (0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                #camera encodings and get faces in the frame
    curr_frame=face_recognition.face_locations(imgS)
    encodeFrame=face_recognition.face_encodings(imgS, curr_frame)

            #zip= loop at the same time
    for encodeFace,faceloc in zip(encodeFrame,curr_frame):
        #get a match from list already known(KnownListEncoded) of faces with new face on camera
        match=face_recognition.compare_faces(KnownListEncoded, encodeFace)
        face_dist=face_recognition.face_distance(KnownListEncoded, encodeFace)
        #print(face_dist)
                #get index of the lowest distance in order to match
        index_match=np.argmin(face_dist)
            #in case of a match make a box around the face
        if match[index_match]:
            name=classNames[index_match].upper()
            #print(name)
            y1,x2,y2,x1= faceloc
                #because img is already resized,without the next line
                #the box wont be at the rigt position
            #y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-30),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)


    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
