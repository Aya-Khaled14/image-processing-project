# canny_edge_detection.py

import cv2
import numpy as np

def  canny_edge_detection(image):
    """
    """
    if image is None:
        return None

    # Step 1: Apply Gaussian Blur
    def gaussian_blur(image, kernel_size=5, sigma=1.4):
        """Apply Gaussian Blur to the image."""
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

    blurred_image = gaussian_blur(image)

    # Step 2: Compute gradients using Sobel operator
    def compute_gradients(image):
        """Compute gradients using Sobel operator."""
        grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # x
        grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # y
        return grad_x, grad_y

    grad_x, grad_y = compute_gradients(blurred_image)

    # Step 3: Compute gradient magnitude and direction
    def compute_magnitude_and_direction(grad_x, grad_y):
        """Compute gradient magnitude and direction."""
        magnitude = cv2.magnitude(grad_x, grad_y)
        direction = cv2.phase(grad_x, grad_y, angleInDegrees=True)
        return magnitude, direction

    magnitude, direction = compute_magnitude_and_direction(grad_x, grad_y)

    # Step 4: Non-Maximum Suppression
    def non_maximum_suppression(magnitude, direction):
        """Apply non-maximum suppression to thin edges."""
        suppressed_image = np.zeros_like(magnitude)
        angle = direction / 180.0 * np.pi  
        rows, cols = magnitude.shape

        for i in range(1, rows-1):
            for j in range(1, cols-1):
                # Check direction of gradient
                current_angle = angle[i, j]
                current_magnitude = magnitude[i, j]

                # Horizontal edge
                if (0 <= current_angle < np.pi/8) or (7*np.pi/8 <= current_angle < np.pi):
                    neighbor1 = magnitude[i, j+1]
                    neighbor2 = magnitude[i, j-1]
                # Vertical edge
                elif (np.pi/8 <= current_angle < 3*np.pi/8):
                    neighbor1 = magnitude[i+1, j]
                    neighbor2 = magnitude[i-1, j]
                # Diagonal edge 1
                elif (3*np.pi/8 <= current_angle < 5*np.pi/8):
                    neighbor1 = magnitude[i+1, j+1]
                    neighbor2 = magnitude[i-1, j-1]
                # Diagonal edge 2
                elif (5*np.pi/8 <= current_angle < 7*np.pi/8):
                    neighbor1 = magnitude[i-1, j+1]
                    neighbor2 = magnitude[i+1, j-1]

                # Suppress if not local maxima
                if current_magnitude >= neighbor1 and current_magnitude >= neighbor2:
                    suppressed_image[i, j] = current_magnitude
                else:
                    suppressed_image[i, j] = 0

        return suppressed_image

    suppressed_image = non_maximum_suppression(magnitude, direction)

    # 5: Apply Edge Tracking by Hysteresis (Thresholding)
    def hysteresis(image, low_threshold, high_threshold):
        """Apply edge tracking by hysteresis (thresholding)."""
        strong_edges = (image > high_threshold)
        weak_edges = ((image >= low_threshold) & (image <= high_threshold))

        # Create output image
        output = np.zeros_like(image)

        
        output[strong_edges] = 255

        
        for i in range(1, image.shape[0] - 1):
            for j in range(1, image.shape[1] - 1):
                if weak_edges[i, j]:
                    if (strong_edges[i+1, j] or strong_edges[i-1, j] or
                        strong_edges[i, j+1] or strong_edges[i, j-1] or
                        strong_edges[i+1, j+1] or strong_edges[i-1, j-1] or
                        strong_edges[i+1, j-1] or strong_edges[i-1, j+1]):
                        output[i, j] = 255

        return output

    return hysteresis(suppressed_image, low_threshold=100, high_threshold=200)