from dgtx.client import Client

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-TRADING-TOKEN-HERE'
)


def test_get_order_book():
    assert client.get_order_book(market_id=1).market_id == 1

