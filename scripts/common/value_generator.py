from decimal import Decimal


def generate_values(ranges):
    values = []
    if ranges and 'ranges' in ranges:
        for value_range_and_series in ranges['ranges']:
            series = value_range_and_series[0]
            values_range = decode_values_range(value_range_and_series[1])
            for mul in [Decimal('0.1'), 1, 10, 100, 1000, 10000, 100000, 1000000]:
                for series_value in series:
                    value = series_value * mul
                    if __in_range(value, values_range):
                        values.append(value)
        if 'extra_values' in ranges:
            values = values + ranges['extra_values']
    return values


def __in_range(value, values_range):
    min_operator = values_range['min_operator']
    max_operator = values_range['max_operator']
    if values_range['min_value'] == values_range['max_value'] and value == values_range['max_value']:
        return min_operator(value, values_range['min_value']) or max_operator(value, values_range['max_value'])
    else:
        return min_operator(value, values_range['min_value']) and max_operator(value, values_range['max_value'])


def decode_values_range(values_range_str):
    values_range_str = values_range_str.replace(' ', '')  # remove spaces
    values_range_splited = values_range_str.split(',')
    if len(values_range_splited) == 2:
        range_min_str = values_range_splited[0]
        range_max_str = values_range_splited[1]
        range_min_operator_str = range_min_str[:1]
        assert range_min_operator_str in ['(', '['], range_min_operator_str
        min_operator = greater_than if range_min_str[:1] == '(' else greater_or_equal
        min_value = Decimal(range_min_str[1:])

        range_max_operator_str = range_max_str[-1:]
        assert range_max_operator_str in [')', ']'], range_max_operator_str
        max_operaotr = less_than if range_max_operator_str == ')' else less_or_equal
        max_value = Decimal(range_max_str[:-1])
        return {'min_operator': min_operator, 'min_value': min_value,
                'max_operator': max_operaotr, 'max_value': max_value}


def greater_than(a, b):
    return a > b


def greater_or_equal(a, b):
    return a >= b


def less_than(a, b):
    return a < b


def less_or_equal(a, b):
    return a <= b



