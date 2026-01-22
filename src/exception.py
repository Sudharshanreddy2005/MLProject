import sys
from typing import Optional


def error_message_detail(error: Exception, error_detail: Optional[object] = None) -> str:
    _, _, exc_tb = sys.exc_info()

    if exc_tb is None:
        return f"Error message: {str(error)}"

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = (
        f"Error occurred in script: [{file_name}] "
        f"at line number: [{line_number}] "
        f"error message: [{str(error)}]"
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: Optional[object] = None):
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
