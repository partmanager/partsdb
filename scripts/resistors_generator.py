from resistors.generate_panasonic_resistors import generate_panasonic_resistors
from resistors.generate_royalohm_resistors import generate_royalohm_resistors
from resistors.generate_tt_electronics_resistors import generate_tt_resistors
from resistors.generate_viking_resistors import generate_viking_resistors
from resistors.generate_vishay_resistors import generate_vishay_resistors
from resistors.generate_walsin_resistor import generate_walsin_resistors
from resistors.generate_yageo_resistors import generate_yageo_resistors


def generate_resistors(dest_dir, data_sources):
    generate_panasonic_resistors(dest_dir, data_sources + "/resistors/")
    generate_royalohm_resistors(dest_dir, data_sources + "/resistors/")
    generate_tt_resistors(dest_dir, data_sources + "/resistors/")
    generate_viking_resistors(dest_dir, data_sources + "/resistors/")
    generate_vishay_resistors(dest_dir, data_sources + "/resistors/")
    generate_walsin_resistors(dest_dir, data_sources + "/resistors/")
    generate_yageo_resistors(dest_dir, data_sources + "/resistors/")
