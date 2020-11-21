import sys


class Point():
    pass


class Triangle():
    pass


def read_data(filename):
    data = list()
    with open(filename) as f:
        data = list(map(lambda x: x.strip('\n').split(), f.readlines()))
        k = len(data)
        for i in range(k):
            data[i] = list(map(int, data[i]))
    return data


def write_data(filename):
    pass


def main(src, dst):
    src = read_data(src)
    print(src)


if __name__ == "__main__":
    params = sys.argv
    main(params[1], params[2])

#triangle.py in.txt out.txt
