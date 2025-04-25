
from Crypto.Hash import SHAKE256

def get_shake_hash(data: bytes, length: int = 64) -> bytes:
    """
    Generate a SHAKE-256 hash of variable length.
    :param data: Input data in bytes
    :param length: Length of output hash in bytes
    :return: SHAKE256 hash
    """
    hasher = SHAKE256.new(data)
    return hasher.read(length)
