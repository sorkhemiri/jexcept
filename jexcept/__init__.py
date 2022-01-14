"""
    Json Serializable Exceptions for Python.
    :copyright: 2021 by Mahdi Sorkhemiri.
    :license: ISC, see LICENSE for more details.
"""
from .base_exception import JException
from . import status
__all__ = [JException, status]
