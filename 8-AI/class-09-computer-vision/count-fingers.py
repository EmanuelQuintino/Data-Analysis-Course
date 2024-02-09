# reference: https://developers.google.com/mediapipe/solutions/vision/hand_landmarker
# pip install opencv-python,
# pip install mediapipe

import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

while True:
    check, frame = video.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = Hand.process(frame_rgb)
    hands_points = results.multi_hand_landmarks

    h, w, _ = frame.shape
    array_points = []
    if hands_points:   
      for points in hands_points:
        mp_draw.draw_landmarks(frame, points, hand.HAND_CONNECTIONS)
        for id, cord in enumerate(points.landmark):
         cx, cy = int(cord.x * w), int(cord.y * h)
         cv2.putText(frame, str(id), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 2)
         array_points.append((cx, cy))
      
      fingers = [8, 12, 16, 20]
      count_fingers = 0
      
      if points:
        # left hand
        if array_points[4][0] < array_points[2][0]:
          count_fingers +=1

        for v in fingers:
          if array_points[v][1] < array_points[v - 2][1]:
            count_fingers += 1
      
      cv2.rectangle(frame, (1, 1), (180, 40), (255, 255, 255), -1)
      cv2.putText(frame, f"Fingers: {count_fingers}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Finger Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break

video.release()
cv2.destroyAllWindows()
