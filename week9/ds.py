# pip install pycryptodome
# Had to change environment to 3.12.9 miniconda for imports to work
import hashlib
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256

# Generate RSA key pair
key = RSA.generate(2048)

# Define the message
message = b"Secure message"

# Hash the message
h = SHA256.new(message)

# Sign the hash
signature = pkcs1_15.new(key).sign(h)

# Verification
try:
    pkcs1_15.new(key.public_key()).verify(h,signature)
    print("Signature is valid")
except (ValueError,TypeError):
    print("Invalid signature")