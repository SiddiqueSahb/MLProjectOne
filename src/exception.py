
import sys
import os
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from exception import CustomException
from logger import logging
import pandas as pd
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """Gives detailed error information: filename, line number, and error message."""
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback info
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where error occurred
    line_number = exc_tb.tb_lineno  # Get the line number where error occurred
    error_message = (
        "Error occurred in Python script: [{0}] "
        "Line number: [{1}] "
        "Error message: [{2}]".format(file_name, line_number, str(error))
    )
    return error_message


class CustomException(Exception):
    """Custom Exception to handle detailed error messages."""
    def __init__(self, error_message, error_detail: sys):
        # Call the parent class constructor to initialize the exception with the error message
        super().__init__(error_message)
        # Use the error_message_detail function to capture detailed error information
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        # Return the error message
        return self.error_message
    
