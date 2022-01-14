from .base_exception import BaseJException
from .status import INTERNAL_SERVER_ERROR_500


class JAPIException(BaseJException):
    HTTP_STATUS = INTERNAL_SERVER_ERROR_500
    MESSAGE = ""
    DETAIL = ""

    @classmethod
    def http_status(cls):
        return cls.HTTP_STATUS

    @classmethod
    def message(cls):
        return cls.MESSAGE

    @classmethod
    def detail(cls):
        return cls.DETAIL

    @classmethod
    def dict(cls):
        return {
            "Exception": cls.MESSAGE,
            "Detail": cls.DETAIL,
        }

    def __str__(self):
        return f"{self.__class__.__name__}:{self.MESSAGE}__HTTP STATUS({self.HTTP_STATUS})"

    def __repr__(self):
        return f"{self.__class__.__name__}:<HTTP STATUS({self.HTTP_STATUS})>"
