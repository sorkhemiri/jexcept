import pytest

from jexcept import JException, status
from jexcept import BaseJException


class BaseExceptionTestCase:

    @staticmethod
    def test_input():
        err = JException()
        assert err.HTTP_STATUS == 500
        assert err.MESSAGE == ""

        err = JException(message="error message", http_status=status.BAD_REQUEST_400)
        assert err.HTTP_STATUS == 400
        assert err.MESSAGE == "error message"

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
            assert err.HTTP_STATUS == 400
            assert err.MESSAGE == "error message"
            assert err.DETAIL == "error detail"
