# flake8: noqa

"""
    Digitex Rest Trading API

    <br> <h4>Digitex's REST trading api specification</h4>  In order to start, one has to register either at https://testnet.digitexfutures.com for testnet (virtual funds trading) or at https://digitex.io - our mainnet (real money trading).  After registration you need to obtain your trading token in your account.  Direct links to the account page: - testnet - https://testnet.digitexfutures.com/profile/account - mainet - https://digitex.io/trade/profile/account  If you have already created your token, you can simply copy it, else click on \"Create\" in the API section of your account.   IMPORTANT NOTES!  - All of the data which is expected to be float or decimal are passed as strings. Data is converted into Decimal/float format on the client level - All timestamps are in microseconds UTC - Enums, such as order types, status etc can be found in Exchange-Meta-Data group of endpoints  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: spavlyuk@digitex.io
    Generated by: https://openapi-generator.tech
"""


__version__ = "0.0.1"

# import ApiClient
from dgtx.digitex_rest_core.api_client import ApiClient

# import Configuration
from dgtx.digitex_rest_core.configuration import Configuration

# import exceptions
from dgtx.digitex_rest_core.exceptions import OpenApiException
from dgtx.digitex_rest_core.exceptions import ApiAttributeError
from dgtx.digitex_rest_core.exceptions import ApiTypeError
from dgtx.digitex_rest_core.exceptions import ApiValueError
from dgtx.digitex_rest_core.exceptions import ApiKeyError
from dgtx.digitex_rest_core.exceptions import ApiException
