import logging
import os
from datetime import datetime 


# Generate the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs path and ensure the logs directory exists
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up the logger with basicConfig
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Corrected the argument name to 'filename'
    level=logging.INFO,  # Set the log level to info
    format="[%(asctime)s] - %(lineno)s - %(name)s"  # Corrected format string
)

