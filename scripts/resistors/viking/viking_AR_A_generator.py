from common.value_series import e24
from resistors.resistor_generator_base import ResistorGeneratorBase
from resistors.common import resistance_to_str_v2


class VikingAR_AGenerator(ResistorGeneratorBase):
    def __init__(self):
        super().__init__("Viking",
                         "Resistor Thin Film",
                         "AR..A",
                         "Automotive Grade Thin Film Precision Chip Resistor",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='-55°C ~ 125°C',
                         size_code={'AR02': '0402', 'AR03': '0603', 'AR05': '0805', 'AR06': '1206', 'AR13': '1210',
                                    'AR10': '2010', 'AR12': '2512'},
                         package={'AR02': 'Chip 0402', 'AR03': 'Chip 0603', 'AR05': 'Chip 0805', 'AR06': 'Chip 1206',
                                  'AR13': 'Chip 1210', 'AR10': 'Chip 2010', 'AR12': 'Chip 2512'},
                         tolerance={'A': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%', 'F': '±1%'},
                         tcr={'B': '±10ppm/°C', 'N': '±15ppm/°C', 'C': '±25ppm/°C', 'D': '±50ppm/°C'},
                         packaging=['T', 'B'],
                         power_rating_codes={'X': '0.1W',  #'1/10W',
                                             'W': '0.125W',  #'1/8W',
                                             'V': '0.25W',  #'1/4W',
                                             'O': '0.33333333W',  #'1/3W',
                                             '1/16': '0.0625W',  #'1/16W',
                                             '1/10': '0.1W',  #'1/10W',
                                             '1/8': '0.125W',  #'1/8W',
                                             '1/4': '0.25W',  #'1/4W',
                                             '1/2W': '0.5W'  #'1/2W'
                                             },
                         product_url='https://www.viking.com.tw/en/category/Thin-Film-Precision-Resistor-AR..A-Series/Resistor-AR-A.html',
                         notes='')
        self.dimensions = {'0402': {'Length': '1.00mm ±0.05', 'Width': '0.50mm ±0.05', 'Height': '0.30mm±0.05',
                                    't1': '0.20mm±0.10', 't2': '0.20±0.10mm'},
                           '0603': {'Length': '1.55mm ±0.10', 'Width': '0.80mm ±0.10', 'Height': '0.45mm±0.10',
                                    't1': '0.3mm±0.20', 't2': '0.3mm±0.20'},
                           '0805': {'Length': '2.00mm ±0.15', 'Width': '1.25mm ±0.15', 'Height': '0.55mm±0.10',
                                    't1': '0.3mm±0.20', 't2': '0.4mm±0.20'},
                           '1206': {'Length': '3.05mm ±0.15', 'Width': '1.55mm ±0.15', 'Height': '0.55mm±0.10',
                                    't1': '0.42mm±0.20', 't2': '0.35mm±0.25'},
                           '1210': {'Length': '3.10mm ±0.10', 'Width': '2.40mm ±0.15mm', 'Height': '0.55mm±0.10',
                                    't1': '0.4mm±0.20', 't2': '0.55mm±0.25'},
                           '2010': {'Length': '4.90mm ±0.15', 'Width': '2.40mm ±0.15', 'Height': '0.55mm±0.10',
                                    't1': '0.6mm±0.30', 't2': '0.5mm±0.25'},
                           '2512': {'Length': '6.30mm ±0.15', 'Width': '3.10mm ±0.15', 'Height': '0.55mm±0.10',
                                    't1': '0.6mm±0.30', 't2': '0.5mm±0.25'}}
        self.max_operating_voltage_standard = {'AR02': '25V', 'AR03': '50V', 'AR05': '100V', 'AR06': '150V',
                                               'AR13': '150V', 'AR10': '150V', 'AR12': '150V'}
        self.max_overload_voltage_standard = {'AR02': '50V', 'AR03': '100V', 'AR05': '200V', 'AR06': '300V',
                                              'AR13': '300V', 'AR10': '300V', 'AR12': '300V'}
        self.max_operating_voltage_high_power = {'AR03': '75V', 'AR05': '150V', 'AR06': '200V', 'AR13': '200V',
                                                 'AR10': '200V'}
        self.max_overload_voltage_high_power = {'AR03': '150V', 'AR05': '300V', 'AR06': '400V', 'AR13': '400V',
                                                'AR10': '400V'}
        self.high_power_rating_code = ['X', 'W', 'V', 'O']
        self.packing_type_and_qty = {'AR02': {'Packaging Type': 'Paper Tape / Reel', 'Reel Diameter': '178mm ±1mm', 'Reel Width': '11.5mm ±1mm', 'Packaging Qty': 10000},
                                     'AR03': {'Packaging Type': 'Paper Tape / Reel', 'Reel Diameter': '178mm ±1mm', 'Reel Width': '11.5mm ±1mm', 'Packaging Qty': 5000},
                                     'AR05': {'Packaging Type': 'Paper Tape / Reel', 'Reel Diameter': '178mm ±1mm', 'Reel Width': '11.5mm ±1mm', 'Packaging Qty': 5000},
                                     'AR06': {'Packaging Type': 'Paper Tape / Reel', 'Reel Diameter': '178mm ±1mm', 'Reel Width': '11.5mm ±1mm', 'Packaging Qty': 5000},
                                     'AR13': {'Packaging Type': 'Paper Tape / Reel', 'Reel Diameter': '178mm ±1mm', 'Reel Width': '11.5mm ±1mm', 'Packaging Qty': 5000},
                                     'AR10': {'Packaging Type': 'Embossed Tape / Reel', 'Reel Diameter': '178mm ±1mm', 'Reel Width': '15.5mm ±1mm', 'Packaging Qty': 4000},
                                     'AR12': {'Packaging Type': 'Embossed Tape / Reel', 'Reel Diameter': '178mm ±1mm', 'Reel Width': '15.5mm ±1mm', 'Packaging Qty': 4000}}
        self.packaging_tape_size = {
            'AR02': {'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm±0.1mm', 'Tape E': '1.75mm±0.05mm',
                     'Tape F': '3.50mm±0.05mm', 'Tape P0': '4mm±0.10mm', 'Tape P1': '2mm±0.05mm',
                     'Tape P2': '2mm±0.05mm', 'Tape D': '1.55mm±0.05mm', 'Tape A0': '0.7mm±0.05mm',
                     'Tape A1': '', 'Tape B0': '1.16mm±0.05mm', 'Tape B1': '', 'Tape T': '0.4mm±0.03mm'},
            'AR03': {'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm±0.1mm', 'Tape E': '1.75mm±0.05mm',
                     'Tape F': '3.50mm±0.05mm', 'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.1mm',
                     'Tape P2': '2mm±0.05mm', 'Tape D': '1.55mm±0.05mm', 'Tape A0': '1.1mm±0.05mm',
                     'Tape A1': '', 'Tape B0': '1.90mm±0.05mm', 'Tape B1': '', 'Tape T': '0.6mm±0.03mm'},
            'AR05': {'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm±0.1mm', 'Tape E': '1.75mm±0.05mm',
                     'Tape F': '3.50mm±0.05mm', 'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.1mm',
                     'Tape P2': '2mm±0.05mm', 'Tape D': '1.55mm±0.05mm', 'Tape A0': '1.6mm±0.05mm',
                     'Tape A1': '', 'Tape B0': '2.39mm±0.05mm', 'Tape B1': '', 'Tape T': '0.75mm±0.05mm'},
            'AR06': {'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm±0.1mm', 'Tape E': '1.75mm±0.05mm',
                     'Tape F': '3.50mm±0.05mm', 'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.1mm',
                     'Tape P2': '2mm±0.05mm', 'Tape D': '1.55mm±0.05mm', 'Tape A0': '2.0mm±0.05mm',
                     'Tape A1': '', 'Tape B0': '3.55mm±0.05mm', 'Tape B1': '', 'Tape T': '0.75mm±0.05mm'},
            'AR13': {'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm±0.1mm', 'Tape E': '1.75mm±0.05mm',
                     'Tape F': '3.50mm±0.05mm', 'Tape P0': '4mm±0.05mm', 'Tape P1': '4mm±0.1mm',
                     'Tape P2': '2mm±0.05mm', 'Tape D': '1.60mm±0.10mm', 'Tape A0': '2.75mm±0.05mm',
                     'Tape A1': '', 'Tape B0': '3.40mm±0.05mm', 'Tape B1': '', 'Tape T': '0.75mm±0.05mm'},
            'AR10': {'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '12mm±0.1mm', 'Tape E': '1.75mm±0.10mm',
                     'Tape F': '4.50mm±0.05mm', 'Tape P0': '4mm±0.05mm', 'Tape P1': '4mm±0.1mm',
                     'Tape P2': '2mm±0.05mm', 'Tape D': '1.50mm±0.10mm', 'Tape A0': '2.85mm±0.10mm',
                     'Tape A1': '', 'Tape B0': '5.45mm±0.10mm', 'Tape B1': '', 'Tape K': '1.0mm±0.2mm'},
            'AR12': {'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '12mm±0.1mm', 'Tape E': '1.75mm±0.10mm',
                     'Tape F': '4.50mm±0.05mm', 'Tape P0': '4mm±0.05mm', 'Tape P1': '4mm±0.1mm',
                     'Tape P2': '2mm±0.05mm', 'Tape D': '1.50mm±0.10mm', 'Tape A0': '3.4mm±0.10mm',
                     'Tape A1': '', 'Tape B0': '6.65mm±0.10mm', 'Tape B1': '', 'Tape K': '1.0mm±0.2mm'}
        }

    def get_max_working_voltage(self, size_code, power_rating_code):
        if power_rating_code in self.high_power_rating_code:
            return self.max_operating_voltage_high_power[size_code]
        else:
            return self.max_operating_voltage_standard[size_code]

    def get_max_overload_voltage(self, size_code, power_rating_code):
        if power_rating_code in self.high_power_rating_code:
            return self.max_overload_voltage_high_power[size_code]
        else:
            return self.max_overload_voltage_standard[size_code]

    def get_dielectric_withstanding_voltage(self, size_code, power_rating_code):
        return ''

    def get_package_dimension(self, size_code, power_rating_code):
        size = self.size_code[size_code]
        return self.dimensions[size]

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        resistance_str = resistance_to_str_v2(value)
        resistance_str = '0' * (4 - len(resistance_str)) + resistance_str
        assert len(resistance_str) == 4, resistance_str
        if power_rating_code not in self.high_power_rating_code:
            power_rating_code = ''
        partnumber = f"{size_code}{tolerance_code}#{tcr_code}{power_rating_code}{resistance_str}A"
        assert len(partnumber) in [12, 13], partnumber
        return partnumber

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        resistance_str = resistance_to_str_v2(value)
        resistance_str = '0' * (4 - len(resistance_str)) + resistance_str
        assert len(resistance_str) == 4, resistance_str
        if power_rating_code not in self.high_power_rating_code:
            power_rating_code = ''
        ordernumber = f"{size_code}{tolerance_code}{packing_type}{tcr_code}{power_rating_code}{resistance_str}A"
        assert len(ordernumber) in [12, 13], ordernumber
        return ordernumber

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if power_rating_code in self.high_power_rating_code:
            return self.get_resistance_range_for_high_power(size_code, tolerance_code, tcr_code, power_rating_code)
        else:
            return self.get_standard_resistance_range(size_code, tolerance_code, tcr_code, power_rating_code)

    def get_standard_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code):
        assert tolerance_code in ['A', 'B', 'C', 'D', 'F']
        assert tcr_code in ['B', 'N', 'C', 'D']

        if size_code == 'AR02' and power_rating_code == '1/16':
            if tolerance_code == 'A':
                return {'ranges': [[e24, "[49.9, 10000]"]]}
            else:
                if tcr_code == 'B':
                    return {'ranges': [[e24, "[49.9, 10000]"]]}
                elif tcr_code == 'N':
                    return {'ranges': [[e24, "[49.9, 69800]"]]}
                elif tcr_code in ['C', 'D']:
                    return {'ranges': [[e24, "[49.9, 100000]"]]}
        if size_code == 'AR03' and power_rating_code == '1/16':
            if tolerance_code == 'A':
                return {'ranges': [[e24, "[10, 49900]"]]}
            else:
                return {'ranges': [[e24, "[10, 332000]"]]}
        if size_code == 'AR05' and power_rating_code == '1/10':
            if tolerance_code == 'A':
                return {'ranges': [[e24, "[10, 100000]"]]}
            else:
                if tcr_code == 'B':
                    return {'ranges': [[e24, "[10, 511000]"]]}
                else:
                    return {'ranges': [[e24, "[10, 1000000]"]]}
        if size_code == 'AR06' and power_rating_code == '1/8':
            if tolerance_code == 'A':
                return {'ranges': [[e24, "[10, 200000]"]]}
            else:
                return {'ranges': [[e24, "[10, 1000000]"]]}
        elif size_code in ['AR13', 'AR10'] and power_rating_code == '1/4':
            if tolerance_code == 'A':
                return {'ranges': [[e24, "[10, 499000]"]]}
            else:
                return {'ranges': [[e24, "[10, 1000000]"]]}
        elif size_code == 'AR12' and power_rating_code == '1/2':
            if tolerance_code == 'A':
                return {'ranges': [[e24, "[10, 499000]"]]}
            else:
                return {'ranges': [[e24, "[10, 1000000]"]]}

    def get_resistance_range_for_high_power(self, size_code, tolerance_code, tcr_code, power_rating_code):
        assert tolerance_code in ['A', 'B', 'C', 'D', 'F']
        assert tcr_code in ['B', 'N', 'C', 'D']

        if size_code == 'AR03' and power_rating_code == 'X':
            if tolerance_code == 'A':
                return {'ranges': [[e24, "[10, 49900]"]]}
            else:
                return {'ranges': [[e24, "[10, 332000]"]]}
        if size_code == 'AR05' and power_rating_code == 'W':
            if tolerance_code == 'A':
                return {'ranges': [[e24, "[10, 100000]"]]}
            else:
                if tcr_code == 'B':
                    return {'ranges': [[e24, "[10, 511000]"]]}
                else:
                    return {'ranges': [[e24, "[10, 1000000]"]]}
        if size_code == 'AR06' and power_rating_code == 'V':
            if tolerance_code == 'A':
                return {'ranges': [[e24, "[10, 200000]"]]}
            else:
                return {'ranges': [[e24, "[10, 1000000]"]]}
        if size_code in ['AR13', 'AR10'] and power_rating_code == 'O':
            if tolerance_code == 'A':
                return {'ranges': [[e24, "[10, 499000]"]]}
            else:
                return {'ranges': [[e24, "[10, 1000000]"]]}

    def packaging_data(self, size_code, power_rating_code, packing_type_code):
        if size_code in ['AR02', 'AR03', 'AR05', 'AR06', 'AR13', 'AR10', 'AR12'] and packing_type_code == 'T':
            packaging = self.packing_type_and_qty[size_code]
            packaging.update(self.packaging_tape_size[size_code])
            return packaging

    def get_files(self, partnumber, ordernumber):
        return {'File Datasheet': 'https://www.viking.com.tw/Templates/att/AR..A_Series.pdf?lng=en'}

    def pre_save_validate(self):
        assert 'AR03A#C1001A' in self.parts
        part = self.parts['AR03A#C1001A']
        assert part['manufacturer'] == 'Viking'
        assert part['partNumber'] == 'AR03A#C1001A'
        assert part['partType'] == 'Resistor Thin Film'
        assert part['series']['name'] == 'AR..A'
        assert part['series']['description'] == 'Automotive Grade Thin Film Precision Chip Resistor'
        parameters = part['parameters']
        assert parameters['Resistance']['value'] == "1000.0R \u00b10.05%"
        assert parameters['TCR']['value'] == "\u00b125ppm/\u00b0C"
        assert parameters['Rated Power']['value'] == "max. 0.0625W"
        assert parameters['Working Voltage']['value'] == 'max. 50V'
        assert parameters['Overload Voltage']['value'] == 'max. 100V'
        assert part['package']['type'] == 'Chip 0603'
        assert part['symbol&footprint']['symbolName'] == 'resistor'

        assert 'AR03ATC1001A' in part['orderNumbers']
        return True
