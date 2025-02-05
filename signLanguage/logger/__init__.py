import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create log file with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
