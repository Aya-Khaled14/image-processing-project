import cv2
import numpy as np

def difference_of_gaussian(image, sigma1=1.0, sigma2=2.0):
    blurred1 = cv2.GaussianBlur(image, (0, 0), sigma1)
    blurred2 = cv2.GaussianBlur(image, (0, 0), sigma2)
    dog = blurred1 - blurred2
    dog = np.maximum(dog, 0)  # Ensure no negative values
    dog = cv2.normalize(dog, None, 0, 255, cv2.NORM_MINMAX)
    return dog
