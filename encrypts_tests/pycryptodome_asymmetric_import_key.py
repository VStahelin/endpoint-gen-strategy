from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("../keys/pk.pem", "rb") as private_key_file:
    private_key = RSA.import_key(private_key_file.read())

with open("../keys/pp.pem", "rb") as public_key_file:
    public_key = RSA.import_key(public_key_file.read())

original_message = b"Hello, world!"

encryptor = PKCS1_OAEP.new(public_key)
encrypted = encryptor.encrypt(original_message)

decryptor = PKCS1_OAEP.new(private_key)
decrypted_message = decryptor.decrypt(encrypted)

print(f'Original Message: {original_message.decode("utf-8")}')
print(f"Encrypted Message: {encrypted.hex()}")
print(f'Decrypted Message: {decrypted_message.decode("utf-8")}')
