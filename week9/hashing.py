import hashlib

data_to_hash = "This is the data that will be hashed"

# Create a SHA256 hash object
sha256_hash = hashlib.sha256()

# Update the hash object with the data.
# Data must be encoded to bytes.
sha256_hash.update(data_to_hash.encode('utf-8'))

# Get the hexadecimal representation of the hash
hashed_data = sha256_hash.hexdigest()

print(f"Original data: {data_to_hash}")
print(f"SHA156 hash: {hashed_data}")