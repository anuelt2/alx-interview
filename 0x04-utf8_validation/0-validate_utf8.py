#!/usr/bin/python3
"""Module with `validUTF8` method"""


def validUTF8(data):
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding
    """
    number_of_bytes = 0

    for num in data:
        byte = num & 0xFF

        if number_of_bytes == 0:
            mask = 0x80
            while mask & byte:
                number_of_bytes += 1
                mask >>= 1

            if number_of_bytes == 0:
                continue

            if number_of_bytes == 1 or number_of_bytes > 4:
                return False

        else:
            if not (byte & 0x80 and not (byte & 0x40)):
                return False

        number_of_bytes -= 1

    return number_of_bytes == 0
