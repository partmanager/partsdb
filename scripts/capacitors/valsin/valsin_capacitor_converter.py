import decimal
from capacitors.capacitor_generator_base import CapacitorGeneratorBase
from common.csv_utils import load_csv_data

voltage_code = {'4V': '4R0', '6.3V': '6R3', '10V': '100', '16V': '160', '25V': '250', '35V': '350', '50V': '500', '100V': '101'}
tolerance = {'A': '±0.05pF', 'B': '±0.10pF', 'C': '±0.25pF', 'D': '±0.50pF', 'F': '±1%', 'G': '±2%', 'J': '±5%',
             'K': '±10%', 'M': '±20%'}
packing = {'T': '7" reel', 'G': '13" reel'}

thickness_and_packaging = {
    '0201_L': {'case size': '0201', "Length": '0.60mm ±0.03mm', "Width": '0.30mm ±0.03mm', 'e': '0.10mm ±0.03mm', 'thickness': '0.30mm ±0.03mm', 'Paper quantity': [15000, 70000]},
    '0201_L1': {'case size': '0201', 'thickness': '0.30mm ±0.05mm', 'Paper quantity': [15000, None]},
    '0201_L2': {'case size': '0201', 'thickness': '0.30mm ±0.09mm', 'Paper quantity': [15000, None]},
    '0402_N': {'case size': '0402', "Length": '1.00mm ±0.05mm', "Width": '0.50mm ±0.05mm', 'e': '0.25mm +0.05/-0.10mm', 'thickness': '0.50mm ±0.05mm', 'Paper quantity': [10000, 50000]},
    '0402_Q': {'case size': '0402', "Length": '1.00mm ±0.05mm', "Width": '0.50mm ±0.05mm', 'e': '0.25mm +0.05/-0.10mm', 'thickness': '0.50mm +0.02/-0.05mm', 'Paper quantity': [10000, 50000]},
    '0402_E': {'case size': '0402', "Length": '1.00mm ±0.20mm', "Width": '0.50mm ±0.20mm', 'e': '0.25mm +0.05/-0.10mm', 'thickness': '0.50mm ±0.20mm', 'Paper quantity': [10000, None]},
    '0603_H': {'case size': '0603', "Length": '1.60mm +0.15/-0.10mm', "Width": '0.80mm 0.15/-0.10mm', 'e': '0.40mm ±0.15mm', 'thickness': '0.50mm ±0.10mm', 'Paper quantity': [4000, None]},
    '0603_S': {'case size': '0603', "Length": '1.60mm ±0.10mm', "Width": '0.80mm ±0.10mm', 'e': '0.40mm ±0.15mm', 'thickness': '0.80mm ±0.07mm', 'Paper quantity': [4000, 15000]},
    '0603_X': {'case size': '0603', "Length": '1.60mm +0.15/-0.10mm', "Width": '0.80mm 0.15/-0.10mm', 'e': '0.40mm ±0.15mm', 'thickness': '0.80mm +0.15/-0.10mm', 'Paper quantity': [4000, None]},
    '0603_X1': {'case size': '0603', "Length": '1.60mm ±0.20mm', "Width": '0.80mm ±0.20mm', 'e': '0.40mm ±0.15mm', 'thickness': '0.80mm ±0.20mm', 'Paper quantity': [4000, 15000]},
    '0805_H': {'case size': '0805', "Length": '2.00mm ±0.15mm', "Width": '1.25mm ±0.10mm', 'e': '0.50mm ±0.20mm', 'thickness': '0.50mm ±0.10mm', 'Paper quantity': [4000, 15000]},
    '0805_A': {'case size': '0805', "Length": '2.00mm ±0.15mm', "Width": '1.25mm ±0.10mm', 'e': '0.50mm ±0.20mm', 'thickness': '0.60mm ±0.10mm', 'Paper quantity': [4000, 15000]},
    '0805_B': {'case size': '0805', "Length": '2.00mm ±0.15mm', "Width": '1.25mm ±0.10mm', 'e': '0.50mm ±0.20mm', 'thickness': '0.80mm ±0.10mm', 'Paper quantity': [4000, 15000]},
    '0805_T': {'case size': '0805', "Length": '2.00mm ±0.20mm', "Width": '1.25mm ±0.20mm', 'e': '0.50mm ±0.20mm', 'thickness': '0.85mm ±0.10mm', 'Paper quantity': [4000, 15000]},
    '0805_D': {'case size': '0805', "Length": '2.00mm ±0.15mm', "Width": '1.25mm ±0.10mm', 'e': '0.50mm ±0.20mm', 'thickness': '1.25mm ±0.10mm', 'Plastic quantity': [3000, 10000]},
    '0805_I': {'case size': '0805', "Length": '2.00mm ±0.20mm', "Width": '1.25mm ±0.20mm', 'e': '0.50mm ±0.20mm', 'thickness': '1.25mm ±0.20mm', 'Plastic quantity': [3000, 10000]},
    '1206_B': {'case size': '1206', "Length": '3.20mm ±0.15mm', "Width": '1.60mm ±0.15mm', 'e': '0.60mm ±0.20mm', 'thickness': '0.80mm ±0.10mm', 'Paper quantity': [4000, 15000]},
    '1206_T': {'case size': '1206', "Length": '3.20mm ±0.20mm', "Width": '1.60mm ±0.20mm', 'e': '0.60mm ±0.20mm','thickness': '0.85mm ±0.10mm', 'Paper quantity': [4000, 10000]},
    '1206_C': {'case size': '1206', "Length": '3.20mm ±0.15mm', "Width": '1.60mm ±0.15mm', 'e': '0.60mm ±0.20mm', 'thickness': '0.95mm ±0.10mm', 'Plastic quantity': [3000, 10000]},
    '1206_J': {'case size': '1206', "Length": '3.20mm ±0.20mm', "Width": '1.60mm ±0.15mm', 'e': '0.60mm ±0.20mm', 'thickness': '1.15mm ±0.15mm', 'Plastic quantity': [3000, 10000]},
    '1206_D': {'case size': '1206', "Length": '3.20mm ±0.15mm', "Width": '1.60mm ±0.15mm', 'e': '0.60mm ±0.20mm', 'thickness': '1.25mm ±0.10mm', 'Plastic quantity': [3000, 10000]},
    '1206_G': {'case size': '1206', "Length": '3.20mm ±0.20mm', "Width": '1.60mm ±0.20mm', 'e': '0.60mm ±0.20mm', 'thickness': '1.60mm ±0.20mm', 'Plastic quantity': [2000, 10000]},
    '1206_P': {'case size': '1206', "Length": '3.20mm +0.30/-0.10mm', "Width": '1.60mm +0.30/-0.1mm', 'e': '0.60mm ±0.20mm', 'thickness': '1.6mm +0.30/-0.10mm', 'Plastic quantity': [2000, 9000]},
    '1210_T': {'case size': '1210', "Length": '3.20mm ±0.30mm', "Width": '2.50mm ±0.20mm', 'e': '0.75mm ±0.25mm', 'thickness': '0.85mm ±0.10mm', 'Plastic quantity': [3000, 10000]},
    '1210_C': {'case size': '1210', "Length": '3.20mm ±0.30mm', "Width": '2.50mm ±0.20mm', 'e': '0.75mm ±0.25mm', 'thickness': '0.95mm ±0.10mm', 'Plastic quantity': [3000, 10000]},
    '1210_D': {'case size': '1210', "Length": '3.20mm ±0.30mm', "Width": '2.50mm ±0.20mm', 'e': '0.75mm ±0.25mm', 'thickness': '1.25mm ±0.10mm', 'Plastic quantity': [3000, 10000]},
    '1210_G': {'case size': '1210', "Length": '3.20mm ±0.40mm', "Width": '2.50mm ±0.30mm', 'e': '0.75mm ±0.25mm', 'thickness': '1.60mm ±0.20mm', 'Plastic quantity': [2000, None]},
    '1210_K': {'case size': '1210', "Length": '3.20mm ±0.40mm', "Width": '2.50mm ±0.30mm', 'e': '0.75mm ±0.25mm', 'thickness': '2.00mm ±0.20mm', 'Plastic quantity': [1000, 6000]},
    '1210_M': {'case size': '1210', "Length": '3.20mm ±0.40mm', "Width": '2.50mm ±0.30mm', 'e': '0.75mm ±0.25mm', 'thickness': '2.50mm ±0.30mm', 'Plastic quantity': [1000, 6000]},
    '1808_D': {'case size': '1808', "Length": '4.50mm ±0.40mm', "Width": '2.03mm ±0.25mm', 'e': '0.75mm ±0.25mm', 'thickness': '1.25mm ±0.10mm', 'Plastic quantity': [2000, 10000]},
    '1808_F': {'case size': '1808', "Length": '4.50mm ±0.40mm', "Width": '2.03mm ±0.25mm', 'e': '0.75mm ±0.25mm', 'thickness': '1.10mm ±0.15mm', 'Plastic quantity': [2000, 10000]},
    '1808_G': {'case size': '1808', "Length": '4.50mm ±0.40mm', "Width": '2.03mm ±0.25mm', 'e': '0.75mm ±0.25mm', 'thickness': '1.60mm ±0.20mm', 'Plastic quantity': [2000, 8000]},
    '1808_K': {'case size': '1808', "Length": '4.50mm ±0.40mm', "Width": '2.03mm ±0.25mm', 'e': '0.75mm ±0.25mm', 'thickness': '2.00mm ±0.20mm', 'Plastic quantity': [1000, 6000]},
    '1812_D': {'case size': '1812', "Length": '4.50mm ±0.40mm', "Width": '3.20mm ±0.30mm', 'e': '0.75mm ±0.25mm', 'thickness': '1.25mm ±0.10mm', 'Plastic quantity': [1000, 5000]},
    '1812_G': {'case size': '1812', "Length": '4.50mm ±0.40mm', "Width": '3.20mm ±0.30mm', 'e': '0.75mm ±0.25mm', 'thickness': '1.60mm ±0.20mm', 'Plastic quantity': [1000, None]},
    '1812_K': {'case size': '1812', "Length": '4.50mm ±0.40mm', "Width": '3.20mm ±0.30mm', 'e': '0.75mm ±0.25mm', 'thickness': '2.00mm ±0.20mm', 'Plastic quantity': [1000, None]},
    '1812_M': {'case size': '1812', "Length": '4.50mm ±0.40mm', "Width": '3.20mm ±0.40mm', 'e': '0.75mm ±0.25mm', 'thickness': '2.50mm ±0.30mm', 'Plastic quantity': [500, 3000]},
    '1812_U': {'case size': '1812', "Length": '4.50mm ±0.40mm', "Width": '3.20mm ±0.40mm', 'e': '0.75mm ±0.25mm', 'thickness': '2.80mm ±0.30mm', 'Plastic quantity': [500, None]}}


def get_package_size(case_code, thickness_code):
    dimensions = thickness_and_packaging[case_code + "_" + thickness_code]
    return {"Length": dimensions["Length"], "Width": dimensions["Width"], 'e': dimensions['e'], 'Height': dimensions['thickness']}


def generate_packaging_info(case_code, thickness_code, packaging_code):
    packaging = thickness_and_packaging[case_code + "_" + thickness_code]
    seven_inch_or_13_inch = 0 if packaging_code == "T" else 1 # 0 for 7" 1 for 13"
    if 'Paper quantity' in packaging:
        return {'Packaging Qty': packaging['Paper quantity'][seven_inch_or_13_inch],
                'Packaging Type': 'Paper Tape / Reel',
                'Packaging Data': {
                    'Reel Diameter': '7"' if seven_inch_or_13_inch == 0 else '13"'}
                }
    elif 'Plastic quantity' in packaging:
        return {'Packaging Qty': packaging['Plastic quantity'][seven_inch_or_13_inch],
                'Packaging Type': 'Embossed Tape / Reel',
                'Packaging Data': {
                    'Reel Diameter': '7"' if seven_inch_or_13_inch == 0 else '13"'}
                }


class WalsinCapacitorConverter(CapacitorGeneratorBase):
    def __init__(self, src_filename, parameters):
        super().__init__(manufacturer='Walsin')
        self.capacitor_data = load_csv_data(src_filename)
        self.parameters = parameters
        self.dielectric_code = {'NP0': 'N', 'X5R': 'X', 'X7R': 'B'}

    def tolerances_for_capacitance(self, capacitance, dielectric, case_height):
        if dielectric == "NP0":
            if '*' in case_height:
                return ['J']
            else:
                if 'pF' in capacitance:
                    capacitance_decimal = decimal.Decimal(capacitance.replace('pF', '').replace(',', '.'))
                    if capacitance_decimal <= 5:
                        return ['A', 'B', 'C']
                    elif capacitance_decimal < 10:
                        return ["C", "D"]
                return ["F", "G", 'J', 'K']
        elif dielectric == 'X7R':
            if '*' in case_height:
                return ['J', 'M']
            else:
                return ['J', 'K', 'M']
        elif dielectric == 'Y5V':
            return ['M', 'Z']
        elif dielectric in ['X5R', 'X6S', 'X7S']:
            if '*' in case_height:
                return ['M']
            else:
                return ['K', 'M']

    def generate_capacitor(self):
        for capacitor in self.capacitor_data:
            for case_size_key in capacitor:
                if case_size_key not in ['Capacitance Code', 'Capacitance', 'Tolerance']:
                    case_height_annotated = capacitor[case_size_key]
                    if case_height_annotated:
                        case_code, voltage = case_size_key.split(' ')
                        capacitance = capacitor['Capacitance']
                        capacitance_code = capacitor['Capacitance Code'].replace("(", '').replace(")", '').replace("-",
                                                                                                                   "")
                        dielectric_code = self.dielectric_code[self.parameters['Dielectric Type']]
                        print(case_code, case_height_annotated, capacitance, self.parameters['Dielectric Type'])
                        for tolerance_code in self.tolerances_for_capacitance(capacitance,
                                                                              self.parameters['Dielectric Type'],
                                                                              case_height_annotated):
                            partnumber = f"{case_code}{dielectric_code}{capacitance_code}{tolerance_code}{voltage_code[voltage]}C#"
                            case_height = case_height_annotated.replace('*', '')

                            parameters = {
                                'Working Temp Range': '-55°C ~ 125°C',
                                'Capacitance': self.encode_parameter(value=capacitance.replace(',', '.'),
                                                                     tolerance=tolerance[tolerance_code]),
                                'Dielectric Type': self.parameters['Dielectric Type'],
                                'Rated Voltage': self.encode_parameter(value='max. {}'.format(voltage))
                            }
                            for packing_code in ['T', 'G']:
                                packaging_info = generate_packaging_info(case_code, case_height, packing_code)
                                ordernumber = partnumber.replace('#', packing_code)
                                if packaging_info:
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
                                        'orderNumbers': {ordernumber: packaging_info}
                                    }
                                    self.validate_part(part)
                                    self.create_or_update_part(part)
