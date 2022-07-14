import os
import sys

class ShipmentException(Exception):
    """
    Custom exception class for shipment price prediction.
    """
    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message) # passing the error to the parent class 
        self.error_message = ShipmentException.get_detailed_error_message(error_message= error_message, error_detail= error_detail)

    def get_detailed_error_message(error_message:Exception, error_detail: sys)->str:

        """
        error_message: Exception object
        error_detail: object of sys module
        """

        _,_,error = error_detail.exc_info() # from the error details, get the traceback of the error. 
                                            # It returns tuples of (filename, line number, function name, text)

        script_name = error.tb_frame.f_code.co_filename # get the file name from the traceback
        function_name = error.tb_frame.f_code.co_name # get the function name from the traceback
        try_block_line_no = error.tb_lineno # get the line number of the error in the try block
        exception_block_line_no = error.tb_frame.f_lineno # get the line number of the exception block error    


        error_msg = f"""
        Error occurred in script:[{script_name}]
        in function: [{function_name}]
        at try block line number: [{try_block_line_no}]
        and exception block line number:[{exception_block_line_no}]
        Error message: [{error_message}]
        """        
        
        return error_msg

    def __str__(self):
        return self.error_message

    def __repr__(self)->str:
        return ShipmentException.__name__.str()