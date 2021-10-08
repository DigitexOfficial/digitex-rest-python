from dgtx.client import Client

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-TRADING-TOKEN-HERE'
)


def test_get_markets():
    assert client.get_markets(market_id=1)[0].id == 1
