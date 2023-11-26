from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64


def generate_aes_key():
    return get_random_bytes(32)


def encrypt_aes(text, key):
    aes_cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = aes_cipher.encrypt_and_digest(text.encode("utf-8"))
    nonce = aes_cipher.nonce
    return base64.urlsafe_b64encode(nonce + tag + ciphertext).decode("utf-8")


def decrypt_aes(ciphertext, key):
    data = base64.urlsafe_b64decode(ciphertext)
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]
    aes_cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    _decrypted_text = aes_cipher.decrypt_and_verify(ciphertext, tag)
    return _decrypted_text.decode("utf-8")


def encrypt_rsa(text, rsa_key):
    public_key = RSA.import_key(rsa_key)
    symmetric_key = generate_aes_key()
    rsa_cipher = PKCS1_OAEP.new(public_key)
    _encrypted_symmetric_key = rsa_cipher.encrypt(symmetric_key)
    _encrypted_text = encrypt_aes(text, symmetric_key)
    return (
        base64.urlsafe_b64encode(_encrypted_symmetric_key).decode("utf-8"),
        _encrypted_text,
    )


def decrypt_rsa(encrypted_symmetric_key, encrypted_text, rsa_key):
    private_key = RSA.import_key(rsa_key)
    rsa_cipher = PKCS1_OAEP.new(private_key)
    symmetric_key = rsa_cipher.decrypt(
        base64.urlsafe_b64decode(encrypted_symmetric_key)
    )
    _decrypted_text = decrypt_aes(encrypted_text, symmetric_key)
    return _decrypted_text


with open("../keys/pk.pem", "rb") as private_key_file:
    rsa_key = private_key_file.read()

original_text = "v1/pay/notify/42475895-e5c3-4a4b-9ae8-4898bffb3e61"

encrypted_symmetric_key, encrypted_text = encrypt_rsa(original_text, rsa_key)
decrypted_text = decrypt_rsa(encrypted_symmetric_key, encrypted_text, rsa_key)

final_url = f"https://vitor.com.br/api/{encrypted_text}"

print(f"Original Text: {original_text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Hash Length: {len(encrypted_text)}")
print(f"Decrypted Text: {decrypted_text}")
print(f"Final URL: {final_url}")
print(f"Final URL Length: {len(final_url)}")
