**Invisibility Cloak with Python + OpenCV 🪄✨**

Ever wondered what it would feel like to disappear like in the movies? This project uses real-time computer vision to create an invisibility cloak effect, allowing you to turn a simple gray towel into a magical cloak!

This project is an excellent introduction to computer vision concepts like real-time video processing, image masking, and color segmentation.

💡 How It Works
The core of this project relies on color-based image manipulation. The program first captures a static image of the background. Then, in the live video feed, it continuously detects pixels within a specific HSV (Hue, Saturation, Value) color range that corresponds to your gray cloak.

A mask is created to identify these gray pixels. Finally, the program replaces the gray pixels in the live video with the corresponding pixels from the original background image. The result is a seamless illusion that makes the cloak—and the person wearing it—disappear.

🔧 Tech Stack
Python: The core programming language.

OpenCV: A powerful library for computer vision tasks, used here for real-time video capture and image processing.

NumPy: A library for fast numerical operations, used to manage image data as arrays.

💻 How to Run the Project
Prerequisites
Python 3.x installed on your system.

A webcam.

Installation
Clone this repository or download the cloak.py file.

Install the required libraries using pip:

pip install opencv-python numpy

Execution
Make sure you are not in front of your webcam when you start the program.

Open your terminal and navigate to the project directory.

Run the script:

python cloak.py

The program will capture the background and display the message "Background captured!".

Step into view and put on your gray towel to see the invisibility effect.


