import cv2
import datetime

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) #file_name, fourcc_code, no.of frames per second, size od vd
#cap.set(3,3000) # if we set any resolution, the camera automatically take resolution
                # which is available for default camera
#cap.set(4,3000)
print(cap.isOpened())
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print(cap.get(3))
#print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = ' Width: '+str(cap.get(3))+' Height: '+str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame,datet,(10,50),font,1,
                            (0,255,255),2,cv2.LINE_AA)
        frame = cv2.putText(frame,text,(50,80),font,1,
                            (0,255,255),2,cv2.LINE_AA)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print(cap)
