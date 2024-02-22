from math import log10, floor
from decimal import Decimal


def digits_multiplier_encoder(value, digits=3, multiplier_str=None):
    """
    Encode value in form of XXXM where X are digits and M is multiplier
    :param value:
    :param digits: number of digits
    :param multiplier_str:
    :return:
    """
    if multiplier_str is None:
        multiplier_str = {-3: '7', -2: '8', -1: '9', 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
    numbers = floor(log10(value))
    multiplier = numbers - digits + 1
    #print("Multiplier", multiplier, multiplier_str[multiplier], 'Value', value, "numbers", log10(value))
    value_str = "{:.2f}".format(value * Decimal(f'1e{multiplier * -1}'))
    value_str = value_str.rstrip('0').rstrip('.') + multiplier_str[multiplier]
    assert '.' not in value_str, value
    return value_str