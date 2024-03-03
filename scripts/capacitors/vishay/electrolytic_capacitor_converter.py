import pandas as pd
from capacitors.capacitor_generator_base import CapacitorGeneratorBase


class VishayElectrolyticCapacitorConverter(CapacitorGeneratorBase):
    def __init__(self, src_filename, parameters):
        super().__init__(manufacturer='Vishay')
        df = pd.read_excel(src_filename)
        self.capacitor_data = df.to_dict(orient='index')
        self.parameters = parameters

    def generate_capacitor(self):
        case_code_map = {"4 x 5.7": "AB",
                         "5 x 5.7": "AC",
                         "6.3 x 5.7": "AD",
                         "6.3 x 7.7": "BM",
                         "8 x 6.5": "AE",
                         "8 x 10": "AF",
                         "10 x 7.7": "XM",
                         "10 x 10": "AG",
                         "12.5 x 13.5": "AH",
                         "12.5 x 16": "CX",
                         "16 x 16.5": "AK",
                         "16 x 21.5": "AM",
                         "18 x 16.5": "AN",
                         "18 x 21.5": "AP"}
        for i in self.capacitor_data:
            capacitors_data = self.capacitor_data[i]
            capacitance_code = capacitors_data['Capacitance Code']
            capacitance = capacitors_data['Capacitance']
            for case_size_key in capacitors_data:
                if case_size_key not in ['Capacitance Code', 'Capacitance'] and not case_size_key.endswith('mA'):
                    case_dimensions = capacitors_data[case_size_key]
                    if case_dimensions and isinstance(case_dimensions, str):
                        voltage_data, unused = case_size_key.split('|')
                        voltage_data = voltage_data.strip()
                        voltage, voltage_code = voltage_data.split(' ')
                        voltage = voltage.strip()
                        voltage_code = voltage_code.strip().replace('(', '').replace(')', '')

                        dimensions_code = case_code_map[case_dimensions]
                        packaging_code = 'AR'
                        internal_code = 'L'
                        partnumber = f"GSC00{dimensions_code}{capacitance_code}{voltage_code}##{internal_code}"
                        ordernumber = f"GSC00{dimensions_code}{capacitance_code}{voltage_code}{packaging_code}{internal_code}"

                        parameters = {
                            'Capacitance': self.encode_parameter(value=capacitance,
                                                                 tolerance=self.parameters['tolerance'],
                                                                 unit='uF'),
                            'Dielectric Type': self.parameters['Dielectric Type'],
                            'Rated Voltage': self.encode_parameter(value='max. {}'.format(voltage),
                                                                   unit='V')
                        }

                        part = {
                                'manufacturer': self.manufacturer,
                                'partNumber': partnumber,
                                'productionStatus': None,
                                'markingCode': None,
                                'partType': 'Aluminium Electrolytic Capacitor',
                                'series': {'name': self.parameters['Series']},
                                'description': None,
                                'productUrl': None,
                                'notes': None,
                                'tags': [],
                                'storageConditions': {'temperature': '',
                                                      'humidity': '',
                                                      'MSLevel': ''},
                                'parameters': parameters,
                                'files': self.get_files(partnumber, ordernumber),
                                'package': {'type': 'SMD',
                                            'dimensions': {}
                                            },
                                'symbol&footprint': {'symbolName': 'capacitor_polar',
                                                     'pinmap': {},
                                                     'footprints': []},
                                'orderNumbers': {ordernumber: {}}
                        }
                        self.validate_part(part)
                        self.create_or_update_part(part)
