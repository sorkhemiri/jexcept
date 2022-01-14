import abc


class BaseJException(Exception):
    @abc.abstractmethod
    def http_status(self):
        pass

    @abc.abstractmethod
    def message(self):
        pass

    @abc.abstractmethod
    def detail(self):
        pass

    @abc.abstractmethod
    def dict(self):
        pass
