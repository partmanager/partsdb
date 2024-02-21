from decimal import Decimal
from math import log10

#header = csv_headers.header + ['Resistance', 'Rated Power', 'TCR',
#                               'Working Voltage', 'Overload Voltage',
#                               'Dielectric Withstanding Voltage', 'Packaging Code', 'Packaging Type', 'Packaging Qty']

#resistor_array_header = csv_headers.header + ['Elements Count', 'Resistance', 'Temperature Coefficient of Resistance',
#                                              'Power Rating Per Resistor', 'Power Rating Package', 'Working Voltage',
#                                              'Overload Voltage', 'Dielectric Withstanding Voltage']

#resistor_radial_header = header + ['Length', 'Diameter', 'Lead diameter', 'Lead length', 'Lead spacing']

#resistor_melf_header = header + ['Length', 'Diameter', 'K']

resistor_tolerance = {'L': '0.01%', 'P': '0.02%', 'W': '0.05%', 'B': '0.1%', 'C': '0.25%', 'D': '0.5%', 'F': '1%',
                      'G': '2%', 'J': '5%'}


def generate_resistance_values(resistance_range):
    if resistance_range:
        values = []
        for mul in [Decimal('0.1'), 1, 10, 100, 1000, 10000, 100000, 1000000]:
            for series_value in resistance_range[0]:
                value = series_value * mul
                if resistance_range[1] <= value <= resistance_range[2]:
                    values.append(value)
        return values
    return []


def resistance_to_str(resistance):
    if resistance < 1000:
        resistance_str = str(resistance).replace('.', 'R').strip('0')
        return resistance_str  # + '0' * (4-len(resistance_str))
    if resistance < 1000000:
        return str(resistance / 1000).replace('.', 'K').strip('0')
    else:
        return str(resistance / 1000000).replace('.', 'M').strip('0')


def resistance_to_str_v2(resistance):
    numbers = int(log10(resistance))
    if resistance < 100:
        resistance_str = str(resistance).rstrip('0').rstrip('.')
        if '.' in resistance_str:
            resistance_str = resistance_str.replace('.', 'R')
        else:
            resistance_str = resistance_str + '0'
    else:
        resistance_str = str(resistance * Decimal(f'1e{2 - numbers}')).rstrip('0').rstrip('.') + str(
            numbers - 2)
    return resistance_str


def resistance_to_str_v3(resistance):
    numbers = int(log10(resistance))
    if resistance < 100:
        resistance_str = str(resistance).rstrip('0').rstrip('.')
        if '.' in resistance_str:
            resistance_str = resistance_str.replace('.', 'R')
        else:
            resistance_str = resistance_str + 'R'
    else:
        resistance_str = str(resistance * Decimal(f'1e{2 - numbers}')).rstrip('0').rstrip('.') + str(
            numbers - 2)
    return resistance_str


def resistance_to_str_multiplier_coma(resistance, digits=3, multiplier_str=None):
    if multiplier_str is None:
        multiplier_str = {-3: '7', -2: '8', -1: '9', 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
    numbers = int(log10(resistance))
    multiplier = numbers - digits + 1
    # print(resistance, "Multiplier", multiplier, multiplier_str[multiplier])
    if multiplier == -1:
        resistance_str = "{:.1f}".format(resistance).replace('.', 'R')
        return resistance_str
    elif multiplier == -2:
        resistance_str = "{:.2f}".format(resistance).replace('.', 'R')
        return resistance_str
    else:
        resistance_str = "{:.2f}".format(resistance * Decimal(f'1e{multiplier * -1}'))
        return resistance_str.rstrip('0').rstrip('.') + multiplier_str[multiplier]


def resistance_to_str_multiplier(resistance, digits=3, multiplier_str=None):
    if multiplier_str is None:
        multiplier_str = {-3: '7', -2: '8', -1: '9', 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
    numbers = int(log10(resistance))
    multiplier = numbers - digits + 1
#    print("Multiplier", multiplier, multiplier_str[multiplier], 'Resistance', resistance, "numbers", log10(resistance))
    resistance_str = "{:.2f}".format(resistance * Decimal(f'1e{multiplier * -1}'))
    resistance_str = resistance_str.rstrip('0').rstrip('.') + multiplier_str[multiplier]
    assert '.' not in resistance_str
    return resistance_str


def test_resistance_to_string():
    print(resistance_to_str_multiplier(1))
    print(resistance_to_str_multiplier(Decimal('51.1')))
    print(resistance_to_str_multiplier(1000))

    print("resistance_to_str_multiplier_coma", resistance_to_str_multiplier_coma(91))
    print("resistance_to_str_multiplier_coma", resistance_to_str_multiplier_coma(91, digits=2))
    print("resistance_to_str_multiplier_coma", resistance_to_str_multiplier_coma(9.09))
    print("resistance_to_str_multiplier_coma", resistance_to_str_multiplier_coma(9.09, digits=2))
