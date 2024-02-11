from capacitors.generate_yageo import generate_yageo_capacitors


def generate_capacitors(dest_dir, data_sources):
    generate_yageo_capacitors(dest_dir, data_sources + "/capacitors/")
