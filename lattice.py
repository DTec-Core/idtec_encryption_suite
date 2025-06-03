
import os
from idtec_core.shake_hash import get_shake_hash

def verify_signature(message: bytes, signature: bytes, public_key: bytes) -> bool:
    """
    expected = get_shake_hash(message + public_key, 64)
    return expected == signature
