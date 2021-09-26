# add dgtx to path
import sys
sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException

client = Client(
    api_client=Client.testnet,
    api_key='4384ac7676cf1254e95366977c3747ca24b5295a'
)

# get the list of markets
markets = client.get_markets()

# filter list of markets to get spot DGTXBTC
spot_DGTXBTC = [i for i in markets if i.name == "DGTX/BTC"][0]

order_book = client.get_order_book(market_id=spot_DGTXBTC.id)

print(order_book)

# return instance in most of the cases is a python class
# which allows to access its properties directly
if not isinstance(markets, ApiException):
    print(f"Best ask for {spot_DGTXBTC.name} is\n"
          f"{[min(order_book.asks, key=lambda ask:ask[0])][-1]}")