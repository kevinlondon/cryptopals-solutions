import binascii
from itertools import izip


def fixed_xor(buffer_a, buffer_b):
    hex_a = int(buffer_a, 16)
    hex_b = int(buffer_b, 16)
    xored_value = str(hex(hex_a ^ hex_b))
    return xored_value[2:-1]


def test_it_hex_decodes_and_xors():
    buffer_a = '1c0111001f010100061a024b53535009181c'
    buffer_b = '686974207468652062756c6c277320657965'
    expected = '746865206b696420646f6e277420706c6179'
    assert fixed_xor(buffer_a, buffer_b) == expected
