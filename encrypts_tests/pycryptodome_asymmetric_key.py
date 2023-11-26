from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

private_key = RSA.generate(2048)
public_key = private_key.publickey()

original_text = b"v1/pay/notify/42475895-e5c3-4a4b-9ae8-4898bffb3e61"

cipher = PKCS1_OAEP.new(public_key)
encrypted_text = cipher.encrypt(original_text)

cipher = PKCS1_OAEP.new(private_key)
decrypted_text = cipher.decrypt(encrypted_text).decode("utf-8")


base_url = "https://vitor.com.br/api/"
final_url = f"{base_url}{encrypted_text.hex()}"

print(f'Original Text: {original_text.decode("utf-8")}')
print(f"Encrypted Text: {encrypted_text.hex()}")
print(f"Decrypted Text: {decrypted_text}")
print(f"Hash Length: {len(encrypted_text.hex())}")
print(f"Base URL: {base_url}")
print(f"Base URL Length: {len(base_url)}")
print(f"Final URL: {final_url}")
print(f"Final URL Length: {len(final_url)}")
