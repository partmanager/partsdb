import decimal
from capacitors.capacitor_generator_base import CapacitorGeneratorBase
from common.csv_utils import load_csv_data


def decode_dimensions(size):
    pin_pitch = {'5': '2.0mm', '6.3': '2.5mm', '8': '3.5mm', '10': '5.0mm', '12.5': '5.0mm', '16': '7.5mm',
                 '18': '7.5mm', '22': '10.0mm'}
    pin_diameter = {'5': '0.5mm', '6.3': '0.5mm', '8': '0.6mm', '10': '0.6mm', '12.5': '0.6mm', '16': '0.8mm',
                    '18': '0.8mm', '22': '0.8mm'}
    diameter_length = size.split('×')
    return {'Diameter': diameter_length[0],
            'Length': diameter_length[1],
            'Pin Diameter': pin_diameter[diameter_length[0]],
            'Pin Pitch': pin_pitch[diameter_length[0]]}


def voltage_from_str(voltage_str):
    voltage = voltage_str.replace('(0J)', '').replace('(1A)', '').replace('(1C)', '').replace('(1E)', '').replace(
        '(1V)', '').replace('(1H)', '').replace('(1J)', '').replace('(1K)', '').replace('(2C)', '').replace(
        '(2D)', '').replace('(2E)', '').replace('(2H)', '').replace('(2W)', '').replace('(2G)', '').replace('(2V)', '')
    return decimal.Decimal(voltage)


def temperature_range(voltage):
    if voltage <= 400:
        return ['-40', '105']
    else:
        return ['-25', '105']


class AishiCapacitorConverter(CapacitorGeneratorBase):
    def __init__(self, src_filename):
        super().__init__(manufacturer='Aishi')
        self.capacitor_data = load_csv_data(src_filename)

    def generate_capacitor(self):
        for capacitor in self.capacitor_data:
            print(capacitor)
            partnumber = capacitor['Part Number']
            ordernumber = partnumber
            dimensions = decode_dimensions(capacitor['Size ΦdxL(mm)'])
            voltage = voltage_from_str(capacitor['WV (V dc )'])
            temperature = temperature_range(voltage)

            parameters = {
                'Working Temp Range': '{}°C ~ {}°C'.format(temperature[0], temperature[1]),
                'Capacitance': self.encode_parameter(value=capacitor['Cap (μF)'] + 'μF', tolerance='±20%'),
                'Dielectric Type': 'Aluminium Oxide',
                'Rated Voltage': self.encode_parameter(value='max. {}V'.format(voltage)),
                'Dissipation Factor': self.encode_parameter(value=capacitor['tanδ']),
                'Rated Ripple Current': self.encode_parameter(
                    value='max. {}mA'.format(capacitor['Rated ripple current (mArms/105°C, 120Hz)']),
                    conditions={'f': '120Hz', 'T_A': '105°C'}),
                'Endurance': self.encode_parameter(value='2000h')}

            part = {
                'manufacturer': self.manufacturer,
                'partNumber': partnumber,
                'productionStatus': None,
                'markingCode': None,
                'partType': 'Aluminium Electrolytic Capacitor',
                'series': {'name': 'WH', 'description': 'Miniature aluminium electrolytic capacitors'},
                'description': None,
                'productUrl': None,
                'notes': '',
                'tags': [],
                'storageConditions': {'temperature': '-40°C ~ 105°C',
                                      'humidity': '',
                                      'MSLevel': ''},
                'parameters': parameters,
                'files': self.get_files(partnumber, ordernumber),
                'package': {'type': 'Radial',
                            'dimensions': {'Length': dimensions['Length'] + 'mm',
                                           'Diameter': dimensions['Diameter'] + 'mm',
                                           'Pitch': dimensions['Pin Pitch'],
                                           'Pin Diameter': dimensions['Pin Diameter']}
                            },
                'symbol&footprint': {'symbolName': 'capacitor_electrolytic',
                                     'pinmap': {},
                                     'footprints': []},
                'orderNumbers': {ordernumber: None}
            }
            self.validate_part(part)
            self.create_or_update_part(part)
