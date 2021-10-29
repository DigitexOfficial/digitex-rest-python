from dgtx.client import Client

client = Client(
    api_client=Client.testnet,
    api_key='10d224aa74c8506d1862e65c7aeba05c05177cf2'
)

minute = 60000000


def test_get_k_lines():
    k_lines_minutes = client.get_k_lines(
        market_id=1, resolution='1', top_n=10, date_from=1620000000000000, date_to=1630000000000000
    )
    k_lines_days = client.get_k_lines(
        market_id=1, resolution='1D', top_n=10, date_from=1620000000000000, date_to=1630000000000000
    )
    k_lines_week = client.get_k_lines(
        market_id=1, resolution='1W', top_n=10, date_from=1620000000000000, date_to=1630000000000000
    )
    k_lines_month = client.get_k_lines(
        market_id=1, resolution='1M', top_n=10, date_from=1620000000000000, date_to=1630000000000000
    )
    k_lines = client.get_k_lines(
        market_id=1, resolution='1', top_n=10
    )
    k_lines_cash = client.get_k_lines(
        market_id=1, resolution='1D', top_n=10, date_from=1635379200000000
    )
    assert k_lines_minutes.market_id == 1
    assert len(k_lines.ohlcv) == 10
    assert len(k_lines_cash.ohlcv) == 3
    assert k_lines.ohlcv[0]['close'] and k_lines.ohlcv[0]['open'] >= k_lines.ohlcv[0]['low']
    assert k_lines.ohlcv[0]['close'] and k_lines.ohlcv[0]['open'] <= k_lines.ohlcv[0]['high']
    assert k_lines_minutes.ohlcv[-2]['timestamp'] - k_lines_minutes.ohlcv[-3]['timestamp'] == minute
    assert k_lines_days.ohlcv[-2]['timestamp'] - k_lines_days.ohlcv[-3]['timestamp'] == minute * 60 * 24
    assert k_lines_week.ohlcv[-2]['timestamp'] - k_lines_week.ohlcv[-3]['timestamp'] == minute * 60 * 24 * 7
    assert k_lines_month.ohlcv[-2]['timestamp'] - k_lines_month.ohlcv[-3]['timestamp'] == minute * 60 * 24 * 30
