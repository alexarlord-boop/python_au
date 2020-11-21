import sys


class Point():
    pass


class Triangle():
    pass


def read_data(filename):
    data = list()
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


def write_data(filename):
    pass


def main(src, dst):
    src = read_data(src)
    print(src)


if __name__ == "__main__":
    params = sys.argv
    main(params[1], params[2])

#triangle.py in.txt out.txt
