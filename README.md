# Cursor Movement Using Eyes

This project allows you to control the cursor movement on your computer screen using your eyes. It utilizes computer vision techniques to detect and track your facial landmarks, specifically the position of your eyes, and translates that into cursor movement.

## Requirements

To run this project, you need to have the following installed:

- Python 3.x
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- PyAutoGUI (`pip install pyautogui`)

## Usage

1. Connect a webcam to your computer.

2. Run the command where the main.py file is stored and run the below command.

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script `main.py` using Python.

   ```bash
   python3 main.py
   ```

1. A window will open showing the webcam feed with overlaid facial landmarks.

2. Move your face towards the webcam so that your eyes are clearly visible.

3. Look at different positions on the screen to control the cursor movement accordingly.

   - The position of your eyes determines the movement of the cursor.
   - Blinking your eyes triggers a mouse click action.
  
4. Press the 'q' key or  'ctrl + c'  to exit the program.


## Data Logging

The script logs the frame number, landmark ID, and (x, y, z) coordinates of each detected facial landmark in a CSV file named frame_data.csv. This file can be useful for further analysis or debugging.

   
