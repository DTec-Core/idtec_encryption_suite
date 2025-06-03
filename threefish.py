
import base64

BLOCK_SIZE = 32  # 256-bit for SHAKE-256 level

def encrypt_message(message: str, key: str) -> str:
    """
    padded = pad(message.encode(), BLOCK_SIZE)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(encrypted).decode()

def decrypt_message(encrypted: str, key: str) -> str:
    ""
    decoded = base64.b64decode(encrypted.encode())
    decrypted = unpad(cipher.decrypt(decoded), BLOCK_SIZE)
    return decrypted.decode()
