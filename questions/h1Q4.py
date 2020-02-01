from skimage import io
from skimage import img_as_float32
from skimage import transform
from scipy import convolve
from mpl_toolkits.mplot3d import Axes3D
import time
import matplotlib.pyplot as plt
import numpy as np

I =  io.imread('RISDance.jpg')
ksize = np.arange(3, 17, 2)
mpix = np.arange(0.25, 8.25, 0.25)
# Using identity matrix as a filter
filters = [None] * len(ksize)
for i in range(len(ksize)):
    filters[i] = np.zeros((ksize[i], ksize[i]))
#print(filters)
scales = mpix / 8
for i in range(len(scales)):
    scales[i] = round(scales[i], 2)
# print(mpix)
# print(scales)
# print(ksize)
# print(filters)

arrsize = len(ksize) * len(mpix)
xs = np.zeros(arrsize)
ys = np.zeros(arrsize)
zs = np.zeros(arrsize)

print(I.dtype)
test = transform.rescale(I, 0.03)
#mpix vs ksize vs time
for i in range(len(scales)):
    print(scales[i])
    scaled = transform.rescale(I, scales[i])
    for j in range(len(ksize)):
        print("(",i,",",j,")")
        curr_index = i * len(ksize) + j
        xs[curr_index] = ksize[j]
        ys[curr_index] = mpix[i]
        start = time.time()
        convolve(scaled, filters[j], mode='constant', cval=0.0)
        end = time.time()
        zs[curr_index] = end - start
res = Axes3D.scatter(xs, ys, zs=zs)
I = img_as_float32(I)
plt.imshow( I )
plt.show()