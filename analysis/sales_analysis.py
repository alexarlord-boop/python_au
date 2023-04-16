import datetime
from datetime import datetime as dt


def get_data(filename):
    with open(filename) as f:
        return list(map(lambda x: x.strip().split(','), f.readlines()))


def parse_data(data):
    headers = data[0]
    return list(map(lambda x: dict(zip(headers, x)), data[1::]))


def get_expr(key, x, value, arg):
    if key == 'date':
        arg_option = {'gt': convert_to_date(x[key]) > convert_to_date(value) if x[key] != '' else None,
                      'lt': convert_to_date(x[key]) < convert_to_date(value) if x[key] != '' else None,
                      'exact': convert_to_date(x[key]) == convert_to_date(value) if x[key] != '' else None}
        return arg_option[arg]
    if key in ['resource', 'count']:
        arg_option = {'gt': int(x[key]) > value if x[key] != '' else None,
                      'lt': int(x[key]) < value if x[key] != '' else None,
                      'exact': int(x[key]) == value if x[key] != '' else None}
        return arg_option[arg]
    if key == 'staff_id':
        arg_option = {'exact': value == x[key],
                      'in': value in x[key]}
        return arg_option[arg]


def filter_data_by(data, key, value, arg):
    return list(filter(lambda x: get_expr(key, x, value, arg), data))


def convert_to_date(date):
    return dt.strptime(date, "%Y-%m")


def sort_data_by(data, key):
    if key in ['resource', 'count']:
        return sorted(data, key=lambda x: int(x[key] if x[key] != '' else 0))
    if key == 'staff_id':
        return sorted(data, key=lambda x: x[key].strip())
    if key == 'date':
        return sorted(data,
                      key=lambda x: convert_to_date(x[key]) if x[key] != '' else datetime.datetime(1, 1, 1, 1, 1, 1, 1))


def main():
    data = parse_data(get_data('data.csv'))
    # print(sort_data_by(data), 'date'))
    # print(filter_data_by(data, 'date', '2020-6', 'lt'))
    # print(filter_data_by(data, 'staff_id', 'P', 'in'))


if __name__ == '__main__':
    main()
