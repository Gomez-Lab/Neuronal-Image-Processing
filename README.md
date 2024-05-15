# Neuronal-Image-Processing
This repository contains code for DaVinci Image Processing using a guided filter. 

## DaVinci Image Processing.ipynb
Jupyter Notebook containing code for pre-processing, processing, and plotting
the white pixel count for the DaVinci Images. A folder of .tif images is input
while pre-processed images, processed images, and box plots of the white pixel 
counts are output.

## preprocessing.py
This python file contains the method to preprocess the images using a guided
filter. The resulting preprocessed images are output.

## processing.py
This code file contains the method to process the images using thresholding to
create a set of binary images. A folder of binary histograms and binary images
are output.

## plot.py
This python file contains the method to create a box plot to compare white
pixel counts for the images. Two different plots are output: wound center locations and wound edge locations
