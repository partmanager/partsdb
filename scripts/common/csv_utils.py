import csv


def load_csv_data(filename):
    data = []
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        for line in reader:
            # print(line)
            data.append(line)
    return data


def encode_parameter_list(parameter_list, condition):
    result_str = ''
    for i, parameter in enumerate(parameter_list):
        if i > 0:
            result_str = result_str + ' | '
        if condition:
            result_str = result_str + parameter.replace('@ ', '@ ' + condition + '=')
        else:
            result_str = result_str + parameter
    return result_str
