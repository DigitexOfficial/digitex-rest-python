# add dgtx to path
import sys

sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-TRADING-TOKEN-HERE'
)

my_open_orders= client.get_orders(page_size=2)
print(my_open_orders)

# return instance in most of the cases is a python class
# which allows to access its properties directly
# if not isinstance(my_order_history, ApiException):
#     print(f"Ids if my orders on this page:"
#           f"{[i.client_id for i in my_order_history.results]}")
