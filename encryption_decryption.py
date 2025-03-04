def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift * mode) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    return result

plaintext = input("Enter your plaintext:")
shift = 5
encrypted = caesar_cipher(plaintext, shift, 1)
decrypted = caesar_cipher(encrypted, shift, -1)

print(f"Original Text: {plaintext}")
print(f"Encrypted Text: {encrypted}")

dec = input ("Do you want to decrypt it as well (Y/N)?:")
if dec == "Y" or "y":
    print(f"Decrypted Text: {decrypted}")
else:
    print("Bye")

