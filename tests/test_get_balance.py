from dgtx.client import Client

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-TRADING-TOKEN-HERE'
)


def test_get_balance():
    assert client.get_balance()
