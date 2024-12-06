from setuptools import setup, find_packages

setup(
    name="AESFileEncryptor",
    version="1.0.0",
    description="A tool for encrypting and decrypting files and folders using AES-256",
    author="层林尽染",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["aes_encryptor"],  # 添加这一行，明确包含主脚本
    install_requires=[
        "pycryptodome>=3.10.1"
    ],
    entry_points={
        "console_scripts": [
            "aes-enc=aes_encryptor:main"
        ]
    },
)
