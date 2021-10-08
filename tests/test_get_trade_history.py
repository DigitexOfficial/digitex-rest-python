from dgtx.client import Client

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-TRADING-TOKEN-HERE'
)


def test_get_trade_history():
    timestamp = 1632234345216613
    trade_history_from = client.get_trade_history(page_size=5, market_id=1, traded_at_from=timestamp)
    trade_history_to = client.get_trade_history(page_size=5, market_id=1, traded_at_to=timestamp)
    market_id = set(instance['market_id'] for instance in trade_history_from.results)
    assert len(trade_history_from.results) == 5
    assert len(market_id) == 1 and market_id == {1}
    assert all(instance['traded_at'] > timestamp for instance in trade_history_from.results)
    assert all(instance['traded_at'] < timestamp for instance in trade_history_to.results)
