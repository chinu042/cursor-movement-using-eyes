import cv2
import mediapipe as mp
import pyautogui
import csv
import math

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Get the frame rate of the webcam
frame_rate = cam.get(cv2.CAP_PROP_FPS)
print("Frame Rate:", frame_rate)

# Create a FaceMesh object for face detection and landmark estimation
face_mesh = mp.solutions.face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

# Get the screen size for cursor control
screen_width, screen_height = pyautogui.size()

# Open the CSV file for writing
csv_file = open('frame_data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Frame', 'Landmark ID', 'X', 'Y', 'Z'])

# Initialize counters and thresholds
frame_counter = 0
blink_counter = 0
blink_threshold = 0.008  # Adjust the threshold as needed

while True:
    # Increment the frame counter
    frame_counter += 1

    # Read a frame from the webcam
    frame_exists, frame = cam.read()
    if not frame_exists:
        break

    # Flip the frame horizontally for a mirrored view
    frame = cv2.flip(frame, 1)

    # Convert the frame from BGR to RGB color space for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with FaceMesh
    results = face_mesh.process(rgb_frame)
    face_landmarks = results.multi_face_landmarks
    frame_height, frame_width, _ = frame.shape

    if face_landmarks:
        # Get the first detected face
        face = face_landmarks[0]

        for id, landmark in enumerate(face.landmark):
            # Extract the x, y, and z coordinates of each landmark
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            z = landmark.z * frame_width  # Scale the Z coordinate based on the frame width

            # Draw a circle at each landmark position
            cv2.circle(frame, (x, y), 3, (0, 255, 0))

            if id == 1:
                # Map the landmark position to the screen size for cursor control
                screen_x = screen_width * landmark.x
                screen_y = screen_height * landmark.y

                # Move the cursor to the mapped position
                pyautogui.moveTo(screen_x, screen_y)

                # Write frame data to the CSV file
                csv_writer.writerow([frame_counter, id, x, y, z])

        # Get the left and right eye landmarks
        left_eye = face.landmark[145].x * frame_width, face.landmark[145].y * frame_height
        right_eye = face.landmark[374].x * frame_width, face.landmark[374].y * frame_height

        # Calculate the distance between the eyes (Z coordinate)
        distance = math.sqrt((left_eye[0] - right_eye[0]) ** 2 + (left_eye[1] - right_eye[1]) ** 2)

        if (face.landmark[362].y - face.landmark[160].y) < blink_threshold:
            # Increment the blink counter
            blink_counter += 1

            if blink_counter >= 5:  # Adjust the counter threshold as needed
                # Perform a mouse click action using PyAutoGUI
                pyautogui.click()
                pyautogui.sleep(1)

                # Reset the blink counter
                blink_counter = 0

    # Display the frame with overlaid landmarks
    cv2.imshow('Cursor Movement Using Eyes', frame)

    # Check if the 'q' key is pressed to exit the program
    if cv2.waitKey(1) == ord('q'):
        break

# Close the CSV file
csv_file.close()

# Release the webcam and close all windows
cam.release()
cv2.destroyAllWindows()

