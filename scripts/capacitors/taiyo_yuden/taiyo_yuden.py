import decimal
from capacitors.capacitor_generator_base import CapacitorGeneratorBase
from common.csv_utils import load_csv_data


class TaiyoYudenCapacitorConverter(CapacitorGeneratorBase):
    def __init__(self, src_filename):
        super().__init__(manufacturer='Taiyo Yuden')
        self.capacitor_data = load_csv_data(src_filename)

    def generate_capacitor(self):
        for capacitor in self.capacitor_data:
            capacitance = capacitor['Capacitance'].replace(' ', '')
            partnumber = capacitor['Previous Part Number'][:-1] + '#' if capacitor['Previous Part Number'] else capacitor['Part Number'][:-1] + '#'
            dissipation_factor = decimal.Decimal(capacitor['tanδ(max) [%]']) / 100 if capacitor['tanδ(max) [%]'] else None
            ordernumber = capacitor['Previous Part Number'] if capacitor['Previous Part Number'] else capacitor['Part Number']

            parameters = {
                'Working Temp Range': capacitor['Temp.[℃]'].replace(" to ", "℃ ~ ") + "℃",
                'Capacitance': self.encode_parameter(value=capacitance, tolerance=capacitor['Cap. Tole.'].replace(' ', '')),
                'Dielectric Type': capacitor['Temperature Characteristic'].replace("LowDistortionStandard", '').split('/')[0],
                'Rated Voltage': self.encode_parameter(value='max. {}V'.format(capacitor['Rated Volt.[Vdc]'])),
                'Dissipation Factor': self.encode_parameter(value=str(dissipation_factor)),
            }

            part = {
                'manufacturer': self.manufacturer,
                'partNumber': partnumber,
                'productionStatus': None,
                'markingCode': None,
                'partType': 'MLCC',
                'series': {'name': None, 'description': None},
                'description': None,
                'productUrl': None,
                'notes': None,
                'tags': [],
                'storageConditions': {'temperature': '-40°C ~ 105°C'},
                'parameters': parameters,
                'files': self.get_files(partnumber, ordernumber),
                'package': {'type': 'Chip ' + capacitor['Case Size(EIA/JIS)'].split('/')[0],
                            'dimensions': {'Length': capacitor['Dimension L'].replace(' ', 'mm ') + 'mm',
                                           'Width': capacitor['Dimension W'].replace(' ', 'mm ') + 'mm',
                                           'Height': capacitor['Dimension T'].replace(' ', 'mm ') + 'mm',
                                           'e': '',
                                           's': ''}
                            },
                'symbol&footprint': {'symbolName': 'capacitor_nonpolar',
                                     'pinmap': {},
                                     'footprints': []},
                'orderNumbers': {ordernumber: {}}
            }
            self.validate_part(part)
            self.create_or_update_part(part)
