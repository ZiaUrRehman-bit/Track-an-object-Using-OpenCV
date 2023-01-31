import cv2 as cv

cap = cv.VideoCapture(0)

tracker = cv.TrackerMOSSE_create() 

while True:

    Success, frame = cap.read()

    cv.imshow("Object Tracking", frame)

    key = cv.waitKey(1)

    if key == ord("q"):
        cap.release()
        cv.destroyAllWindows()
        break

cap.release()
cv.destroyAllWindows()