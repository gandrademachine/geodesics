import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a sphere
r = 1
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0.0:pi:10j, 0.0:2.0*pi:10j]
def parametrized(n):
    return [n[0]*sin(n[2])*cos(n[1]),n[0]*sin(n[2])*sin(n[1]),n[0]*sin(n[1])]
x,y,z = parametrized([r,theta,phi])

def derivative(function,array,index):
    dx = 1e-4
    return (function(array[index])-function(array[index-1]))/dx
#Import data
# geodesic distance
dist = np.zeros(len(phi))
for i in range(len(phi)):
    for j in range(len(phi)):
        dist[i] = ((sin(phi[i][j])*cos(theta[i][j])-(sin(phi[i-1][j])*cos(theta[i-1][j]))**2+(sin(phi[i][j])*sin(theta[i][j])-sin(phi[i-1][j])*sin(theta[i-1][j]))**2+(cos(phi[i][j])-cos(phi[i-1][j]))**2))**0.5

xx = r*sin(min(dist))*cos(min(dist))
yy = r*sin(min(dist))*sin(min(dist))
zz = r*cos(min(dist))
#Set colours and render
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect("auto")
ax.scatter(x,y,z)

ax.scatter((xx),(yy),(zz))
print(dist)
plt.show()

