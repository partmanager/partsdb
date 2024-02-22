from .viking.viking_AR_generator import VikingARGenerator
from .viking.viking_AR_A_generator import VikingAR_AGenerator
from .viking.viking_ARG_generator import VikingARGResistorGenerator
from .viking.viking_PWR_generator import VikingPWRResistorGenerator


def generate_viking_resistors(dest_dir, data_sources):
    dest_dir = dest_dir + "/viking/"

    ar_a = VikingAR_AGenerator()
    ar_a.generate_resistor(dest_dir + 'viking_ar_a_generated.json')
    ar = VikingARGenerator()
    ar.generate_resistor(dest_dir + 'viking_ar_generated.json')
    arg = VikingARGResistorGenerator()
    arg.generate_resistor(dest_dir + 'viking_arg_generated.json')
    pwr = VikingPWRResistorGenerator()
    pwr.generate_resistor(dest_dir + 'viking_pwr_generated.json')
