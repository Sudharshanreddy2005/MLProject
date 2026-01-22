import logging
import os
from datetime import datetime

# Folder where logs will be stored
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name (ONLY filename)
LOG_FILE_NAME = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Full path = logs folder + filename
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)
