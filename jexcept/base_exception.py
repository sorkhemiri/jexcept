import abc


class BaseJException(Exception):
    HTTP_STATUS = None
    MESSAGE = None
    DETAIL = None

    @abc.abstractmethod
    def dict(self):
        pass
