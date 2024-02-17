from .aishi.aishi_converter import AishiCapacitorConverter


def generate_aishi_capacitors(dest_dir, data_sources):
    dest_dir = dest_dir + "/aishi/"
    aishi_converter = AishiCapacitorConverter(data_sources + '/aishi/aishi_wh.csv',)
    aishi_converter.generate(dest_dir + '/aishi_wh_generated.json')
