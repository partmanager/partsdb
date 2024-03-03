import decimal
from capacitors.capacitor_generator_base import CapacitorGeneratorBase
from common.csv_utils import load_csv_data

voltage_code = {'6.3V': 'Y', '10V': 'Q', '16V': 'J', '25V': 'X', '50V': 'A', '100V': 'B'}
tolerance = {'B': '±0.10pF', 'C': '±0.25pF', 'D': '±0.50pF', 'F': '±1%', 'G': '±2%', 'J': '±5%', 'K': '±10%'}
packing = {'C': {'Packaging Code': 'C',
                 'Packaging Type': 'Paper Tape / Reel',
                 'Packaging Data': {
                    'Reel Diameter': '7"'}
                 },
           'P': {'Packaging Code': 'P',
                 'Packaging Type': 'Paper Tape / Reel',
                 'Packaging Data': {
                     'Reel Diameter': '13"'}
                 },
           'T': {'Packaging Code': 'T',
                 'Packaging Type': 'Embossed Tape / Reel',
                 'Packaging Data': {
                    'Reel Diameter': '7"'}
                 },
           'R': {'Packaging Code': 'R',
                 'Packaging Type': 'Embossed Tape / Reel',
                 'Packaging Data': {
                     'Reel Diameter': '13"'}
                 }
           }


def get_packing_codes(case_code, thickness_code):
    if case_code == '0402':
        if thickness_code == 'N':
            return ['C', 'P']
        elif thickness_code == 'E':
            return ['E']
    if case_code == '0603':
        if thickness_code in ['S', 'X', "X’"]:
            return ['C', 'P']
    if case_code == '0805':
        if thickness_code in ['A', 'B', 'T']:
            return ['C', 'P']
        elif thickness_code in ['D', 'I']:
            return ['T', 'R']
    if case_code == '1206':
        if thickness_code == 'B':
            return ['C', 'P']
        elif thickness_code in ['C', 'J', 'D']:
            return ['T', 'R']
        elif thickness_code in ['G', 'P']:
            return ['T']
    if case_code == '1210':
        if thickness_code in ['C', 'D']:
            return ['T', 'R']
        elif thickness_code in ['G', 'K', 'M']:
            return ['T']


def get_tolerance(capacitance):
    if 'pF' in capacitance and decimal.Decimal(capacitance.replace('pF', '')) < 10:
        return ['B', 'C', 'D']
    else:
        return ['F', 'G', 'J', 'K']


def get_package_size(case_code, thickness_code):
    if case_code == '0402':
        if thickness_code == 'N':
            return {"Length": '1.00mm ±0.05mm', "Width": '0.50mm ±0.05mm', "Height": '0.50mm ±0.05mm', 'e': '0.25mm +0.05/-0.10mm'}
        elif thickness_code == 'E':
            return {"Length": '1.00mm ±0.20mm', "Width": '0.50mm ±0.20mm', "Height": '0.50mm ±0.20mm',
                    'e': '0.25mm +0.05/-0.10mm'}
    if case_code == '0603':
        if thickness_code == 'S':
            return {"Length": '1.60mm ±0.10mm', "Width": '0.80mm ±0.10mm', "Height": '0.80mm ±0.07mm',
                    'e': '0.40mm ±0.15mm'}
        elif thickness_code == 'X':
            return {"Length": '1.60mm +0.15/-0.10mm', "Width": '0.80mm +0.15/-0.10mm', "Height": '0.80mm +0.15/-0.10mm',
                    'e': '0.40mm ±0.15mm'}
        elif thickness_code == "X’":
            return {"Length": '1.60mm ±0.2mm', "Width": '0.80mm ±0.2mm', "Height": '0.80mm ±0.2mm',
                    'e': '0.40mm ±0.15mm'}
    if case_code == '0805':
        if thickness_code == 'A':
            return {"Length": '2.00mm ±0.15mm', "Width": '1.25mm ±0.1mm', "Height": '0.60mm ±0.1mm',
                    'e': '0.50mm ±0.2mm'}
        elif thickness_code == 'B':
            return {"Length": '2.00mm ±0.15mm', "Width": '1.25mm ±0.1mm', "Height": '0.80mm ±0.1mm',
                    'e': '0.50mm ±0.2mm'}
        elif thickness_code == 'D':
            return {"Length": '2.00mm ±0.15mm', "Width": '1.25mm ±0.1mm', "Height": '1.25mm ±0.1mm',
                    'e': '0.50mm ±0.2mm'}
        elif thickness_code == 'T':
            return {"Length": '2.00mm ±0.2mm', "Width": '1.25mm ±0.2mm', "Height": '0.85mm ±0.1mm',
                    'e': '0.50mm ±0.2mm'}
        elif thickness_code == 'I':
            return {"Length": '2.00mm ±0.2mm', "Width": '1.25mm ±0.2mm', "Height": '1.25mm ±0.2mm',
                    'e': '0.50mm ±0.2mm'}
    if case_code == '1206':
        if thickness_code == 'B':
            return {"Length": '3.20mm ±0.15mm', "Width": '1.60mm ±0.15mm', "Height": '0.80mm ±0.1mm',
                    'e': '0.60mm ±0.2mm'}
        elif thickness_code == 'C':
            return {"Length": '3.20mm ±0.15mm', "Width": '1.60mm ±0.15mm', "Height": '0.95mm ±0.1mm',
                    'e': '0.60mm ±0.2mm'}
        elif thickness_code == 'D':
            return {"Length": '3.20mm ±0.15mm', "Width": '1.60mm ±0.15mm', "Height": '1.25mm ±0.1mm',
                    'e': '0.60mm ±0.2mm'}
        elif thickness_code == 'J':
            return {"Length": '3.20mm ±0.20mm', "Width": '1.60mm ±0.15mm', "Height": '1.15mm ±0.15mm',
                    'e': '0.60mm ±0.2mm'}
        elif thickness_code == 'G':
            return {"Length": '3.20mm ±0.20mm', "Width": '1.60mm ±0.2mm', "Height": '1.6mm ±0.2mm',
                    'e': '0.60mm ±0.2mm'}
        elif thickness_code == 'P':
            return {"Length": '3.20mm +0.30/-0.1mm', "Width": '1.60mm +0.3/-0.1mm', "Height": '1.6mm +0.30/-0.1mm',
                    'e': '0.60mm ±0.2mm'}
    if case_code == '1210':
        if thickness_code == 'C':
            return {"Length": '3.20mm ±0.30mm', "Width": '2.50mm ±0.20mm', "Height": '0.95mm ±0.1mm',
                    'e': '0.75mm ±0.25mm'}
        elif thickness_code == 'D':
            return {"Length": '3.20mm ±0.30mm', "Width": '2.50mm ±0.20mm', "Height": '1.25mm ±0.1mm',
                    'e': '0.75mm ±0.25mm'}
        elif thickness_code == 'G':
            return {"Length": '3.20mm ±0.40mm', "Width": '2.50mm ±0.30mm', "Height": '1.60mm ±0.2mm',
                    'e': '0.75mm ±0.25mm'}
        elif thickness_code == 'K':
            return {"Length": '3.20mm ±0.40mm', "Width": '2.50mm ±0.30mm', "Height": '2.00mm ±0.2mm',
                    'e': '0.75mm ±0.25mm'}
        elif thickness_code == 'M':
            return {"Length": '3.20mm ±0.40mm', "Width": '2.50mm ±0.30mm', "Height": '2.50mm ±0.3mm',
                    'e': '0.75mm ±0.25mm'}


class VishayCapacitorConverter(CapacitorGeneratorBase):
    def __init__(self, src_filename, parameters):
        super().__init__(manufacturer='Vishay')
        self.capacitor_data = load_csv_data(src_filename)
        self.parameters = parameters

    def generate_capacitor(self):
        for capacitor in self.capacitor_data:
            for case_size_key in capacitor:
                if case_size_key not in ['Capacitance Code', 'Capacitance']:
                    case_height = capacitor[case_size_key]
                    if case_height:
                        case_code, voltage = case_size_key.split(' ')
                        capacitance = capacitor['Capacitance']
                        capacitance_code = capacitor['Capacitance Code']
                        dielectric_code = {'C0G': 'A', 'X7R': 'Y'}[self.parameters['Dielectric Type']]
                        if '/' in case_height:
                            case_height = case_height[0]
                        if len(case_height) > 1 and case_height[-1] != "’":
                            tolerances = {'1': ['B', 'C', 'D', 'F', 'G', 'K'], '2': ['K'], '3': ['M']}
                            allowed_tolerance = tolerances[case_height[-1]]
                            case_height = case_height[:-1]
                        else:
                            allowed_tolerance = ['B', 'C', 'D', 'F', 'G', 'J','K']
                        for capacitance_tolerance_code in get_tolerance(capacitance):
                            if capacitance_tolerance_code not in allowed_tolerance:
                                continue
                            if case_height == 'T' and capacitance_tolerance_code != 'J':
                                continue
                            if case_height == 'P' and voltage in ['25V', '50V'] and capacitance_tolerance_code != 'J':
                                continue

                            partnumber = f"VJ{case_code}{dielectric_code}{capacitance_code}{capacitance_tolerance_code}X{voltage_code[voltage]}#W1BC"

                            parameters = {
                                'Working Temp Range': '-55°C ~ 125°C',
                                'Capacitance': self.encode_parameter(value=capacitance,
                                                                     tolerance=tolerance[capacitance_tolerance_code]),
                                'Dielectric Type': self.parameters['Dielectric Type'],
                                'Rated Voltage': self.encode_parameter(value='max. {}'.format(voltage))
                            }

                            for packing_code in get_packing_codes(case_code, case_height):
                                ordernumber = partnumber.replace('#', packing_code)

                                part = {
                                    'manufacturer': self.manufacturer,
                                    'partNumber': partnumber,
                                    'productionStatus': None,
                                    'markingCode': None,
                                    'partType': 'MLCC',
                                    'series': {'name': 'VJ...W1BC', 'description': 'Basic Commodity Series'},
                                    'description': None,
                                    'productUrl': None,
                                    'notes': None,
                                    'tags': [],
                                    'storageConditions': {'temperature': '-40°C ~ 105°C',
                                                          'humidity': '',
                                                          'MSLevel': ''},
                                    'parameters': parameters,
                                    'files': self.get_files(partnumber, ordernumber),
                                    'package': {'type': 'Chip ' + case_code,
                                                'dimensions': get_package_size(case_code, case_height)
                                                },
                                    'symbol&footprint': {'symbolName': 'capacitor_nonpolar',
                                                         'pinmap': {},
                                                         'footprints': []},
                                    'orderNumbers': {ordernumber: packing[packing_code]}
                                }
                                self.validate_part(part)
                                self.create_or_update_part(part)
