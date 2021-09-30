# add dgtx to path
import sys

sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-API-TOKEN-HERE'
)

# get the list of markets
markets = client.get_markets(market_id=1)

print(markets)

order_book = client.get_order_book(market_id=markets[0].id)

print(order_book)

# return instance in most of the cases is a python class
# which allows to access its properties directly
if not isinstance(markets, ApiException):
    print(
        f"Best ask for {markets[0].name} is\n"
        f"{[min(order_book.asks, key=lambda ask: ask[0])][-1][0]}"
    )
