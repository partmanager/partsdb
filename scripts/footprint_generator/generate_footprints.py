import json

from pathlib import Path
from part_library_gen import footprint_generator
from part_library_gen.exporters.svg.footprint_exporter import export


def generate_schematic_symbols(files):
    for file in files:
        with open(file, 'r') as f:
            data = json.load(f)
            for part in data:
                process_part_data(part)


def load_files(directory):
    files = Path(directory).rglob('*.json')
    return [x for x in files if not str(x).endswith('_generated.json')]


def process_part_data(part):
    if "symbol&footprint" in part:
        symbol_footprint = part["symbol&footprint"]
        if 'footprint_generator' in symbol_footprint:
            print("Processing", part['partNumber'])
            for generator in symbol_footprint['footprint_generator']:
                symbol_data = symbol_footprint['footprint_generator'][generator]
                symbol_data["generator"] = generator
                symbol_data["data"] = part["package"]["dimensions"]
                print(symbol_data)
                generated, filename = footprint_generator.generate(symbol_data)
                export(generated, 'generated/footprints/' + filename)


if __name__ == "__main__":
    generate_schematic_symbols(load_files("components"))
