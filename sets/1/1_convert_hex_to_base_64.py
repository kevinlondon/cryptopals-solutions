import binascii
import base64


def hex_to_base64(source):
    base10 = binascii.unhexlify(source)
    return base64.b64encode(base10)


def test_it_passes_the_example():
    source = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    assert hex_to_base64(source) == expected
