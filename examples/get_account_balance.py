# add dgtx to path
import sys
sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-API-TOKEN-HERE'
)

my_balance = client.get_balance()
print(my_balance)

# return instance in most of the cases is a python class
# which allows to access its properties directly
if not isinstance(my_balance, ApiException):
    print(f"My available balances to trade:\n"
          f"{[(i.currency.code, i.available_balance) for i in my_balance]}")
