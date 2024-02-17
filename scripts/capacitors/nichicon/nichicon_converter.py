import decimal
from capacitors.capacitor_generator_base import CapacitorGeneratorBase
from common.csv_utils import load_csv_data


def generate_dimensions(size):
    pin_pitch = {'5': '2.0mm', '6.3': '2.5mm', '8': '3.5mm', '10': '5.0mm', '12.5': '5.0mm', '16': '7.5mm',
                 '18': '7.5mm', '20': '10.0mm', '22': '10.0mm', '25': '12.5mm'}
    pin_diameter_table = {'5': '0.5mm', '6.3': '0.5mm', '8': '0.6mm', '10': '0.6mm', '12.5': '0.6mm', '16': '0.8mm',
                          '18': '0.8mm', '20': '1mm', '22': '1mm', '25': '1mm'}
    diameter_length = size.strip().split('×')
    diameter_length[0] = diameter_length[0].strip()
    diameter_length[1] = diameter_length[1].strip()

    if diameter_length[0] == '12.5':
        if float(diameter_length[1]) > 25:
            pin_diameter = '0.8mm'
        else:
            pin_diameter = '0.6mm'
    else:
        pin_diameter = pin_diameter_table[diameter_length[0]]

    return {'Diameter': diameter_length[0],
            'Length': diameter_length[1],
            'Pin Diameter': pin_diameter,
            'Pitch': pin_pitch[diameter_length[0]]}


def get_temperature(voltage):
    if voltage <= 100:
        return {'Working Temp Min': '-55', 'Working Temp Max': '105'}
    elif voltage <= 400:
        return {'Working Temp Min': '-40', 'Working Temp Max': '105'}
    elif voltage <= 450:
        return {'Working Temp Min': '-25', 'Working Temp Max': '105'}


class NichiconCapacitorConverter(CapacitorGeneratorBase):
    def __init__(self, src_filename, parameters):
        super().__init__(manufacturer='Nichicon')
        self.capacitor_data = load_csv_data(src_filename)
        self.parameters = parameters

    def generate_capacitor(self):
        for capacitor in self.capacitor_data:
            if capacitor['Case size φD × L  (mm)']:
                print(capacitor)
                diameter = capacitor['Case size φD × L  (mm)'].split('×')[0].strip()
                series = self.parameters['Series']
                voltage_code = capacitor['Voltage code']
                voltage = decimal.Decimal(capacitor['Voltage'].replace('V', ''))
                capacitance_code = capacitor['Cap (code)']
                configuration_code = {'5': 'DD', '6.3': 'ED', '8': 'PD', '10': 'PD', '12.5': 'HD', '16': 'HD',
                                      '18': 'HD', '20': 'RD', '22': 'RD', '25': 'RD'}
                capacitance_tolerance_code = 'M'
                partnumber = f"U{series}{voltage_code}{capacitance_code}{capacitance_tolerance_code}{configuration_code[diameter]}"
                ordernumber = partnumber

                parameters = {
                    'Working Temp Range': get_temperature(voltage),
                    'Capacitance': self.encode_parameter(value=capacitor['Cap (uF)'] + 'μF', tolerance='±20%'),
                    'Dielectric Type': 'Aluminium Oxide',
                    'Rated Voltage': self.encode_parameter(value='max. {}'.format(capacitor['Voltage'])),
                    'Rated Ripple Current': self.encode_parameter(value='max. {}mA'.format(capacitor['Rated ripple'])),
                    'Endurance': self.encode_parameter(value=self.parameters['Endurance'])
                }

                part = {
                    'manufacturer': self.manufacturer,
                    'partNumber': partnumber,
                    'productionStatus': None,
                    'markingCode': None,
                    'partType': 'Aluminium Electrolytic Capacitor',
                    'series': {'name': series, 'description': self.parameters['Series Description']},
                    'description': None,
                    'productUrl': None,
                    'notes': None,
                    'tags': [],
                    'storageConditions': {'temperature': '-40°C ~ 105°C',
                                          'humidity': '',
                                          'MSLevel': ''},
                    'parameters': parameters,
                    'files': self.get_files(partnumber, ordernumber),
                    'package': {'type': 'Radial',
                                'dimensions': generate_dimensions(capacitor['Case size φD × L  (mm)'].strip())
                                },
                    'symbol&footprint': {'symbolName': 'capacitor_nonpolar',
                                         'pinmap': {},
                                         'footprints': []},
                    'orderNumbers': {ordernumber: {}}
                }
                self.validate_part(part)
                self.create_or_update_part(part)
