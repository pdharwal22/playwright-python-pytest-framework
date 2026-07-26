import logging
from pathlib import Path


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)

    log_direcotry = Path("reports/logs")
    log_direcotry.mkdir(parents=True, exist_ok=True)

    log_file = log_direcotry / "automation.log"
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

