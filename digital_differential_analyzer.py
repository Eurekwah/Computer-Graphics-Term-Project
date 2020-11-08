import round as rd
import time


def dda(x_0, y_0, x_e, y_e):
    dx, dy = x_e - x_0, y_e - y_0
    x, y = x_0, y_0
    steps = max(abs(dx), abs(dy))
    print(steps)
    points = []
    x_i, y_i = dx / steps, dy / steps
    for i in range(steps):
        x += x_i
        y += y_i
        #points.append([x, y])
        points.append([rd.round(x), rd.round(y)])
    return points


if __name__ == "__main__":
    print(dda(0, 0, -5, -3))
