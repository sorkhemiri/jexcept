from jexcept import JException, status


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
        err = JException(message="error message", http_status=status.BAD_REQUEST_400)
        assert err.dict() == {"Exception": "error message"}
