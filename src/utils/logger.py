# utils/logger.py （日志工具）

import logging

def setup_logger(name, level=logging.DEBUG):
    """Set up a logger with a specific name and level."""
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
