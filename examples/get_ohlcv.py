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

print(spot_DGTXBTC)
ohlcv = client.get_k_lines(market_id=spot_DGTXBTC.id, resolution='1D')
print(ohlcv)


# dumb example trading wise however it shows the usage of data classes
closes = [i.close for i in ohlcv.ohlcv]
print(closes)
