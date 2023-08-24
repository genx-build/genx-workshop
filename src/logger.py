import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent.resolve() / "logs"
LOG_DIR.mkdir(exist_ok=True)

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%dT%H:%M:%S")

# stdout_handler = logging.StreamHandler(sys.stdout)
# stdout_handler.setLevel(logging.INFO)
# stdout_handler.setFormatter(formatter)

dt = datetime.now(timezone.utc)
log_file = LOG_DIR / f"output-{dt.year}-{dt.month}-{dt.day}.log"
file_handler = logging.FileHandler(filename=log_file,mode="a+",)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


def get_logger(name) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    # logger.addHandler(stdout_handler)
    return logger
