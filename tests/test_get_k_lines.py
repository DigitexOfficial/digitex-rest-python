from dgtx.client import Client

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-TRADING-TOKEN-HERE'
)


def test_get_k_lines():
    k_lines = client.get_k_lines(
        market_id=1, resolution='1', top_n=10, date_from=1620000000000000, date_to=1630000000000000
    )
    assert k_lines.market_id == 1
    assert k_lines.ohlcv[-1]['timestamp'] - k_lines.ohlcv[-2]['timestamp'] == 60000000
    assert len(k_lines.ohlcv) == 10
