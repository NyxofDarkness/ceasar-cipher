from ceasar_cipher.ceasar_cipher import encrypt, decrypt, crack
import pytest

text = "It was the best of times, it was the worst of times."
message = "Lw zdv wkh ehvw ri wlphv, lw zdv wkh zruvw ri wlphv."


# encrypt a string with a given shift
# encryption should handle upper and lower case letters
# encryption should allow non-alpha characters but ignore them, including white space
def test_encrypt():
    actual = encrypt(text, 3)
    expected = message
    assert actual == expected

# decrypt a previously encrypted string with the same shift
def test_decrypt():
    actual = decrypt(message, 3)
    expected = text
    assert actual == expected


# decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
def test_crack():
    actual = crack(message)
    expected = text
    assert actual == expected
