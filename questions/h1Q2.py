from skimage import io
from skimage import img_as_float32
from skimage import transform
from scipy.ndimage import convolve
from scipy.ndimage import correlate
from mpl_toolkits.mplot3d import Axes3D
import time
import matplotlib.pyplot as plt
import numpy as np

I =  io.imread('RISDance.jpg')
I = img_as_float32(I)
filter =  np.array(((1, 0, -1), (1, 0, -1), (1, 0, -1)))
filter = np.expand_dims(filter, -1)

conv = convolve(I, filter)
corr = correlate(I, filter)
plt.imshow( conv )
plt.show()
plt.imshow(corr)
plt.show()