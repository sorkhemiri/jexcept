# JExcept
### Json Serializable Exceptions for Python.

jexcept is a framework-independent wrapper around python exception making error handling easier and more detailed in web applications.
```python
from jexcept import JAPIException, status
class CustomException(JAPIException):
    MESSAGE = "Error Message"
    DETAIL = "Error Detail"
    HTTP_STATUS = status.BAD_REQUEST_400

raise CustomException
```
## Features
raise exceptions in any level of your application and catch them with detail, covert them to json serializable response.

## Installation
Jexcept is on [PyPI](https://pypi.org/project/JExcept/), so all you need to do is:
```shell
pip install jexcept
```

## Testing
just run:
```shell
make test
```
## Contributing
Please see the [Contribution Guidelines](Contribution.md).

## Copyright
JExcept is an open source project by Mahdi Sorkhemiri. See the [license](LICENSE) file for more information.