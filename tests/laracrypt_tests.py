from nose.tools import *
from laracrypt import Crypt

class TestEncryption(object):

    def __init__(self):
        self.key = 'abcdefghijklmnopqrtuvwxyz1234567'

    def test_encrypt_string(self):
        encrypter = Crypt(self.key)

        string = 'please encrypt this string'
        encrypted_string = encrypter.encrypt(string)
        unencrypted_string = encrypter.decrypt(encrypted_string)

        assert string == unencrypted_string

    def test_laravel_string_decrypted(self):
        encrypter = Crypt(self.key)

        string_encrypted_in_laravel_52 = 'this is encrypted in laravel'
        encrypted_string_from_laravel = "eyJpdiI6IlprVkJHYWFQQ2doMEo0VUVCcFJ3M2c9PSIsInZhbHVlIjoiQXpCVittbEVpcjdEd1NpN0lFV2tHSDdacllBZllZNG1adGFcLzZkdHZmUEk3Nk5NaWNFanNlbndZM3pNeFNrMVciLCJtYWMiOiI3NmRjYzZkZTY5OWQ3OWM0OTdhMmI3MThlZDA2MjZkOGQxYmY0MDAzOTBmNmFhNDZmMjNhY2RjN2QyMjRjYzczIn0="

        unencrypted_string = encrypter.decrypt(encrypted_string_from_laravel)

        assert string_encrypted_in_laravel_52 == unencrypted_string
