__author__ = 'alexey'

TEST_VIDEO = 'E:/rc-video/GOPR0544.mp4'

import cv2

cap = cv2.VideoCapture(TEST_VIDEO)
if not cap.isOpened():
    print('Something gone bad :(')
    exit(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()