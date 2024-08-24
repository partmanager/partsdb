import decimal
from capacitors.capacitor_generator_base import CapacitorGeneratorBase
from common.csv_utils import load_csv_data


voltage_code = {'6.3V': '0J', '10V': '1A', '16V': '1C', '20V': '1D', '25V': '1E', '35V': '1V', '40V': '1G', '50V': '1H',
                '63V': '1J', '80V': '1K', '100V': '2A'}

pitch_code = {'2.0mm': '020', '2.5mm': '025', '3.5mm': '035', '5.0mm': '050', '7.5mm': '075'}

dissipation_factor = {'6.3V': '0.22', '10V': '0.19', '16V': '0.16', '20V': '', '25V': '0.14', '35V': '0.12',
                      '40V': '', '50V': '0.10', '63V': '0.09', '80V': '', '100V': ''}

packaging_code = {'A': {'Packaging Code': 'A', 'Packaging Type': "Ammo"},
                  'B': {'Packaging Code': 'B', 'Packaging Type': "Bulk"}}


def decode_dimensions(size):
        pin_pitch = {'5': '2.0mm', '6.3': '2.5mm', '8': '3.5mm', '10': '5.0mm', '12.5': '5.0mm', '13': '5.0mm',
                     '16': '7.5mm', '18': '7.5mm', '22': '10.0mm'}
        pin_diameter = {'5': '0.5mm', '6.3': '0.5mm', '8A': '0.5mm', '8B': '0.6mm', '10': '0.6mm', '12.5': '0.6mm',
                        '13': '0.6mm', '16': '0.8mm', '18': '0.8mm', '22': '0.8mm'}
        diameter_length = size.split('x')
        correction = ''
        if decimal.Decimal(diameter_length[0]) == 8:
            if decimal.Decimal(diameter_length[1]) >= 16:
                correction = 'B'
            else:
                correction = 'A'
        return {'Diameter': diameter_length[0],
                'Length': diameter_length[1],
                'Pin Diameter': pin_diameter[diameter_length[0] + correction],
                'Pin Pitch': pin_pitch[diameter_length[0]]}


def voltage_from_str(voltage_str):
    #voltage = voltage_str.replace('(0J)', '').replace('(1A)', '').replace('(1C)', '').replace('(1E)', '').replace(
    #    '(1V)', '').replace('(1H)', '').replace('(1J)', '').replace('(1K)', '').replace('(2C)', '').replace(
    #    '(2D)', '').replace('(2E)', '').replace('(2H)', '').replace('(2W)', '').replace('(2G)', '').replace('(2V)', '')
    return decimal.Decimal(voltage_str.replace('V', ''))


def temperature_range(voltage):
    if voltage <= 400:
        return ['-40', '105']
    else:
        return ['-25', '105']


def encode_dimensions(dimensions):
    diameter = int(decimal.Decimal(dimensions['Diameter'].replace('mm', '')) * 10)
    length = int(decimal.Decimal(dimensions['Length'].replace('mm', '')) * 10)
    return "{:04d}{:04d}".format(diameter, length)


class JBCapacitorsConverter(CapacitorGeneratorBase):
    def __init__(self, src_filename, parameters):
        super().__init__(manufacturer='JB Capacitors')
        self.capacitor_data = load_csv_data(src_filename)
        self.parameters = parameters

    def generate_capacitor(self):
        for capacitor in self.capacitor_data:
            if capacitor['Size ØDxL (mm)']:
                generation_parameters = self.parameters
                dimensions = decode_dimensions(capacitor['Size ØDxL (mm)'])
                voltage = capacitor['Voltage']
                capacitance_code = '{:03d}'.format(int(capacitor['Capacitance Code'])) if "R" not in capacitor[
                    'Capacitance Code'] else capacitor['Capacitance Code']
                tolerance_code = 'M'
                lead_length = '000'
                partnumber = f"{generation_parameters['Series']}{voltage_code[voltage]}{capacitance_code}{tolerance_code}{pitch_code[dimensions['Pin Pitch']]}{encode_dimensions(dimensions)}{lead_length}#"

                parameters = {
                    'Working Temp Range': '-40°C ~ 105°C',
                    'Capacitance': self.encode_parameter(value=capacitor['Capacitance'] + 'μF', tolerance='±20%'),
                    'Dielectric Type': 'Aluminium Oxide',
                    'Rated Voltage': self.encode_parameter(value='max. {}'.format(voltage)),
                    'Dissipation Factor': self.encode_parameter(value=dissipation_factor[voltage]),
                    'Rated Ripple Current': self.encode_parameter(
                        value='max. {}mA'.format(capacitor['Ripple Current (mA rms, 105°C 100KHz)']),
                        conditions={'f': self.parameters['RippleCurrentCondFreq'],
                                    'T_A': self.parameters['RippleCurrentCondTemp']}),
                    'Endurance': self.encode_parameter(value='2000h')}

                for packaging in ['A', 'B']:
                    ordernumber = partnumber.replace('#', packaging)
                    packaging_type = packaging_code[packaging]
                    part = {
                        'manufacturer': self.manufacturer,
                        'partNumber': partnumber,
                        'productionStatus': None,
                        'markingCode': None,
                        'partType': 'Aluminium Electrolytic Capacitor',
                        'series': {'name': generation_parameters['Series'], 'description': None},
                        'description': None,
                        'productUrl': None,
                        'notes': '',
                        'tags': [],
                        'storageConditions': {'temperature': '-40°C ~ 105°C'},
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
                        'orderNumbers': {ordernumber: packaging_type}
                    }
                    self.validate_part(part)
                    self.create_or_update_part(part)
