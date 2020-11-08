import numpy as np


def copypoints(points: list, x, y):
    a = np.array([[x, y], [y, x], [x, -y], [y, -x],
                  [-x, y], [-y, x], [-x, -y], [-y, -x]])
    a = np.unique(a, axis=0)
    for i in a.tolist():
        points.append(i)


def mpc(r, x_c, y_c):
    points = []
    copypoints(points, 0, r)
    p = 5/4 - r
    x, y = 0, r
    #x, y = points[-1][0], points[-1][1]
    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * x + 1 - 2 * y
        copypoints(points, x, y)
    points = np.array(points) + np.array([x_c, y_c])
    return points.tolist()


if __name__ == "__main__":
    print(mpc(10, 0, 0))
