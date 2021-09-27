# add dgtx to path
import sys
sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-API-TOKEN-HERE'
)

# get the list of currencies
currencies = client.get_currencies()
print(currencies)

# return instance in most of the cases is a python class
# which allows to access its properties directly
if not isinstance(currencies, ApiException):
    print(f"Id of the first currency in the list is {currencies[0].id}"
          f", currency name is {currencies[0].name}")