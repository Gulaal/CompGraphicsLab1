import numpy as np

def star_points(center=(0, 0), outer_radius=5, inner_radius=2, num_points=5):
    x0, y0 = center
    angles = np.linspace(0, 2*np.pi, 2*num_points, endpoint=False)
    radii = [outer_radius, inner_radius] * num_points
    points = []
    for angle, r in zip(angles, radii):
        x = x0 + r * np.cos(angle)
        y = y0 + r * np.sin(angle)
        points.append([x, y])
    points.append(points[0])
    return np.array(points)

def translation_matrix(tx, ty):
    return np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])

def scaling_matrix(sx, sy):
    return np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

def rotation_matrix(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

def rotation_point_matrix(px, py, angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s, px*(1-c)+py*s], [s, c, py*(1-c)-px*s], [0, 0, 1]])

def transfer_Ox_matrix(dx):
    return np.array([[1, 0, dx],[0, 1, 0], [0, 0, 1]])

def transfer_Oy_matrix(dy):
    return np.array([[1, 0 , 0], [0, 1, dy], [0, 0, dy]])

def reflection_Ox_matrix():
    return np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])

def reflection_Oy_matrix():
    return np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])

def reflection_yx_matrix():
    return np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])

def transform(points, matrix):
    N = points.shape[0]
    ones = np.ones((N, 1))
    points_h = np.hstack([points, ones])
    points_transformed_h = (matrix @ points_h.T).T
    return points_transformed_h[:, :2]
