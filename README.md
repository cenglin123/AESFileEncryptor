# AESFileEncryptor
AES File/Folder Encryptor A Python-based tool for encrypting and decrypting files and folders using AES-256 encryption. Supports custom passwords, static keys, and drag-and-drop functionality when packaged as an executable.  基于 Python 的 AES-256 文件/文件夹加密解密工具。支持自定义密码、静态密钥，并在打包为可执行文件后支持拖放功能。

## AES File/Folder Encryptor

## Introduction
AES File/Folder Encryptor is a Python-based tool designed to secure sensitive data through AES-256 encryption. It allows users to encrypt and decrypt files or folders using a static key or a password-derived key for enhanced flexibility and security.

## Key Features
- **File Encryption/Decryption**: Encrypt files into `.encrypted` format and restore them when needed.
- **Folder Encryption/Decryption**: Encrypt entire folders into a `.encrypted` file and restore folder contents.
- **Custom Password Support**: Use a custom password to generate a secure encryption key.
- **Static Key Option**: Automatically fallback to a predefined static key if no password is provided.

## System Requirements
- **Python Version**: Python 3.8 or higher.
- **Dependencies**: Install required libraries using:
  ```bash
  pip install -r requirements.txt
  ```

## How to Use

### Command-Line Examples
#### Encrypt a File
```bash
aes-enc /path/to/file.txt
```
Encrypts `file.txt` to `file.txt.encrypted`.

#### Decrypt a File
```bash
aes-enc /path/to/file.txt.encrypted
```
Decrypts `file.txt.encrypted` back to `file.txt`.

#### Encrypt a Folder
```bash
aes-enc /path/to/folder
```
Compresses and encrypts the folder into `folder.encrypted`.

#### Use a Custom Password
```bash
aes-enc -p "MySecurePassword" /path/to/file.txt
```
Generates an encryption key based on the provided password.

### Drag-and-Drop Functionality
This tool supports drag-and-drop functionality when packaged as an executable file. Simply drag files or folders onto the `.exe` file, and the tool will automatically determine whether to encrypt or decrypt the input:

- Files with `.encrypted` extensions will be decrypted.
- Other files and folders will be encrypted.

## License
This project is licensed under the MIT License.

