from dgtx.client import Client

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-TRADING-TOKEN-HERE'
)


def test_get_recent_trades():
    recent_trades = client.get_recent_trades(market_id=1, max_trades=10)
    assert len(recent_trades.recent_trades) == 10
    assert recent_trades.market_id == 1
