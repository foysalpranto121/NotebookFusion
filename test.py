import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from NotebookFusion.logger import logger
from NotebookFusion.custom_exception import InvalidURLException


def test_logger_info():
    logger.info("This is an info message for testing.")


def test_invalid_url_exception():
    try:
        raise InvalidURLException("This is a test for InvalidURLException.")
    except InvalidURLException as e:
        logger.error(f"Caught expected exception: {e}")
        print("InvalidURLException test passed!")


if __name__ == "__main__":
    test_logger_info()
    print("Logger test passed!")
    test_invalid_url_exception()
