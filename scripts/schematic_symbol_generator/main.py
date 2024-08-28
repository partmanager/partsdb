import json

from pathlib import Path
from part_library_gen import symbol_generator


def load_files(directory):
    files = Path(directory).rglob('*.json')
    return [x for x in files if not str(x).endswith('_generated.json')]


def process_part_data(part):
    if "symbol&footprint" in part:
        symbol_footprint = part["symbol&footprint"]
        if 'pinmap' in symbol_footprint and len(symbol_footprint['pinmap']) > 0:
            print("Processing", part['partNumber'])
            symbol_data = {
                'designator': "U?",
                'manufacturer': part['manufacturer'],
                'part': part['partNumber'],
                'pins': symbol_footprint['pinmap'],
                'symbol_generator': {'default': {}}
            }
            if 'symbol_generator' in symbol_footprint:
                print("Using dedicated generator")
                for generator in symbol_footprint['symbol_generator']:
                    symbol_data['symbol_generator'] = {generator: symbol_footprint['symbol_generator'][generator]}
                    generated, filename = symbol_generator.generate(symbol_data)[0]
                    symbol_generator.export_symbol(generated, 'symbols/' + filename)
            else:
                symbol_generator.generate(symbol_data)


def generate_schematic_symbols(files):
    for file in files:
        with open(file, 'r') as f:
            data = json.load(f)
            for part in data:
                process_part_data(part)


if __name__ == "__main__":
    generate_schematic_symbols(load_files("components"))
