import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

print("Please step out of the frame while the camera captures the background.")
time.sleep(3)

print("Capturing background...")
background_frames = []
for i in range(30):
    ret, frame = cap.read()
    if ret:
        background_frames.append(frame)

background = background_frames[-1]
print("Background captured! You can now use the cloak. Put on your gray towel.")

lower_gray = np.array([0, 0, 0])
upper_gray = np.array([180, 255, 60])

lower_light_gray = np.array([0, 0, 180])
upper_light_gray = np.array([180, 50, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(hsv, lower_gray, upper_gray)
    mask2 = cv2.inRange(hsv, lower_light_gray, upper_light_gray)
    
    mask = cv2.add(mask1, mask2)
    
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

    mask_inverse = cv2.bitwise_not(mask)
    red_region = cv2.bitwise_and(background, background, mask=mask)

    frame_without_red = cv2.bitwise_and(frame, frame, mask=mask_inverse)

    final_output = cv2.add(red_region, frame_without_red)

    cv2.imshow("Invisibility Cloak", final_output)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()