
import sys
import logging
import traceback
class ErrorHandler:

    def __init__(self, log_file='error.log'):
        logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')

    def handle_error(self, e, classname, funcname):
        if isinstance(e, FileNotFoundError):
            print(f'Error: can not find the file {e.filename}')
        elif isinstance(e, ImportError):
            print(f'Error: An error occurred while importing the required libraries')
        logging.error(f'Error: {e} Exception type: {type(e).__name__} Class name: {classname} Function name: {funcname}')
        sys.exit()
        