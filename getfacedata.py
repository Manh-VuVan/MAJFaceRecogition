import cv2
cap = cv2.VideoCapture(0)
count = 0
while True:
    count = count + 1
    ret, frame = cap.read()
    cv2.imshow("MAJ Vision", frame)
    cv2.waitKey(1)
    cv2.imwrite("loan/{}.png".format(count), frame)
    if count == 50:
        break