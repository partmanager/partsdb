import json
from pathlib import Path


def load_part_types():
    return ['Aluminium Electrolytic Capacitor',
            'Balun',
            'Battery',
            'Battery Holder',
            'Bridge Rectifier',
            'Cap',
            'Common Mode Choke',
            'Connector',
            'Connector Bus',
            'Connector Accessory',
            'Connector IDC',
            'Connector Terminal Block',
            'Connector microSD Card',
            'Connector Pins',
            'Crystal',
            'Crystal Oscillator',
            'Enclosure',
            'Enclosure Accessory',
            'ESD Suppressor',
            'Fuse',
            'Ind', 'Inductor', 'IC', 'IC LDO', 'IC MCU',
            'IC Voltage Reference', 'IC Voltage Regulator', 'IC Voltage Regulator Switching', 'IC DC-DC', 'IC Opamp', 'IC RF Amplifier', 'IC RF Synthesizer',
            'LED',
            'LCD Display',
            'Lightpipe',
            'MLCC',
            'Module',
            'PTC Fuse',
            'Res',
            'Resistor Thick Film',
            'Resistor Array',
            'Relay',
            'Small Signal Diode',
            'Surge arrester',
            'Switch',
            'Schottky Diode',
            'Transistor MOSFET P',
            'Transistor MOSFET N',
            'TVS',
            'Varistor',
            'Zener Diode']


def load_manufacturers():
    with open('./manufacturers/manufacturers.json') as f:
        manufacturers = json.load(f)
        return [x['name'] for x in manufacturers] + [x['full_name'] for x in manufacturers if x['full_name'] is not None and len(x['full_name']) > 0]


def load_files(directory):
    files = Path(directory).rglob('*.json')
    return [x for x in files if not str(x).endswith('_generated.json')]