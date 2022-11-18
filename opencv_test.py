import cv2

# Init a screen obj
vid_screen = cv2.VideoCapture(0)

while True:
    # Capture
    ret, frame = vid_screen.read()
    # Display
    cv2.imshow('OpenCV Window', frame)
    # Stop if any key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release and destroy the screen obj
vid_screen.release()
cv2.destroyAllWindows()


SHA256:c1Hq5X/WXnnuiAR+OQxl9O6BXDjCedg9dt7lsTdRPLE