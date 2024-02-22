from common.value_series import e24, e24_e96, e24_e192
from common.value_encoder import digits_multiplier_encoder
#from resistors.common import resistor_melf_header
from resistors.resistor_generator_base import ResistorGeneratorBase


class VishayMMU(ResistorGeneratorBase):
    def __init__(self):
        super().__init__(manufacturer='Vishay',
                         part_type="Resistor Thin Film",
                         series="MMU, MMA, MMB",
                         series_description="Professional Thin Film MELF Resistors",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='5°C ~ 35°C',
                         size_code={'MMU0102': '0102', 'MMA0204': '0204', 'MMB0207': '0207'},
                         package={'MMU0102': 'MELF 0102', 'MMA0204': 'MELF 0204', 'MMB0207': 'MELF 0207'},
                         packaging=['B3', 'B0', 'B2', 'B7', 'M3', 'M8'],
                         tolerance={'D': '±0.5%', 'F': '±1%', 'G': '±2%', 'J': '±5%'},
                         tcr={'D': '±25ppm/°C', 'C': '±50ppm/°C', 'B': '±100ppm/°C'},
                         power_rating_codes={'MMU0102': '0.3W', 'MMA0204': '0.4W', 'MMB0207': '1W'},
                        # header=resistor_melf_header + ['File Datasheet'],
                         product_url='https://www.vishay.com/product?docid=28713',
                         notes="Generated based on data from datasheet: Document Number: 28713, Revision: 11-Nov-2021")

        self.working_voltage = {'MMU0102': '150V', 'MMA0204': '200V', 'MMB0207': '350V'}
        self.max_overload_voltage = None
        self.dielectric_withstanding_voltage = {'MMU0102': '200V', 'MMA0204': '300V', 'MMB0207': '500V'}
        self.dimensions = {'MMU0102': {'Length': '2.2mm +0mm/-0.1mm', 'Diameter': '1.1mm +0mm/-0.1mm', 'K': '0.4mm +0.1mm/-0.05mm'},
                           'MMA0204': {'Length': '3.6mm +0mm/-0.2mm', 'Diameter': '1.4mm +0mm/-0.1mm', 'K': '0.75mm ±0.1mm'},
                           'MMB0207': {'Length': '5.8mm +0mm/-0.15mm', 'Diameter': '2.2mm +0mm/-0.2mm', 'K': '1.15mm ±0.1mm'}}

    def get_package_dimension(self, size_code, power_rating_code):
        return self.dimensions[size_code]

    def get_max_working_voltage(self, size_code, power_rating_code):
        return self.working_voltage[size_code]

    def get_dielectric_withstanding_voltage(self, size_code, power_rating_code):
        return self.dielectric_withstanding_voltage[size_code]

    def get_part_number(self, size_code, resistance, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        if size_code == power_rating_code:
            version = '0'
            value_str = digits_multiplier_encoder(resistance)
            assert len(value_str) == 4, str(value_str) + ', resistance ' + str(resistance)
            packing_type = '##'
            return f"{size_code}{version}{tcr_code}{value_str}{tolerance_code}{packing_type}00"

    def get_order_number(self, size_code, resistance, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        version = '0'
        value_str = digits_multiplier_encoder(resistance)
        assert len(value_str) == 4, str(value_str) + ', resistance ' + str(resistance)
        return f"{size_code}{version}{tcr_code}{value_str}{tolerance_code}{packing_type}00"

    def get_resistance_range(self, size, tolerance_code, tcr_code, taping_reel, special_feature):
        if size == 'MMU0102':
            if tcr_code == 'C':  # 50ppm
                if tolerance_code == 'J':  # 5%
                    return {'ranges': [[e24, '[0.22, 0.91]']]}
                elif tolerance_code == 'G':  # 2%
                    return {'ranges': [[e24, '[1, 9.1]']]}
                elif tolerance_code == 'F':  # 1%
                    return {'ranges': [[e24_e96, '[10, 2210000]']]}
                elif tolerance_code == 'D':  # 0.5%
                    return {'ranges': [[e24_e192, '[10, 221000]']]}
            elif tcr_code == 'D':  # 25ppm
                if tolerance_code == 'F':  # 1%
                    return {'ranges': [[e24_e96, '[10, 221000]']]}
                elif tolerance_code == 'D':  # 0.5%
                    return {'ranges': [[e24_e192, '[10, 221000]']]}
        elif size == 'MMA0204':
            if tcr_code == 'C':  # 50ppm
                if tolerance_code == 'J':  # 5%
                    return {'ranges': [[e24, '[0.22, 0.91]']]}
                elif tolerance_code == 'G':  # 2%
                    return {'ranges': [[e24, '[0.22, 0.91]']]}
                elif tolerance_code == 'F':  # 1%
                    return {'ranges': [[e24_e96, '[1, 10000000]']]}
                elif tolerance_code == 'D':  # 0.5%
                    return {'ranges': [[e24_e192, '[10, 2200000]']]}
            elif tcr_code == 'D':  # 25ppm
                if tolerance_code == 'F':  # 1%
                    return {'ranges': [[e24_e96, '[10, 511000]']]}
                elif tolerance_code == 'D':  # 0.5%
                    return {'ranges': [[e24_e192, '[10, 511000]']]}
        elif size == 'MMB0207':
            if tcr_code == 'B':  # 100ppm
                if tolerance_code == 'J':  # 5%
                    return {'ranges': [[e24, '[0.1, 0.20]']]}
                elif tolerance_code == 'G':  # 2%
                    return {'ranges': [[e24, '[0.1, 0.20]']]}
            elif tcr_code == 'C':  # 50ppm
                if tolerance_code == 'J':  # 5%
                    return {'ranges': [[e24, '[0.22, 0.91]']]}
                elif tolerance_code == 'G':  # 2%
                    return {'ranges': [[e24, '[0.22, 0.91]']]}
                elif tolerance_code == 'F':  # 1%
                    return {'ranges': [[e24, '[0.22, 0.91]']]}
            elif tcr_code == 'D':  # 25ppm
                if tolerance_code == 'F':  # 1%
                    return {'ranges': [[e24_e96, '[1, 15000000]']]}
                elif tolerance_code == 'D':  # 0.5%
                    return {'ranges': [[e24_e192, '[10, 1000000]']]}

    def packaging_data(self, size_code, power_rating_code, packaging_code):
        if size_code == 'MMU0102':
            if packaging_code == 'B3':
                packaging = {'Packaging Code': packaging_code, 'Packaging Type': 'Antistatic blister Tape / Reel',
                             'Packaging Qty': 3000,
                             'Reel Diameter': '180mm', 'Reel Width': ''}
                return packaging
            elif packaging_code == 'B0':
                packaging = {'Packaging Code': packaging_code, 'Packaging Type': 'Antistatic blister Tape / Reel',
                             'Packaging Qty': 10000,
                             'Reel Diameter': '330mm', 'Reel Width': ''}
                return packaging
            elif packaging_code == 'M8':
                packaging = {'Packaging Code': packaging_code, 'Packaging Type': 'Bulk',
                             'Packaging Qty': 8000}
                return packaging
        elif size_code == 'MMA0204':
            if packaging_code == 'B3':
                packaging = {'Packaging Code': packaging_code, 'Packaging Type': 'Antistatic blister Tape / Reel',
                             'Packaging Qty': 3000,
                             'Reel Diameter': '180mm', 'Reel Width': ''}
                return packaging
            elif packaging_code == 'B0':
                packaging = {'Packaging Code': packaging_code, 'Packaging Type': 'Antistatic blister Tape / Reel',
                             'Packaging Qty': 10000,
                             'Reel Diameter': '330mm', 'Reel Width': ''}
                return packaging
            elif packaging_code == 'M3':
                packaging = {'Packaging Code': packaging_code, 'Packaging Type': 'Bulk',
                             'Packaging Qty': 3000}
                return packaging
        elif size_code == 'MMB0207':
            if packaging_code == 'B2':
                packaging = {'Packaging Code': packaging_code, 'Packaging Type': 'Antistatic blister Tape / Reel',
                             'Packaging Qty': 2000,
                             'Reel Diameter': '180mm', 'Reel Width': ''}
                return packaging
            elif packaging_code == 'B7':
                packaging = {'Packaging Code': packaging_code, 'Packaging Type': 'Antistatic blister Tape / Reel',
                             'Packaging Qty': 7000,
                             'Reel Diameter': '330mm', 'Reel Width': ''}
                return packaging

    def get_files(self, partnumber, ordernumber):
        return {'File Datasheet': 'https://www.vishay.com/docs/28713/melfprof.pdf'}
