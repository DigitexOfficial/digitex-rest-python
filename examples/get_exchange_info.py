# add dgtx to path
import sys
sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-API-TOKEN-HERE'
)

# get the list of exchange data
ex = client.get_exchange_info()
print(ex)

# return instance in most of the cases is a python class
# which allows to access its properties directly
if not isinstance(ex, ApiException):
    print(f"Order meta parameters:\n")
    print(ex.order_meta)
