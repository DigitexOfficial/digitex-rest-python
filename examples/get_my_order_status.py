# add dgtx to path
import sys

sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-API-TOKEN-HERE'
)

my_order = client.get_order_status(client_id='ec825f37-1af8-46ae-89d5-d2b0ffbdaf3f')
print(my_order)

# return instance in most of the cases is a python class
# which allows to access its properties directly
# if not isinstance(my_order_history, ApiException):
#     print(f"Ids if my orders on this page:"
#           f"{[i.client_id for i in my_order_history.results]}")
