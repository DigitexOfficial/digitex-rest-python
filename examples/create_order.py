# add dgtx to path
import sys
from decimal import Decimal
sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException
from dgtx.digitex_rest_core.model.order_duration import OrderDuration
from dgtx.digitex_rest_core.model.order_side import OrderSide
from dgtx.digitex_rest_core.model.order_type import OrderType
from dgtx.extra_data_classes import PlaceOrderMeta

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-API-TOKEN-HERE'
)

# place order
new_order = PlaceOrderMeta(
    market_id=1, # BTCUSDS Futures
    side=OrderSide(1),
    duration=OrderDuration(2),
    leverage=10,
    type=OrderType(2),
    quantity=Decimal(9),
    price=Decimal(38000)
)

placed_order = client.place_order(new_order)
print(placed_order) # returns new order. to get order status query client.get_order_status