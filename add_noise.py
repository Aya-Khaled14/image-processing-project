import cv2
import numpy as np

def add_noise(self):

        if self.image is None:
         return

    # Copy the image to avoid modifying the original
        noisy_image = self.image.copy()

    # Probability of noise
        prob = 0.02  # Adjust this value to control noise level

    # Get image dimensions
        if len(self.image.shape) == 3:  # Color image
            row, col, ch = self.image.shape
        else:  # Grayscale image
          row, col = self.image.shape
          ch = 1

    # Add salt noise (white pixels)
        num_salt = int(prob * row * col)
        salt_coords = [np.random.randint(0, i, num_salt) for i in (row, col)]
        if ch == 3:
          noisy_image[salt_coords[0], salt_coords[1], :] = 255  # Set to white
        else:
          noisy_image[salt_coords[0], salt_coords[1]] = 255

    # Add pepper noise (black pixels)
        num_pepper = int(prob * row * col)
        pepper_coords = [np.random.randint(0, i, num_pepper) for i in (row, col)]
        if ch == 3:
            noisy_image[pepper_coords[0], pepper_coords[1], :] = 0  # Set to black
        else:
         noisy_image[pepper_coords[0], pepper_coords[1]] = 0

    # Set the processed image
        self.processed_image = noisy_image
        self.display_image(self.processed_image)