from resistors.generate_panasonic_resistors import generate_panasonic_resistors


def generate_resistors(dest_dir, data_sources):
    generate_panasonic_resistors(dest_dir, data_sources + "/resistors/")
