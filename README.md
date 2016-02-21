# Laracrypt

Laravel-compatible, two-way encryption


## Usage

```python
from laracrypt import Crypt

# Pass it a string of 32 bits, 
# 99.9% of the time, this means a string
# that is 32 characters in length
crypt = Crypt('this string has 32 characters!!!')

string_to_encrypt = 'Please encrypt this string'

encrypted_string = crypt.encrypt(string_to_encrypt)

# later...
unencrypted_string = crypt.decrypt(encrypted_string)

assert encrypted_string == unencrypted_string
```
