# add dgtx to path
import sys
sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-TRADING-TOKEN-HERE'
)

# get the list of markets
markets = client.get_markets()
print(markets)

# return instance in most of the cases is a python class
# which allows to access its properties directly
if not isinstance(markets, ApiException):
    print(f"Id of the first market in the list is {markets[0].id}"
          f", market description is {markets[0].description}")