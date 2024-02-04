import cv2
import numpy as np

cap = cv2.VideoCapture(0)
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters =  cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

while True:
    _, image = cap.read()
    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(image)
    for corners in markerCorners:
        corners = np.int0(corners)
        arc = cv2.arcLength(corners[0], True)
        cv2.polylines(image, [corners], True, (0,255,0), 4)
    cv2.imshow("Result", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()