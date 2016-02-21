import hmac
import json
import base64
import random
import hashlib
from Crypto.Cipher import AES
from phpserialize import loads, dumps


class Crypt:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
        base64_iv = base64.b64encode(iv)
        mode = AES.MODE_CBC
        encrypter = AES.new(self.key, mode, IV=iv)

        value = base64.b64encode(encrypter.encrypt(self._pad(dumps(text))))
        mac = self._hash(base64_iv, value)

        json_encoded = json.dumps({
            'iv': base64_iv,
            'value': value,
            'mac': mac
        })

        return base64.b64encode(json_encoded)

    def decrypt(self, payload):
        data = json.loads(base64.b64decode(payload))

        value = base64.b64decode(data['value'])
        iv = base64.b64decode(data['iv'])

        return loads(self._mcrypt_decrypt(value, iv))

    def _pad(self, data):
        """
        Pad value with bytes so it's a multiple of 16
        See: http://stackoverflow.com/questions/14179784/python-encrypting-with-pycrypto-aes
        :param data:
        :return data:
        """
        length = 16 - (len(data) % 16)
        data += chr(length)*length
        return data

    def _hash(self, iv, value):
        """
        Generate and hmac signature for this encrypted data
        :param key:
        :param iv:
        :param value:
        :return string:
        """
        return hmac.new(self.key, msg=iv+value, digestmod=hashlib.sha256).hexdigest()

    def _mcrypt_decrypt(self, value, iv):
        AES.key_size = 128

        crypt_object = AES.new(key=self.key, mode=AES.MODE_CBC, IV=iv)
        return crypt_object.decrypt(value)