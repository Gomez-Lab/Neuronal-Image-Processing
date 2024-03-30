from guided_filter.core.filters import FastGuidedFilter, GuidedFilter
from guided_filter.io_util.image import loadRGB
from guided_filter.cv.image import to32F
import guided_filter
import cv2
import numpy as np
import time
from skimage import io, img_as_float
import matplotlib.pyplot as plt
import os
import time

def guidedPreprocessing(self):
    start_time = time.time()

    # read in images from folder and input into array
    images = []

    for file in os.listdir("images"):
        img = np.float32(cv2.imread(os.path.join("images", file), 1))
        
        # Convert the image to float32 for guided filter
        floatImg = img.astype(np.float32) / 255.0
        # Convert to grayscale for guided filter (if necessary)
        gray = cv2.cvtColor(floatImg, cv2.COLOR_BGR2GRAY)

        # Set the parameters for the guided filter
        radius = 10
        eps = 0.2

        # Create a GuidedFilter object
        guided_filter = GuidedFilter(gray, radius, eps)

        # Apply guided filter
        guided_filtered = guided_filter.filter(floatImg)
        
        img = guided_filtered * 255
        final = img.astype(np.uint8)
        
        filename = file.replace(".tif", "")
        if img is not None:
            images.append((filename, final))

    for n in range(0, len(images)):
        cv2.imwrite(f'guided_{images[n][0]}.png',images[n][1])


    print("Denoising Complete!")
    print("--- %s seconds ---" % (time.time() - start_time))