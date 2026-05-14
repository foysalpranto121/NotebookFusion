import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from NotebookFusion.logger import logger

def test_logger_info():
    logger.info("This is an info message for testing.")

if __name__ == "__main__":
    test_logger_info()
    print("Logger test passed!")
