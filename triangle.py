import sys
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y


class Triangle:
    def __init__(self, a, b, c):
        self.a_crds = a
        self.b_crds = b
        self.c_crds = c
        self.a = sqrt((b.x - c.x) ** 2 + (b.y - c.y) ** 2)
        self.b = sqrt((a.x - c.x) ** 2 + (a.y - c.y) ** 2)
        self.c = sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)

    def __str__(self):
        return f"{self.a_crds.x} {self.a_crds.y} {self.b_crds.x} {self.b_crds.y} {self.c_crds.x} {self.c_crds.y}"

    def is_triangle(self):
        return (self.a < self.b + self.c) and (self.b < self.c + self.a) and (self.c < self.a + self.b)

    def is_rb(self):
        return (self.a == self.b) or (self.b == self.c) or (self.c == self.a)

    def square(self):
        if self.is_triangle() and self.is_rb():
            p = (self.a + self.b + self.c) / 2
            s = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
            return s
        return -1


def read_data(filename):
    res_data = list()
    with open(filename) as f:
        data = list(map(lambda x: x.strip('\n').split(), f.readlines()))
        k = len(data)
        for i in range(k):
            is_num_row = True
            if len(data[i]) == 6:
                for j in range(6):
                    try:
                        data[i][j] = float(data[i][j])
                    except ValueError:
                        is_num_row = False
                if is_num_row:
                    res_data.append(data[i])
    return res_data


def write_data(filename, data):
    mx_sq = 0
    res_triangle = None
    for line in data:
        triangle = Triangle(Point(line[0], line[1]),
                            Point(line[2], line[3]),
                            Point(line[4], line[5]))
        if triangle.square() > mx_sq:
            mx_sq = triangle.square()
            res_triangle = triangle

    with open(filename, 'w') as f:
        if mx_sq != 0:
            f.write(str(triangle))


def main(src, dst):
    src = read_data(src)
    write_data(dst, src)


if __name__ == "__main__":
    params = sys.argv
    main(params[1], params[2])

# triangle.py in.txt out.txt
