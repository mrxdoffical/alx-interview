#!/usr/bin/python3
"""
this module checks if data is utf8 valid or not
"""


def validUTF8(data):
    """
    this is tha validation function using shifting bits
    """
    num_cont = 0
    for byte in data:
        if byte < 0 or byte > 255:
            return False
        if num_cont == 0:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                num_cont = 1
            elif byte >> 4 == 0b1110:
                num_cont = 2
            elif byte >> 3 == 0b11110:
                num_cont = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_cont -= 1
    return num_cont == 0
