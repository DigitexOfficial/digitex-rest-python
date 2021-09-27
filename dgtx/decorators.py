import decimal
import logging

from decimal import Decimal
from functools import wraps
from typing import Callable, Mapping, MutableSequence

from dgtx.digitex_rest_core.model_utils import OpenApiModel


logger = logging.getLogger(__name__)


def isfloat(value: str) -> bool:
    """
    Checks if given string is convertable to float.
    Require consistent lazy `and` check!
    """

    if isinstance(value, str):
        if value.replace('.', '', 1).isdigit():
            return True
        try:  # TODO need to find more elegant way to detect
            # workaround if it is scientific notation
            Decimal(value)
            return True
        except decimal.InvalidOperation:
            return False
    else:
        return False

    # dcml = value and isinstance(value, str) and value.replace('.', '', 1).isdigit()

    # return value and isinstance(value, str) and '.' in value and value.replace('.', '', 1).isdigit()
    # return value and isinstance(value, str) and 'E-' in value and value.replace('.', '', 1).isdigit()


def decimal_args_to_string(function: Callable) -> Callable:
    """
    Wrapps given callable and changes it arguments and keyword arguments so presented decimals are converted to string.
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        args = *tuple(str(value) if isinstance(value, Decimal) else value for value in args),
        kwargs = {key: str(value) if isinstance(value, Decimal) else value for key, value in kwargs.items()}
        return function(*args, **kwargs)
    return wrapper


def string_values_to_decimal(obj):
    if isfloat(obj):
        obj: Decimal = Decimal(obj)
    elif isinstance(obj, Mapping):
        Map = type(obj)
        obj: Map = Map({key: string_values_to_decimal(value) for key, value in obj.items()})
    elif isinstance(obj, MutableSequence):
        Sequence = type(obj)
        obj: Sequence = Sequence(string_values_to_decimal(value) for value in obj)
    elif isinstance(obj, OpenApiModel) and hasattr(obj, '_data_store'):
        obj._data_store.update({key: string_values_to_decimal(value) for key, value in obj._data_store.items()})
    return obj


def return_decimals(function: Callable) -> Callable:
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return string_values_to_decimal(result)
    return wrapper


def string_to_decimal(function: Callable) -> Callable:
    """NOT IN USE!
    Wrapps given callable and changes it return value whether its Mapping, Sequence or OpenApiModel
        so presented float-like strings are converted to decimal.
    Result object type is equivelent to original one, given that
        mapping object could not just be dict (e.g. OrderedDict),
        sequence object could not junst be list (e.g. ReturnList),
        same for OpenApiModel objects.
    Uses case for nested maps and sequences in first depth applying same logic
        although their types are by default dict or list respectively.
    """
    @wraps(function)
    def wrapper(*args,  **kwargs):
        result = function(*args, **kwargs)
        if isinstance(result, Mapping):
            Map = type(result)
            _result = Map()
            for field, obj in result.items():
                if isfloat(obj):
                    _result[field] = Decimal(obj)
                elif isinstance(obj, Mapping):
                    _result[field] = {key: Decimal(value) if isfloat(value) else value for key, value in obj.items()}
                elif isinstance(obj, MutableSequence):
                    _result[field] = [Decimal(value) if isfloat(value) else value for value in obj]
                else:
                    _result[field] = obj
            return _result

        elif isinstance(result, OpenApiModel) and hasattr(result, '_data_store'):
            _data_store = dict()
            for field, obj in result._data_store.items():
                if isfloat(obj):
                    _data_store[field] = Decimal(obj)
                elif isinstance(obj, Mapping):
                    _data_store[field] = {
                        key: Decimal(value) if isfloat(value) else value for key, value in obj.items()
                    }
                elif isinstance(obj, MutableSequence):
                    _data_store[field] = [Decimal(value) if isfloat(value) else value for value in obj]
                elif isinstance(obj, OpenApiModel) and hasattr(obj, '_data_store'):
                    __data_store = dict()
                    for _field, _obj in obj._data_store.items():
                        if isfloat(_obj):
                            __data_store[_field] = Decimal(_obj)
                        elif isinstance(_obj, Mapping):
                            __data_store[_field] = {
                                _key: Decimal(_value) if isfloat(_value) else _value for _key, _value in _obj.items()
                            }
                        elif isinstance(_obj, MutableSequence):
                            __data_store[_field] = [Decimal(_value) if isfloat(_value) else _value for _value in _obj]
                        else:
                            _data_store[field] = obj
                    obj._data_store = __data_store
                else:
                    _data_store[field] = obj
            result._data_store = _data_store
            return result

        elif isinstance(result, MutableSequence):
            Seq = type(result)
            _result = Seq()
            for obj in result:
                if isfloat(obj):
                    _result.append(Decimal(obj))
                elif isinstance(obj, OpenApiModel) and hasattr(obj, '_data_store'):
                    _data_store = dict()
                    for field, obj_ in obj._data_store.items():
                        if isfloat(obj_):
                            _data_store[field] = Decimal(obj_)
                        elif isinstance(obj_, Mapping):
                            _data_store[field] = {
                                key: Decimal(value) if isfloat(value) else value for key, value in obj.items()
                            }
                        elif isinstance(obj_, MutableSequence):
                            _data_store[field] = [Decimal(value) if isfloat(value) else value for value in obj_]
                        elif isinstance(obj_, OpenApiModel) and hasattr(obj_, '_data_store'):
                            __data_store = dict()
                            for _field, _obj in obj_._data_store.items():
                                if isfloat(_obj):
                                    __data_store[_field] = Decimal(_obj)
                                elif isinstance(_obj, Mapping):
                                    __data_store[_field] = {
                                        _key: Decimal(_value) if isfloat(_value) else _value for _key, _value in
                                        _obj.items()
                                    }
                                elif isinstance(_obj, MutableSequence):
                                    __data_store[_field] = [
                                        Decimal(_value) if isfloat(_value) else _value for _value in _obj
                                    ]
                                else:
                                    __data_store[_field] = _obj
                            obj_._data_store = __data_store
                        else:
                            _data_store[field] = obj_
                    obj._data_store = _data_store
                    _result.append(obj)
                elif isinstance(obj, Mapping):
                    _result.append({key: Decimal(value) if isfloat(value) else value for key, value in obj.items()})
                elif isinstance(obj, MutableSequence):
                    _result.append([Decimal(value) if isfloat(value) else value for value in obj])
                else:
                    _result.append(obj)
            return _result

        else:
            if result is not None:
                logger.warning("Decorated function does not return Mapping, Sequence or OpenApiModel object.")
            return result

    return wrapper
