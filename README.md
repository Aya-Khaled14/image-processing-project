Overview

This application is a graphical user interface (GUI) for performing various image processing operations. It supports tasks such as Canny Edge Detection, Difference of Gaussian (DoG), adding noise, and removing noise. All the operations are implemented in separate external files, ensuring modularity and maintainability.

Features

Load Image: Load an image from your filesystem for processing.

Canny Edge Detection: Detect edges in the image using the function imported from canny_edge_detection.py.

Difference of Gaussian (DoG): Apply the Difference of Gaussian technique using a function from difference_of_gaussian.py.

Add Noise: Add noise to the image using the function in add_noise.py.

Remove Noise: Remove noise from the image using the function in remove_noise.py.

Save Processed Image: Save the processed image back to your filesystem.

Modular Design

The following operations are implemented in external files:

Canny Edge Detection: The logic for Canny Edge Detection is imported from canny_edge_detection.py.

Difference of Gaussian: The implementation for Difference of Gaussian is imported from difference_of_gaussian.py.

Add Noise: The logic for adding noise to an image is contained in add_noise.py.

Remove Noise: The function to remove noise from an image is in remove_noise.py.

This modular approach makes the code easier to manage and extend. Each file can be independently tested and modified without affecting the main GUI application.

Requirements

To run this application, you need to install the following Python libraries:

opencv-python

numpy

pillow

tkinter (comes pre-installed with Python)

Install the required libraries using the following command:

pip install opencv-python numpy pillow

How to Use

Clone the repository or download the necessary files.

Ensure the required dependencies are installed.

Run the main script using the command:

python main.py

Use the GUI to:

Load an image.

Apply various image processing operations.

Save the processed image.

File Descriptions

main.py: Contains the main GUI logic and integrates all the operations.

canny_edge_detection.py: Implements the Canny Edge Detection function.

difference_of_gaussian.py: Implements the Difference of Gaussian function.

add_noise.py: Provides functionality to add noise to images.

remove_noise.py: Implements noise removal functionality.

Example Workflow

Launch the application.

Click "Load Image" to load an image from your system.

Choose any operation:

"Canny Edge Detection" for edge detection.

"Difference of Gaussian" to enhance details.

"Add Noise" to introduce noise.

"Remove Noise" to clean up noisy images.

Save the processed image using "Save Processed Image."

Screenshot

(Add a screenshot of the application interface and an example of a processed image here.)

Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
