from dgtx.client import Client
from dgtx.digitex_rest_core.model.order_status import OrderStatus

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-TRADING-TOKEN-HERE'
)

timestamp = 1632234345216613

get_currencies_response = client.get_currencies()
get_order_book_response = client.get_order_book(market_id=1)
get_recent_trades_response = client.get_recent_trades(market_id=1, max_trades=10)
get_k_lines_response = client.get_k_lines(
        market_id=1, resolution='1', date_from=1629999100000000, date_to=1629999200000000
    )
get_exchange_info_response = client.get_exchange_info()
get_markets_response = client.get_markets(market_id=1)
get_order_status_response = client.get_order_status(client_id='7fce7478-a241-4b0d-bca3-2948d0f7ce2e')
get_orders_response = client.get_orders()
get_trade_history_response = client.get_trade_history(page_size=5)
get_order_history_response = client.get_order_history(status=3)
get_balance_response = client.get_balance()
get_position_response = client.get_position()


print(get_order_history_response.results)