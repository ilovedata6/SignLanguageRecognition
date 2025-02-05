import sys
from signLanguage.logger import logging


def error_message_detail(error, error_detail: sys):
    """
    Generate detailed error message including filename, line number, and error message
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    return error_message


class SignLanguageException(Exception):
    """
    Custom exception class for Sign Language Detection project
    """
    
    def __init__(self, error_message, error_detail):
        """
        :param error_message: Error message in string format
        :param error_detail: sys module containing error detail
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)
        
        # Log the error message using the logger
        logging.error(self.error_message)

    def __str__(self):
        # Only return the custom error message without the traceback
        return self.error_message
