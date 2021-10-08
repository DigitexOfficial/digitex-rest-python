from dgtx.client import Client
from dgtx.digitex_rest_core.model.order_status import OrderStatus

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-TRADING-TOKEN-HERE'
)


def test_get_order_history():
    timestamp = 1632234345216613
    order_history_from = client.get_order_history(market_id=1, page_size=5, created_at_from=timestamp)
    # order_history_to = client.get_order_history(market_id=1, page_size=5, created_at_to=timestamp)
    order_history_by_status = client.get_order_history(status=3)
    market_id = set(instance['market_id'] for instance in order_history_from.results)
    assert all(instance['status'] == OrderStatus(3) for instance in order_history_by_status.results)
    assert len(order_history_from.results) == 5
    assert len(market_id) == 1 and market_id == {1}
    assert all(instance['created_at'] > timestamp for instance in order_history_from.results)
    # assert all(instance['created_at'] < timestamp for instance in order_history_to.results)
