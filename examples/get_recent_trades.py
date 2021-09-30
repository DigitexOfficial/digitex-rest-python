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

recent_trades = client.get_recent_trades(market_id=markets[0].id, max_trades=2)

print(recent_trades)