from .base_exception import BaseJException
from .status import INTERNAL_SERVER_ERROR_500


class JException(BaseJException):
    def __init__(self, message: str = "", http_status: int = INTERNAL_SERVER_ERROR_500, detail: str = ""):
        super(JException, self).__init__(message)
        self.HTTP_STATUS = http_status
        self.MESSAGE = message
        self.DETAIL = detail

    def dict(self):
        return {
            "Exception": self.MESSAGE,
            "Detail": self.DETAIL,
        }

    def __str__(self):
        return f"{self.__class__.__name__}:{self.MESSAGE}__HTTP STATUS({self.HTTP_STATUS})"

    def __repr__(self):
        return f"{self.__class__.__name__}:<HTTP STATUS({self.HTTP_STATUS})>"
