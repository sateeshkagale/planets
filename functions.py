def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15
print('freezing point of water:',fahr_to_kelvin(32))
print('boiling point of water:',fahr_to_kelvin(212))
