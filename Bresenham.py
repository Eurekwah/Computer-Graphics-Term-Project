import numpy as np


def calculate(points: list, p, twodx, twody, steps):
    for i in range(steps):
        if p < 0:
            points.append([points[-1][0] + 1, points[-1][1]])
            p = p + twody
        else:
            points.append([points[-1][0] + 1, points[-1][1] + 1])
            p = p + twody - twodx
    return np.array(points)


def bresenham(x_1, y_1, x_2, y_2):
    if x_1 < x_2:
        x_0, y_0, x_e, y_e = x_1, y_1, x_2, y_2
    elif x_1 == x_2:
        points = []
        i = min(y_1, y_2)
        while i != max(y_1, y_2):
            points.append([x_1, i])
            i += 1
        return points
    else:
        x_0, y_0, x_e, y_e = x_2, y_2, x_1, y_1

    slope = (y_e - y_0) / (x_e - x_0)

    dx, dy = x_e - x_1, y_e - y_1

    if slope > 0:
        if slope < 1:
            return(calculate([[x_0, y_0]], 2 * dy - dx, 2 * dx, 2 * dy, dx))
        else:
            points = calculate([[y_0, x_0]], 2 * dx - dy, 2 * dy, 2 * dx, dy)
            points[:, [0, 1]] = points[:, [1, 0]]
            return points.tolist()
    else:
        if slope > -1:
            points = calculate([[x_0, -y_0]], -2 * dy -
                               dx, 2 * dx, -2 * dy, dx)
            points[:, 1] *= -1
            return points.tolist()
        else:
            points = calculate([[-y_0, x_0]], 2 * dx +
                               dy, -2 * dy, 2 * dx, -dy)
            points[:, [0, 1]] = points[:, [1, 0]]
            points[:, 1] *= -1
            return points.tolist()


'''
    for i in range(steps):
        if p < 0:
            points.append([points[-1][0] + 1, points[-1][1]])
            p = p + twody
        else:
            points.append([points[-1][0] + 1, points[-1][1] + 1])
            p = p + twody - twodx
    return points
'''


if __name__ == "__main__":
    print(bresenham(10, -20, 18, -30))
