from .valsin.valsin_capacitor_converter import WalsinCapacitorConverter


def generate_walsin_capacitors(dest_dir, data_sources):
    dest_dir = dest_dir + '/walsin'
    np0_generator = WalsinCapacitorConverter(data_sources + '/walsin/walsin_MLCC_NP0.csv', {'Dielectric Type': 'NP0'})
    np0_generator.generate(dest_dir + '/walsin/walsin_NP0_generated.json')

    x5r_generator = WalsinCapacitorConverter(data_sources + '/walsin/walsin_MLCC_X5R.csv', {'Dielectric Type': 'X5R'})
    x5r_generator.generate(dest_dir + '/walsin/walsin_X5R_generated.json')

    x7r_generator = WalsinCapacitorConverter(data_sources + '/walsin/walsin_MLCC_X7R.csv', {'Dielectric Type': 'X7R'})
    x7r_generator.generate(dest_dir + '/walsin/walsin_X7R_generated.json')
