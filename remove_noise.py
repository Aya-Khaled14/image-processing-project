# import cv2
# import numpy as np

# def remove_noise(self):
#     """Remove noise using the efficient median filter (cv2.medianBlur)."""
#     if self.processed_image is None:
#         return

#     if len(self.processed_image.shape) == 3:  
#         denoised_image = np.zeros_like(self.processed_image)
#         for i in range(3):
#             denoised_image[:, :, i] = cv2.medianBlur(self.processed_image[:, :, i], 3) 
#     else:  
#         denoised_image = cv2.medianBlur(self.processed_image, 3) 

#     self.processed_image = denoised_image
#     self.display_image(self.processed_image)

import cv2
import numpy as np

def remove_noise(self):
    """Remove noise using the efficient median filter (cv2.medianBlur), convert color image to grayscale first."""
    if self.processed_image is None:
        return

   
    if len(self.processed_image.shape) == 3:  
        gray_image = cv2.cvtColor(self.processed_image, cv2.COLOR_BGR2GRAY)  
    else:  
        gray_image = self.processed_image

   
    denoised_image = cv2.medianBlur(gray_image, 3) 
    
    self.processed_image = denoised_image
    self.display_image(self.processed_image)
