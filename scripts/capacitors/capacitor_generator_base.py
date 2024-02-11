from common.part_generator_base import PartGeneratorBase


class CapacitorGeneratorBase(PartGeneratorBase):
    def __init__(self, manufacturer):
        super().__init__(manufacturer)

    def generate_parts(self):
        return self.generate_capacitor()

    def validate_part(self, part):
        super(CapacitorGeneratorBase, self).validate_part(part)
        assert part['partType'] in ['Aluminium Electrolytic Capacitor', 'MLCC'], part['partType']