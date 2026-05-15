from NotebookFusion.custom_exception import InvalidURLException, NotebookFusionException
import sys

def test_invalid_url_exception():
    try:
        raise InvalidURLException("Test URL exception")
    except InvalidURLException as e:
        assert str(e) == "Test URL exception"

def test_notebook_fusion_exception():
    try:
        1 / 0
    except Exception as e:
        custom_exc = NotebookFusionException(e, sys)
        assert "division by zero" in str(custom_exc)
