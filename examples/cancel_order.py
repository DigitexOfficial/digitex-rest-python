# add dgtx to path
import sys
from decimal import Decimal

sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException
from dgtx.digitex_rest_core.model.cancel_order import CancelOrder

client = Client(
    api_client=Client.testnet,
    api_key='4384ac7676cf1254e95366977c3747ca24b5295a'
)

# get order to cancel
orders = client.get_orders()
# print(orders)

orders_to_cancel = CancelOrder(
    market_id=1,  # unique order id is insured only per market level
    orders_client_ids=[i.client_id for i in orders.results]  # list of orders to cancel
)

cancel_order = client.cancel_order(orders_to_cancel)
print(cancel_order)