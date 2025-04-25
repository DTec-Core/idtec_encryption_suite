
import os
from idtec_core.shake_hash import get_shake_hash

def generate_signature_keypair():
    """
    Simulate generation of a lattice-based keypair.
    Replace with full lattice-based math engine.
    """
    private_key = os.urandom(64)
    public_key = get_shake_hash(private_key, 64)
    return private_key, public_key

def sign_message(message: bytes, private_key: bytes) -> bytes:
    """
    Sign a message with a private key using SHAKE-based hashing.
    """
    digest = get_shake_hash(message + private_key, 64)
    return digest

def verify_signature(message: bytes, signature: bytes, public_key: bytes) -> bool:
    """
    Verify the signature using message and public key.
    """
    expected = get_shake_hash(message + public_key, 64)
    return expected == signature
