import pytest

from jexcept import BaseJException, status
from jexcept import JAPIException


class BaseExceptionTestCase:

    @staticmethod
    def test_dict():
        class MyAPIException(JAPIException):
            MESSAGE = "error message"
            DETAIL = "error detail"
            HTTP_STATUS = status.BAD_REQUEST_400

        assert MyAPIException.dict() == {"Exception": "error message", "Detail": "error detail"}

    @staticmethod
    def test_raise():
        class MyAPIException(JAPIException):
            pass

        with pytest.raises(BaseJException):
            raise MyAPIException

        class MyAPIException(JAPIException):
            MESSAGE = "error message"
            DETAIL = "error detail"
            HTTP_STATUS = status.BAD_REQUEST_400

        try:
            raise MyAPIException
        except BaseJException as err:
            assert err.HTTP_STATUS == 400
            assert err.MESSAGE == "error message"
            assert err.DETAIL == "error detail"
