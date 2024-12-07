from .panasonic.panasonic_ERA_generator import PanasonicERAResistorGenerator
from .panasonic.panasonic_ERJ_generator import PanasonicERJ_05_ResistorGenerator, PanasonicERJ_1_ResistorGenerator, PanasonicERJ_5_ResistorGenerator
from .panasonic.panasonic_ERJH_generator import PanasonicERJHResistorGenerator
from .panasonic.panasonic_ERJP_generator import PanasonicERJPResistorGenerator


def generate_panasonic_resistors(dest_dir, data_sources):
    dest_dir = dest_dir.joinpath("panasonic")

    era = PanasonicERAResistorGenerator()
    era.generate_resistor(dest_dir.joinpath('panasonic_era_generated.json'))

    erj = PanasonicERJ_05_ResistorGenerator()
    erj.generate_resistor(dest_dir.joinpath('panasonic_erj_05_generated.json'))
    erj = PanasonicERJ_1_ResistorGenerator()
    erj.generate_resistor(dest_dir.joinpath('panasonic_erj_1_generated.json'))
    erj = PanasonicERJ_5_ResistorGenerator()
    erj.generate_resistor(dest_dir.joinpath('panasonic_erj_5_generated.json'))

    erjh = PanasonicERJHResistorGenerator()
    erjh.generate_resistor(dest_dir.joinpath('panasonic_erjh_generated.json'))

    erjp = PanasonicERJPResistorGenerator()
    erjp.generate_resistor(dest_dir.joinpath('panasonic_erjp_generated.json'))