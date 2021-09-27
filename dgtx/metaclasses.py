from dgtx.decorators import decimal_args_to_string, return_decimals

"""
Example usage:
```
    class Request(metaclass=RequestMeta):
        def get(self, *args, **kwargs):
            # given arguments decimal values are converted to string
            ....


    class Response(metaclass=ResponseMeta):
        def data(self, *args, **kwargs):
            return {'field': Decimal('1.1')}


    response = Response()
    data = response.data()  # `data` should now be equal to {'field': '1.1'}
```
"""


class ResponseMeta(type):
    """Metaclass that wraps every factored class bound methods with `string_to_decimal` decorator."""

    def __new__(mcs, what, bases, attrs):
        _attrs = {name: return_decimals(attr) if callable(attr) else attr for name, attr in attrs.items()}
        return super().__new__(mcs, what, bases, _attrs)


class RequestMeta(type):
    """Metaclass that wraps every factored class bound methods with `decimal_to_string` decorator."""

    def __new__(mcs, what, bases, attrs):
        _attrs = {name: decimal_args_to_string(attr) if callable(attr) else attr for name, attr in attrs.items()}
        return super().__new__(mcs, what, bases, _attrs)


class ClientMeta(RequestMeta, ResponseMeta):
    """Metaclass uses both above cases."""
