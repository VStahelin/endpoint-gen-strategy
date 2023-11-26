from cryptography.fernet import Fernet
import zlib

secret_key = Fernet.generate_key()

cipher_suite = Fernet(secret_key)

original_text = "v1/pay/notify/42475895-e5c3-4a4b-9ae8-4898bffb3e61"

compressed_data = zlib.compress(original_text.encode())

encrypted_text = cipher_suite.encrypt(compressed_data).decode()

print("Encrypted Text:", encrypted_text)

decrypted_text = zlib.decompress(cipher_suite.decrypt(encrypted_text)).decode()

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
