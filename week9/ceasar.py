# Uses ASCII to transfrom characters, leaves spaces and punctuation intact
def encrypt(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 +base)
        else:
            result += char
    return result

# Same logic as encrypt, just negative shift
def decrypt(text,shift):
    return encrypt(text, -shift)
    
key = 5
string = "My name is Emils"
encrypted = encrypt(string, key)
print(encrypted)
decrypted = decrypt(encrypted,key)
print(decrypted)