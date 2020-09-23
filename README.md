# pypass 

pypass is library to parse password entries from [Password Store (pass)](https://www.passwordstore.org/) password manager, stored in [recommended format](https://www.passwordstore.org/#organization).

## Example

Suppose your password entry is named `Email/donenfeld.com` at contains following fields:
```
Yw|ZSNH!}z"6{ym9pI
Username: AmazonianChicken@example.com
PIN: 84719
```

You can read it using this library with following code:

```python
from passpy import PasswordStoreEntry

entry = PasswordStoreEntry('Email/donenfeld.com')
print(entry['password']) # Yw|ZSNH!}z"6{ym9pI
print(entry['Username']) # AmazonianChicken@example.com
print(entry['PIN']) # 84719
```

Additionally if `pass-otp` is available and desired entry has OTP key URI defined, OTP code can be obtained using

```python
print(entry.get_otp_code())
```
