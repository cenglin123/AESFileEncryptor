import argparse
import os
import logging
from utils.logger import setup_logger
from utils.file_operations import read_file, write_file, list_files
from utils.key_manager import load_static_key, generate_key
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import shutil
import tempfile

logger = setup_logger(__name__)

class AESFileEncryptor:
    def __init__(self, password=None):
        self.key = generate_key(password.encode()) if password else load_static_key()
        self.block_size = 16
        logger.debug("AESFileEncryptor initialized with block size: %s", self.block_size)

    def encrypt_file(self, file_path):
        logger.debug("Encrypting file: %s", file_path)
        data = read_file(file_path)
        cipher = AES.new(self.key, AES.MODE_CBC)
        encrypted_data = cipher.encrypt(pad(data, self.block_size))

        encrypted_file = file_path + '.encrypted'
        write_file(encrypted_file, cipher.iv + encrypted_data)
        logger.debug("Encryption complete: %s -> %s", file_path, encrypted_file)

    def decrypt_file(self, file_path):
        logger.debug("Decrypting file: %s", file_path)
        try:
            data = read_file(file_path)
            iv = data[:16]
            encrypted_data = data[16:]
            cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
            decrypted_data = unpad(cipher.decrypt(encrypted_data), self.block_size)

            decrypted_file = file_path.replace('.encrypted', '')
            write_file(decrypted_file, decrypted_data)
            logger.debug("Decryption complete: %s -> %s", file_path, decrypted_file)
        except (ValueError, KeyError) as e:
            logger.error("Failed to decrypt file: %s. Possible incorrect password or file not encrypted.", file_path)

    def encrypt_folder(self, folder_path):
        logger.debug("Encrypting folder: %s", folder_path)
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        shutil.make_archive(temp_file.name, 'zip', folder_path)
        zip_path = temp_file.name + ".zip"

        data = read_file(zip_path)
        cipher = AES.new(self.key, AES.MODE_CBC)
        encrypted_data = cipher.encrypt(pad(data, self.block_size))

        encrypted_file = folder_path + '.encrypted'
        write_file(encrypted_file, cipher.iv + encrypted_data)
        os.remove(zip_path)
        logger.debug("Folder encryption complete: %s -> %s", folder_path, encrypted_file)

    def decrypt_folder(self, file_path):
        logger.debug("Decrypting folder file: %s", file_path)
        try:
            data = read_file(file_path)
            iv = data[:16]
            encrypted_data = data[16:]
            cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
            decrypted_data = unpad(cipher.decrypt(encrypted_data), self.block_size)

            temp_dir = tempfile.mkdtemp()
            zip_path = os.path.join(temp_dir, "decrypted.zip")
            write_file(zip_path, decrypted_data)

            folder_path = file_path.replace('.encrypted', '')
            shutil.unpack_archive(zip_path, folder_path)
            os.remove(zip_path)
            logger.debug("Folder decryption complete: %s -> %s", file_path, folder_path)
        except (ValueError, KeyError) as e:
            logger.error("Failed to decrypt folder file: %s. Possible incorrect password or file not encrypted.", file_path)

    def process_path(self, path):
        logger.debug("Processing path: %s", path)
        if os.path.isfile(path):
            if path.endswith('.encrypted'):
                self.decrypt_file(path)
            else:
                self.encrypt_file(path)
        elif os.path.isdir(path):
            if path.endswith('.encrypted'):
                self.decrypt_folder(path)
            else:
                self.encrypt_folder(path)

def main():
    parser = argparse.ArgumentParser(description="AES File/Folder Encryptor")
    parser.add_argument("paths", nargs='+', help="Files or folders to process")
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="DEBUG",
        help="Set the logger level",
    )
    parser.add_argument(
        "-p", "--password",
        type=str,
        help="Custom password for generating encryption key",
    )
    args = parser.parse_args()

    logger.setLevel(getattr(logging, args.log_level.upper(), logging.DEBUG))

    encryptor = AESFileEncryptor(password=args.password)

    for path in args.paths:
        if os.path.exists(path):
            encryptor.process_path(path)
        else:
            logger.error("Path does not exist: %s", path)

if __name__ == "__main__":
    main()
