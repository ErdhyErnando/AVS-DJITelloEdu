# DJITello Face Tracking and Keyboard Control 🚁

This repository contains the code for a DJITelloEdu drone that can track and follow faces and control movement using a keyboard. It includes the following files:

## Files
- `face_tracking.py` 📁: Main Python script for controlling the DJITello drone and performing face tracking.
- `haarcascade_frontalface_default.xml` 📄: Haar cascade XML file for face detection.
- `check_battery.py` 📁: Python script to check the DJITello battery.
- `keyboard_movement_control.py` 📁: Python script for controlling the DJITello using the keyboard.

## Usage
1. Connect your computer to the DJITello drone's Wi-Fi network.
2. Run the `face_tracking.py` script.
3. The DJITello drone will take off and start the face tracking.
4. The drone will track and follow detected faces in the live video stream.
5. Press the 'q' key to land the drone and exit the program.

## DJITelloPy Library

This project utilizes the DJITelloPy library, which provides a simple and intuitive interface to control the DJITello drone using Python. For more information on DJITelloPy and its functionalities, refer to the [official documentation](https://djitellopy.readthedocs.io/en/latest/).

## Acknowledgements 🙏
Special thanks to Murtaza's Workshop - Robotics and AI for their valuable contributions and resources that inspired and guided the development of this project. Their expertise and dedication greatly influenced the success of implementing face tracking and keyboard control on the DJITello drone. Thank you, Murtaza's Workshop.
