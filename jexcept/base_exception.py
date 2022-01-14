from .status import INTERNAL_SERVER_ERROR_500


class JException(Exception):
    def __init__(self, message: str = "", http_status: int = INTERNAL_SERVER_ERROR_500):
        super(JException, self).__init__(message)
        self.__http_status = http_status
        self.__message = message

    @property
    def http_status(self):
        return self.__http_status

    @property
    def message(self):
        return self.__message

    def dict(self):
        return {
            "Exception": self.message,
        }

    def __str__(self):
        return f"{self.__class__.__name__}:{self.__message}__HTTP STATUS({self.__http_status})"

    def __repr__(self):
        return f"{self.__class__.__name__}:<HTTP STATUS({self.__http_status})>"
