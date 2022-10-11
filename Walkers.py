import cv2


# Create our body classifier


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')
frame = cv2.imread("walking.avi")


gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray)
print(faces)
print(len(faces))
count=0
for (x,y,w,h) in faces:
       cv2.rectangle(cap,(x,y),(x+w,y+h),(0,0,255),2)
       crop_vid= cap[y:y+h,x:x+w] 
       cv2.imwrite("face"+str(count)+".avi" , crop_vid)  
       count=count+1 
# Loop once video is successfully loaded
       
    
    # Read first frame
    

 
 
cv2.imshow('cap',frame)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
