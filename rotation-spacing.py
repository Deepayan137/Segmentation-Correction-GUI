# -*- coding: utf-8 -*-
"""
Automatically detect rotation and line spacing of an image of text using
Radon transform

If image is rotated by the inverse of the output, the lines will be
horizontal (though they may be upside-down depending on the original image)

It doesn't work with black borders
"""

from __future__ import division, print_function
from skimage.transform import radon
from PIL import Image
from numpy import asarray, mean, array, blackman
import numpy
from numpy.fft import rfft
import matplotlib.pyplot as plt
from scipy import ndimage
import cv2
from matplotlib.mlab import rms_flat
try:
    # More accurate peak finding from
    # https://gist.github.com/endolith/255291#file-parabolic-py
    from parabolic import parabolic

    def argmax(x):
        return parabolic(x, numpy.argmax(x))[0]
except ImportError:
    from numpy import argmax

filename = 'skew-linedetection.png'

# Load file, converting to grayscale
image = cv2.imread(filename)
I = asarray(Image.open(filename).convert('L'))
I = I - mean(I)  # Demean; make the brightness extend above and below zero
plt.subplot(2, 2, 1)
plt.imshow(I)

# Do the radon transform and display the result
sinogram = radon(I)

plt.subplot(2, 2, 2)
plt.imshow(sinogram.T, aspect='auto')
plt.gray()

# Find the RMS value of each row and find "busiest" rotation,
# where the transform is lined up perfectly with the alternating dark
# text and white lines
r = array([rms_flat(line) for line in sinogram.transpose()])
rotation = argmax(r)
print('Rotation: {:.2f} degrees'.format(90 - rotation))
plt.axhline(rotation, color='r')
result = ndimage.rotate(image,(90 - rotation))
cv2.imshow('image',result)
cv2.waitKey(0)
# Plot the busy row
row = sinogram[:, rotation]
N = len(row)
plt.subplot(2, 2, 3)
plt.plot(row)

# Take spectrum of busy row and find line spacing
window = blackman(N)
spectrum = rfft(row * window)
plt.plot(row * window)
frequency = argmax(abs(spectrum))
line_spacing = N / frequency  # pixels
print('Line spacing: {:.2f} pixels'.format(line_spacing))

plt.subplot(2, 2, 4)
plt.plot(abs(spectrum))
plt.axvline(frequency, color='r')
plt.yscale('log')
plt.show()
