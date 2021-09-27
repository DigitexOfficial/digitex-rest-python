# add dgtx to path
import sys

sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-API-TOKEN-HERE'
)

my_trade_history = client.get_order_history(page_size=3)
print(my_trade_history)

# return instance in most of the cases is a python class
# which allows to access its properties directly
if not isinstance(my_trade_history, ApiException):
    print(f"Quantity traded in the first trade on this page is "
          f"{my_trade_history.results[0].quantity}")
