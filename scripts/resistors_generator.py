from resistors.generate_panasonic_resistors import generate_panasonic_resistors
from resistors.generate_royalohm_resistors import generate_royalohm_resistors


def generate_resistors(dest_dir, data_sources):
    generate_panasonic_resistors(dest_dir, data_sources + "/resistors/")
    generate_royalohm_resistors(dest_dir, data_sources + "/resistors/")

