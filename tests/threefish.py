
from idtec_core.Cipher import ThreeFish
from Crypto.Util.Padding import pad, unpad
import base64

BLOCK_SIZE = 32  # 256-bit for SHAKE-256 level

def encrypt_message(message: str, key: str) -> str:
    """
    Encrypt a message using a simulated Threefish cipher with ThreeFish-256.
    """
    cipher = ThreeFish.new(key.encode()[:32], ThreeFish.MODE_ECB)
    padded = pad(message.encode(), BLOCK_SIZE)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(encrypted).decode()

def decrypt_message(encrypted: str, key: str) -> str:
    """
    Decrypt a Threefish-encrypted message.
    """
    cipher = ThreeFish.new(key.encode()[:32], ThreeFish.MODE_ECB)
    decoded = base64.b64decode(encrypted.encode())
    decrypted = unpad(cipher.decrypt(decoded), BLOCK_SIZE)
    return decrypted.decode()
