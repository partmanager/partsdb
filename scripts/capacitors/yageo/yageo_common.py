import csv
import decimal
from math import log10


tolerance_code = {'±0.1pF': 'B', '±0.25pF': 'C', '±0.5pF': 'D', '±1%': 'F', '±2%': 'G', '±5%': 'J', '±10%': 'K', '±20%': 'M', '-20%/+80%': 'Z'}
voltage_code = {'6.3': '5', '10': '6', '16': '7', '25': '8', '50': '9', '100': '0', '200': 'A', '250': 'Y', '500': 'B', '630': 'Z'}

packing_style = {'R': {'Packaging Code': 'R', 'Packaging Type': 'Paper Tape / Reel',
                       'Packaging Data': {
                           'Reel Diameter': '7"'
                       }},
                 'K': {'Packaging Code': 'K', 'Packaging Type': 'Embossed Tape / Reel',
                       'Packaging Data': {
                           'Reel Diameter': '7"'
                       }},
                 'P': {'Packaging Code': 'P', 'Packaging Type': 'Paper Tape / Reel',
                       'Packaging Data': {
                           'Reel Diameter': '13"'
                       }},
                 'F': {'Packaging Code': 'F', 'Packaging Type': 'Embossed Tape / Reel',
                       'Packaging Data': {
                           'Reel Diameter': '13"'
                       }},
                 'C': {'Packaging Code': 'C', 'Packaging Type': 'Bulk'}
                 }


def capacitance_to_str(resistance):
    numbers = int(log10(resistance))
    if numbers - 1 < 0:
        if numbers - 1 == -1:
            resistance_str = str(resistance * decimal.Decimal(f'1e{1 - numbers}')).rstrip('0').rstrip('.') + 'J'
    else:
        resistance_str = str(resistance * decimal.Decimal(f'1e{1 - numbers}')).rstrip('0').rstrip('.') + str(
            numbers - 1)
    return resistance_str


def load_capacitor_data(src_filename):
    data = []
    with open(src_filename) as csv_file:
        reader = csv.DictReader(csv_file)
        for line in reader:
            data.append(line)
    del data[0]  # remove info line
    return data


def decode_case_and_volgage(case_and_voltage):
    case_voltage = case_and_voltage.split('|')
    case = case_voltage[0].strip()
    voltage = decimal.Decimal(case_voltage[1].replace('V', ''))
    return [case, voltage]