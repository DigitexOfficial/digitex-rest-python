"""
    Digitex Rest Trading API

    <br> <h4>Digitex's REST trading api specification</h4>  In order to start, one has to register either at https://testnet.digitexfutures.com for testnet (virtual funds trading) or at https://digitex.io - our mainnet (real money trading).  After registration you need to obtain your trading token in your account.  Direct links to the account page: - testnet - https://testnet.digitexfutures.com/profile/account - mainet - https://digitex.io/trade/profile/account  If you have already created your token, you can simply copy it, else click on \"Create\" in the API section of your account.   IMPORTANT NOTES!  - All of the data which is expected to be float or decimal are passed as strings. Data is converted into Decimal/float format on the client level - All timestamps are in microseconds UTC - Enums, such as order types, status etc can be found in Exchange-Meta-Data group of endpoints  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: spavlyuk@digitex.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from dgtx.digitex_rest_core.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from dgtx.digitex_rest_core.exceptions import ApiAttributeError


def lazy_import():
    from dgtx.digitex_rest_core.model.order_duration import OrderDuration
    from dgtx.digitex_rest_core.model.order_side import OrderSide
    from dgtx.digitex_rest_core.model.order_type import OrderType
    globals()['OrderDuration'] = OrderDuration
    globals()['OrderSide'] = OrderSide
    globals()['OrderType'] = OrderType


class PlaceOrder(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'market_id': (int,),  # noqa: E501
            'side': (OrderSide,),  # noqa: E501
            'type': (OrderType,),  # noqa: E501
            'duration': (OrderDuration,),  # noqa: E501
            'leverage': (int,),  # noqa: E501
            'quantity': (str,),  # noqa: E501
            'price': (str,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'market_id': 'market_id',  # noqa: E501
        'side': 'side',  # noqa: E501
        'type': 'type',  # noqa: E501
        'duration': 'duration',  # noqa: E501
        'leverage': 'leverage',  # noqa: E501
        'quantity': 'quantity',  # noqa: E501
        'price': 'price',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PlaceOrder - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            market_id (int): market id, can be found in markets instance. [optional]  # noqa: E501
            side (OrderSide): [optional]  # noqa: E501
            type (OrderType): [optional]  # noqa: E501
            duration (OrderDuration): [optional]  # noqa: E501
            leverage (int): Leverage of the trades, only valid for futures market and will be ignored for spot. [optional]  # noqa: E501
            quantity (str): quantity of the order. If you are trading futures, this is - amount of contracts.  for spot - it depends on your side.. [optional]  # noqa: E501
            price (str): price of the orders. [optional]  # noqa: E501
            client_id (str): user generated uidid. it is optional, the backend will generate one if nothing is provided. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """PlaceOrder - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            market_id (int): market id, can be found in markets instance. [optional]  # noqa: E501
            side (OrderSide): [optional]  # noqa: E501
            type (OrderType): [optional]  # noqa: E501
            duration (OrderDuration): [optional]  # noqa: E501
            leverage (int): Leverage of the trades, only valid for futures market and will be ignored for spot. [optional]  # noqa: E501
            quantity (str): quantity of the order. If you are trading futures, this is - amount of contracts.  for spot - it depends on your side.. [optional]  # noqa: E501
            price (str): price of the orders. [optional]  # noqa: E501
            client_id (str): user generated uidid. it is optional, the backend will generate one if nothing is provided. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
