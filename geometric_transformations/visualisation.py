import numpy as np
import matplotlib.pyplot as plt
from calculations import *

pts = star_points(center=(0, 0), outer_radius=5, inner_radius=2)

R = rotation_matrix(np.pi/10)
pts_rot = transform(pts, R)

Rot = rotation_point_matrix(1, 1, np.pi)
pts_rot1 = transform(pts_rot, Rot)

plt.figure(figsize=(8, 8))
plt.plot(pts_rot[:,0], pts_rot[:,1], color='red')
plt.plot(pts_rot1[:,0], pts_rot1[:,1], color='green')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.title('Аффинные преобразования звезды')
plt.show()