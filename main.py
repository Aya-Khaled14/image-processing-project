import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk 
from canny_edge_detection import canny_edge_detection  # Import the custom canny_edge_detection function
from difference_of_gaussian import difference_of_gaussian
from add_noise import add_noise
from remove_noise import remove_noise

# Initialize the main GUI window
class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing GUI")
        self.root.geometry("800x800")

        self.root.configure(bg="#2e3b55")  

        self.image = None  # Original Image
        self.processed_image = None  # Processed Image

        # GUI Elements
        self.label = Label(root, text="Image Processing Project", font=("Arial", 20, "bold"), bg="#2e3b55", fg="#ffffff", padx=10, pady=10)
        self.label.pack(pady=20)

        self.image_label = Label(root, bg="#2e3b55")
        self.image_label.pack()

        button_style = {
            "font": ("Arial", 14),
            "bg": "#FFFFFF",  
            "fg": "#2e3b55",  
            "activebackground": "#45a049",  
            "activeforeground": "#ffffff", 
            "relief" : "raised",  
            "bd": 4,  
            "padx": 10, 
            "pady": 5
        }

        self.load_button = Button(root, text="Load Image", command=self.load_image, **button_style)
        self.load_button.pack(pady=10)

        self.canny_button = Button(root, text="Canny Edge Detection", command=self.canny_edge_detection, **button_style)
        self.canny_button.pack(pady=10)

        self.dog_button = Button(root, text="Difference Of Gaussian", command=self.difference_of_gaussian, **button_style)
        self.dog_button.pack(pady=10)

        self.add_noise_button = Button(root, text="Add Noise", command=lambda: add_noise(self), **button_style)
        self.add_noise_button.pack(pady=10)

        self.remove_noise_button = Button(root, text="Remove Noise", command=lambda: remove_noise(self), **button_style)
        self.remove_noise_button.pack(pady=10)

        self.save_button = Button(root, text="Save Processed Image", command=self.save_image, **button_style)
        self.save_button.pack(pady=10)


    def load_image(self):
        """Load an image and display it"""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            self.image = cv2.imread(file_path)  # Load the image in color by default
            self.display_image(self.image)

    def display_image(self, img):
        """Display the image on the GUI"""
        # Check if the image is in color (3 channels)
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB
        img = Image.fromarray(img)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def canny_edge_detection(self):
        """Perform Canny Edge Detection using the custom method"""
        if self.image is None:
            return
        # Convert to grayscale if the image is in RGB
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) if len(self.image.shape) == 3 else self.image
        self.processed_image = canny_edge_detection(gray_image)  # Call the custom canny_edge_detection function
        self.display_image(self.processed_image)


    def difference_of_gaussian(self):
        """Apply Difference of Gaussian"""
        if self.image is None:
            return
        # Convert to grayscale if the image is in RGB
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) if len(self.image.shape) == 3 else self.image
        self.processed_image =  difference_of_gaussian(gray_image)
        self.display_image(self.processed_image)


    def save_image(self):
        """Save the processed image"""
        if self.processed_image is None:
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            # If the image is in color, convert it back to BGR before saving
            if len(self.processed_image.shape) == 3:
                self.processed_image = cv2.cvtColor(self.processed_image, cv2.COLOR_RGB2BGR)
            cv2.imwrite(file_path, self.processed_image)

# Run the application
if __name__ == "__main__":
    root = Tk()
    app = ImageProcessingApp(root)
    root.mainloop()