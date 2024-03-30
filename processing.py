import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

def processing(self):
    # Path to the folder containing images
    folder_path = 'guided filtered images'

    # Output folder for saving thresholded images
    output_folder = 'guided binary images'

    # Threshold value (adjust as needed)
    threshold_value = 27

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each file in the folder
    for filename in os.listdir('guided filtered images'):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.tif')):
            # Load an image using OpenCV
            image_path = os.path.join(folder_path, filename)
            original_image = cv2.imread(image_path, 0)

            # Apply thresholding to get a binary image
            _, binary_image = cv2.threshold(original_image, threshold_value, 255, cv2.THRESH_BINARY)
            
            # Save the binary image
            newName = filename.replace(".tif", "")
            newName = newName.replace("denoised_", "")
            output_path = os.path.join(output_folder, f'{newName}_binary.png')
            cv2.imwrite(output_path, binary_image)

            # Plot the histogram of the binary image
            binary_histogram, binary_bins = np.histogram(binary_image.flatten(), 2, [0, 256])
            plt.bar(binary_bins[:-1], binary_histogram, width=1, color='black')
            plt.xlabel('Pixel Intensity')
            plt.ylabel('Frequency')
            plt.title(f'Binary Image Histogram - {newName}')
            
            output_path = os.path.join('guided binary histograms', f'{newName}_binaryHist.png')
            plt.savefig(output_path)
            plt.close()

    print("Complete!")
