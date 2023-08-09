# This simple Python script can be used to decode SQL authentication

# Test encrypted = A2A5B3A592A592A5D2A553A582A5E3A5
# Test decrypted = password


def decrypt(encrypted):
    encrypted_bytes = bytes.fromhex(encrypted)
    decrypted_bytes = bytearray()

    for current_byte in range(len(encrypted_bytes)):
        # XOR byte with A5
        decrypted_byte = encrypted_bytes[current_byte] ^ 0xA5
        upper_nibble = decrypted_byte & 0xF0
        lower_nibble = decrypted_byte & 0x0F
        # Swap nibbles
        upper_nibble >>= 4
        lower_nibble <<= 4
        final_byte = lower_nibble ^ upper_nibble
        decrypted_bytes.append(final_byte)

    print("Decrypted password: " + decrypted_bytes.decode('utf-16'))


if __name__ == '__main__':
    encrypted = input("Enter encrypted password: ")
    decrypt(encrypted)
