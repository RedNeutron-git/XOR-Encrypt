#/bin/python27

# RedNeutron

# Encryptor
def xor_encrypt_decrypt(data, key):
    result = ""
    for i in range(len(data)):
        result += chr(ord(data[i]) ^ ord(key[i % len(key)]))
    return result

def display_encrypted_text(input_file, key):
    with open(input_file, 'r') as file:
        plaintext = file.read()
    encrypted_text = xor_encrypt_decrypt(plaintext, key)
    print("{ 0x" + ', 0x'.join(hex(ord(x))[2:] for x in encrypted_text) + "}")

# Input file
input_filename = 'file-input.ic'
encryption_key = 'secretkey'

# Show encrypted file
display_encrypted_text(input_filename, encryption_key)
