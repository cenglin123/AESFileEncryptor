# utils/file_operations.py （文件相关操作封装）

import os

def list_files(directory, recursive=True):
    """List all files in a directory."""
    if recursive:
        for root, _, files in os.walk(directory):
            for file in files:
                yield os.path.join(root, file)
    else:
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                yield os.path.join(directory, file)

def read_file(file_path):
    """Read a file's content."""
    with open(file_path, 'rb') as f:
        return f.read()

def write_file(file_path, data):
    """Write data to a file."""
    with open(file_path, 'wb') as f:
        f.write(data)
