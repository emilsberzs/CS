# Cryptography in practice-encryption,PKI, digital signatures, hash functions.(part1)
## Introduction to cryptography
- Cryptography is is science of securing data using cryptography
- Protection of personal messages, bank details, passwords etc.
- Prevention of tampering and unauthorised access
- Key terms:
    - Encryption:
        - Changing plaintext data into cyphertext
    - Decryption:
        - Changing cyphertext into plaintext
    - Key:
        - Secret password/number used in both encryption and decryption
    - Cipher:
        - Method/Algorithm used to encrypt and decrypt data

## Key management
- Process of handling cryptographic keys throughout their lifecycle
- Includes key:
    - Generation
    - Distribution
    - Storage 
    - Rotation
    - Deletion
    - Expiration date setting
    - Access management
- Best practices:
    - Use secure key generators
    - Store in protected vaults or hardware
    - Never embedd in source code or configuration files
    - Rotate keys regularly
    - Limit access to keys using strict controls
    - Log all key related actions for auditing and incident response

## Symmetric cryptography
- Uses single shared key for both encryption and decryption
- Same key must be shared in a safe way between parties before communication starts
- ![alt text](image.png)
- ![alt text](image-2.png)
- Used in many places due to its **speed** and **efficiency**, for example:  
    - Database records
    - Files on devices
    - Mobile app communications
    - VPN's
    - Transaction data in financial systems




### Advanced Encryption Standart(AES)
- Symmetric encryption algorithm
- Encrypts data in blocks using multiple rounds of substitution and transformation based on the keylengths
- Scrambles data using shared secret key
- Supports different key-lengths:
    - 128 bit
    - 192 bit
    - 256 bit
- Fast, secure,and resistant to many attack methods

## Asymetric cryptography
- Slower than symmetric encryption
- Uses Public key(encryption)/Private key(decryption) pair
- ![alt text](image-1.png)

### Key terms
- Public key:
    - Ecrypt or verify
- Private key:
    - Decrypt or sign
- Key pair:
    - Two keys that work together
- Digital signatures:
    - Prove identity and message integrity using a private key

### How Asymetric encryption works
- Sender uses receivers public key to encrypt data
- Only receiver can decrypt data using his private key
- Used for privacy and secure messages
- Public key can be shared freely

### Use cases of asymetric encryption
- Secure websites and email
- Blockchain and crypto-currencies
- Software licensing
- VPN's

### Advantagees and limitations od asymetric encryption
- +Secure without shared keys
- +Supports authentication
- -Slower than symmetric methods
- -Need more processing power

### Common asymetric algorithms
- Rivest-Shamir-Adleman(RSA):
    - Widely used for encryption and signing
- Elliptic curve cryptography(ECC):
    - Secure with smaller key sizes
- Diffie Hellman:
    - Used to securely exhange keys

## Ceasar Cipher in python
- See ceasar.py
- Substitution cipher
- Each letter is shifted by a fixed number of places down the alphabet

## Cryptographic algorithms and hash functions
### Hash function
- Converts data into fixed length output
- Input and output are always the same length, regardless of the length of the input
- One way, irreversible process
- Even small change in input will create completely different output

### Key properties of hash functions
- Deterministic and fast:
    - Same input, always produces exactly the same output
- Irreversible:
    - Can't reverse engineer input from the output
- Avalanche effect:
    - Small input change causes large output change, totally different
- Collision resistant:
    - No two inputs can produce the same output

### Hash functions vs Encryption
- Hashing functions has no key and cannot be reversed
- Used for verification, not confidentiality
- Helps detect tampering and errors

### Use cases: 
- Password storage
    - Store only hashed version of passwords
    - User input is hashed and compared with stored hash
    - Prevents original passwords from being exposed
- Data integrity:
    - Hashes verify downloaded or received files
    - Mismatch indicated tampering or corruption
    - Used in software, backups and messages

### Common Hash algorithms
- MD5:
    - Fast but outdated
- SHA-1:
    - Outdated and weak
- SHA-2/SHA3:
    - Modern, trusted and in use


### **Check hashing.py file in this folder**

### Strengths and weaknesses of hash functions
- +Fast and simple
- -Weak hashes are vulnerable to attacks