from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend()
)

public_key = private_key.public_key()

original_message = b"v1/pay/notify/42475895-e5c3-4a4b-9ae8-4898bffb3e61"

encrypted = public_key.encrypt(
    original_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

decrypted_message = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

base_url = "https://vitor.com.br/api/"
final_url = f"{base_url}{encrypted}"

print(f"Original Message: {original_message}")
print(f"Encrypted Message: {encrypted}")
print(f'Decrypted Message: {decrypted_message.decode("utf-8")}')
print(f"Hash Length: {len(encrypted)}")
print(f"Base URL: {base_url}")
print(f"Base URL Length: {len(base_url)}")
print(f"Final URL: {final_url}")
print(f"Final URL Length: {len(final_url)}")
