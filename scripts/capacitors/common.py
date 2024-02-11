import decimal


def str_capacitance_to_capacitance_in_pF(str_capacitance):
    if 'pF' in str_capacitance:
        return decimal.Decimal(str_capacitance.replace('pF', ''))
    if 'nF' in str_capacitance:
        return decimal.Decimal(str_capacitance.replace('nF', '')) * 1000
    if 'uF' in str_capacitance or 'μF' in str_capacitance:
        return decimal.Decimal(str_capacitance.replace('uF', '').replace('μF', '')) * 1000000
    raise ValueError("Invalid capacitance string format: ", str_capacitance)

