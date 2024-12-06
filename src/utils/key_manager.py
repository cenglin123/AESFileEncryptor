# utils/key_manager.py （密钥管理功能）

import hashlib
import sys

def load_static_key():
    """Load a fixed static key for encryption and decryption."""
    # A fixed 256-bit (32-byte) key for AES-256
    return b"This_is_a_fixed_key_for_AES_256!".ljust(32, b"_")

def generate_key(source_data):
    """Generate a 256-bit key from the provided source data."""
    return hashlib.sha256(source_data).digest()

def load_key_from_program():
    """Generate a key based on the current program's binary."""
    with open(sys.argv[0], 'rb') as f:
        program_data = f.read()
    return generate_key(program_data)
