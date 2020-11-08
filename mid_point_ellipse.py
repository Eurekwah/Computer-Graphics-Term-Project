import numpy as np


def copypoints(points: list, x, y):
    a = np.array([[x, y], [-x, -y], [x, -y], [-x, y]])
    a = np.unique(a, axis=0)
    for i in a.tolist():
        points.append(i)


def mpe(r_x, r_y, x_c, y_c):
    p = pow(r_y, 2) - pow(r_x, 2) * r_y + 1/4 * pow(r_x, 2)
    x, y = 0, r_y
    points = []
    copypoints(points, x, y)
    while(2 * pow(r_y, 2) * x <= 2 * pow(r_x, 2) * y):
        x += 1
        if p < 0:
            p = p + 2 * pow(r_y, 2) * x + pow(r_y, 2)
        else:
            y -= 1
            p = p + 2 * pow(r_y, 2) * x + pow(r_y, 2) - 2 * pow(r_x, 2) * y
        copypoints(points, x, y)
    p = pow(r_y, 2) * pow((x + 1/2), 2) + pow(r_x, 2) * \
        pow((y - 1), 2) - pow(r_x, 2) * pow(r_y, 2)
    while y != 0:
        y -= 1
        if p > 0:
            p = p - 2 * pow(r_x, 2) * y + pow(r_x, 2)
        else:
            x += 1
            p = p + 2 * pow(r_y, 2) * x + pow(r_x, 2) - 2 * pow(r_x, 2) * y
        copypoints(points, x, y)
    return points


if __name__ == "__main__":
    print(mpe(8, 6, 0, 0))
