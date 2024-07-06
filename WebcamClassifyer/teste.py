import cv2

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not access the webcam.")
else:
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        cv2.imshow('Webcam Test', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
