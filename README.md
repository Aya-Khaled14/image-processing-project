# 🌟 Image Processing GUI Application

## 📖 Overview

This application is a graphical user interface (GUI) for performing various image processing operations. It supports tasks such as Canny Edge Detection, Difference of Gaussian (DoG), adding noise, and removing noise. All the operations are implemented in separate external files, ensuring modularity and maintainability.

---

## ✨ Features

- **🖼️ Load Image**: Load an image from your filesystem for processing.
- **🔍 Canny Edge Detection**: Detect edges in the image using the function imported from `canny_edge_detection.py`.
- **📊 Difference of Gaussian (DoG)**: Apply the Difference of Gaussian technique using a function from `difference_of_gaussian.py`.
- **🎛️ Add Noise**: Add noise to the image using the function in `add_noise.py`.
- **🧹 Remove Noise**: Remove noise from the image using the function in `remove_noise.py`.
- **💾 Save Processed Image**: Save the processed image back to your filesystem.

---

## 🛠️ Modular Design

The following operations are implemented in external files:

1. **Canny Edge Detection**: The logic for Canny Edge Detection is imported from `canny_edge_detection.py`.
2. **Difference of Gaussian**: The implementation for Difference of Gaussian is imported from `difference_of_gaussian.py`.
3. **Add Noise**: The logic for adding noise to an image is contained in `add_noise.py`.
4. **Remove Noise**: The function to remove noise from an image is in `remove_noise.py`.

This modular approach makes the code easier to manage and extend. Each file can be independently tested and modified without affecting the main GUI application.

---

## 📋 Requirements

To run this application, you need to install the following Python libraries:

- `opencv-python`
- `numpy`
- `pillow`
- `tkinter` (comes pre-installed with Python)

Install the required libraries using the following command:

```bash
pip install opencv-python numpy pillow
