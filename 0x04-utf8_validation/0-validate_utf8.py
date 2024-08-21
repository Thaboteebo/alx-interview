#!/usr/bin/env python3
""" module doc """


def validUTF8(data):
    i = 0
    while i < len(data):
        byte = data[i]
        if byte < 0x80:
            i += 1
        elif byte < 0xC0:
            return False
        elif byte < 0xE0:
            if i + 1 >= len(data) or data[i + 1] < 0x80 or data[i + 1] >= 0xC0:
                return False
            i += 2
        elif byte < 0xF0:
            if i + 2 >= len(data) or data[i + 1] < 0x80 or data[i + 1] >= 0xC0:
                return False
            i += 3
        else:
            if i + 3 >= len(data) or data[i + 1] < 0x80 or data[i + 1] >= 0xC0:
                return False
            i += 4
    return True
