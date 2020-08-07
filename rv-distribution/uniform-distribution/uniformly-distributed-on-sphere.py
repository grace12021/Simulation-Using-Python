import numpy as np
import csv
import matplotlib.pyplot as plt

'''
Reference : http://corysimon.github.io/articles/uniformdistn-on-sphere
'''

# Generate N random points
N = 1000

#Generator of Uniform RV
a = np.random.uniform(0, 1, N)
b = np.random.uniform(0, 1, N)

#Spherical Coordinates
theta = 2 * np.pi * a
phi = np.arccos(1-2*b)

#XYZ Coordinates
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

#Visuailization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)

#Save as png
plt.savefig(str(N)+'-points-uniformly-distributed-on-sphere.png')
plt.show()
