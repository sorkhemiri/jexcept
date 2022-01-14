import pytest

from jexcept import JException, status
from jexcept import BaseJException


class BaseExceptionTestCase:

    @staticmethod
    def test_input():
        err = JException()
        assert err.http_status == 500
        assert err.message == ""

        err = JException(message="error message", http_status=status.BAD_REQUEST_400)
        assert err.http_status == 400
        assert err.message == "error message"

    @staticmethod
    def test_dict():
        err = JException(message="error message", http_status=status.BAD_REQUEST_400, detail="error detail")
        assert err.dict() == {"Exception": "error message", "Detail": "error detail"}

    @staticmethod
    def test_raise():
        with pytest.raises(BaseJException):
            raise JException()

        try:
            raise JException(message="error message", http_status=status.BAD_REQUEST_400, detail="error detail")
        except BaseJException as err:
            assert err.http_status == 400
            assert err.message == "error message"
            assert err.detail == "error detail"
