from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode


def encrypt(text, key):
    key = key.ljust(32, b"\0")[:32]
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    _encrypted_text = cipher.encrypt(pad(text.encode("utf-8"), 16))
    result = iv + _encrypted_text

    return b64encode(result).decode("utf-8")


def decrypt(encrypted_text, key):
    key = key.ljust(32, b"\0")[:32]
    _encrypted_text = b64decode(encrypted_text)
    iv = _encrypted_text[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    _decrypted_text = unpad(cipher.decrypt(_encrypted_text[16:]), 16).decode("utf-8")
    return _decrypted_text


original_text = "v1/pay/notify/42475895-e5c3-4a4b-9ae8-4898bffb3e61"
symmetric_key = get_random_bytes(32)

encrypted_text = encrypt(original_text, symmetric_key)
decrypted_text = decrypt(encrypted_text, symmetric_key)

base_url = "https://vitor.com.br/api/"
final_url = f"{base_url}{encrypted_text}"

print(f"Original Text: {original_text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
print(f"Hash Length: {len(encrypted_text)}")
print(f"Base URL: {base_url}")
print(f"Base URL Length: {len(base_url)}")
print(f"Final URL: {final_url}")
print(f"Final URL Length: {len(final_url)}")
