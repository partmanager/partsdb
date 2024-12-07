from .walsin.walsin_WF_generator import WalsinWFResistorGenerator


def generate_walsin_resistors(dest_dir, data_sources):
    dest_dir = dest_dir.joinpath("walsin")

    wf = WalsinWFResistorGenerator()
    wf.generate_resistor(dest_dir.joinpath('walsin_wf_generated.json'))
