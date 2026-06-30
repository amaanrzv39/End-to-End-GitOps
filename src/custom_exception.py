import traceback
import sys

class CustomException(Exception):

    def __init__(self, error_message: str, error_detail:Exception):  
        self.error_message = self.get_detailed_error_message(error_message, error_detail)
        super().__init__(self.error_message)
        
    @staticmethod
    def get_detailed_error_message(error_message, error_detail):

        _, _, exc_tb = traceback.sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return f"Error in {file_name} | line {line_number} | {error_message} | detail: {error_detail}"
    
    def __str__(self):
        return self.error_message