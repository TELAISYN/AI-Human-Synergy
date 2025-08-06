import hashlib
from Crypto.Hash import RIPEMD

FILENAME = "Ordinal_05.pdf"

with open(FILENAME, "rb") as f:
    data = f.read()

sha256 = hashlib.sha256(data).digest()
sha256_hex = hashlib.sha256(data).hexdigest()
ripemd = RIPEMD.new()
ripemd.update(sha256)
ripemd_hex = ripemd.hexdigest()

print("SHA256     :", sha256_hex)
print("RIPEMD160  :", ripemd_hex)