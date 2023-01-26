#!/usr/bin/python3
"""
UTF-8 Validation
"""
from typing import List


def validUTF8(data:  List[int]) -> bool:
    # Check if the data set is empty
    if not data:
        return False

    # Check if the data set contains only valid UTF-8 characters
    for c in data:
        if (c < 0x00 or c > 0x7F):
            return False

    # Check if the data set contains a valid UTF-8 sequence
    i = 0
    while i < len(data):
        # Get the first byte of the sequence
        c = data[i]

        # If it's a single byte character, move on to the next one
        if (c >> 7) == 0:
            i += 1

        # If it's a 2 byte character, check that the next byte is valid
        elif (c >> 5) == 6:
            if i+1 >= len(data) or (data[i+1] >> 6) != 2:
                return False

            i += 2

        # If it's a 3 byte character, check that the next two bytes are valid
        elif (c >> 4) == 14:
            if i+2 >= len(data) or (data[i+1] >> 6) != 2 or\
               (data[i+2] >> 6) != 2:
                return False

            i += 3

        # If it's a 4 byte character, check that the next three bytes are valid
        elif (c >> 3) == 30:
            if i+3 >= len(data) or (data[i+1] >> 6) != 2 or\
               (data[i+2] >> 6) != 2 or (data[i+3] >> 6) != 2:
                return False

            i += 4

        else:  # Invalid UTF-8 sequence found
            return False

    return True
