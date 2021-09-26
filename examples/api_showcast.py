# add dgtx to path
import sys
from time import sleep

sys.path.append('../.')

from dgtx.extra_data_classes import PlaceOrderMeta, UpdateOrderMeta
from decimal import Decimal
from dgtx.digitex_rest_core.model.cancel_order import CancelOrder
from dgtx.digitex_rest_core.model.order_duration import OrderDuration
from dgtx.digitex_rest_core.model.order_side import OrderSide

from dgtx.digitex_rest_core.model.order_type import OrderType
from dgtx.digitex_rest_core import ApiException
from dgtx.client import Client

client = Client(
    api_client=Client.testnet,
    api_key='4384ac7676cf1254e95366977c3747ca24b5295a'
)

# # client either returns a data class or ApiException instance
# # error code can be found in ApiException.status
# # more detailed error description is in ApiException.reason
#
# # ping the exchange
# ping = client.ping()
# print(ping)
#
# # return instance in most of the cases is a python class
# # which allows to access its properties directly
# if not isinstance(ping, ApiException):
#     print(f"Current server time in nanoseconds is {ping.timestamp}")
#
# # most of the meta data needed to start trading is in the
# # get_exchange info method of the client
#
# ex = client.get_exchange_info()
# # exchange info consists of several attributes
# # >>>> order_meta
# # it contains dictionaries of accepted order parameters, such as
# # duration (GTC, IOC, etc), position (LONG, SHORT), side (Buy, Sell),
# # type (LIMIT order or MARKET order)
# if not isinstance(ex, ApiException):
#     print(ex.order_meta)
#
# # these properties can be accessed in the following way:
# print(f"This is how you access order meta parameters without the need"
#       f" to memorize it: ex.order_meta.type['LIMIT'] -> {ex.order_meta.type['LIMIT']}")
#
# # >>> ex.currencies
# # This is a list of currencies available to work with at the exchange.
# print(ex.currencies)
#
# # >>> ex.markets
# # This is a list of markets that is available to trade
# print(ex.markets)
#
# ##################################
# ##### Exchange market info #######
# ##################################
#
# # order book
# order_book = client.get_order_book(
#     market_id=2  # Market DGTX/ETH
# )
# print(order_book)
#
# # recent trades
# recent_trades = client.get_recent_trades(market_id=1, max_trades=2)
# print(recent_trades)
#
# # ohlcv or klines

ohlc = client.get_k_lines(market_id=1, resolution='1D')
print(ohlc)


# #################################
# ######### Trader's info #########
# #################################
#
# # get my balance
# my_balance = client.get_balance()
# print(my_balance)

# get my position
# my_position = client.get_position()
# print(my_position)
#
# # my open orders
# my_open_orders = client.get_orders()
# print(my_open_orders)
# #
# # my order history
# my_order_history = client.get_order_history(page_size=2)
# print(my_order_history)
#
# ##########################
# ###### TRADING ###########
# ##########################
#
# place order
# new_order = PlaceOrderMeta(
#     market_id=1,
#     side=OrderSide(1),
#     duration=OrderDuration(2),
#     leverage=10,
#     type=OrderType(2),
#     quantity=Decimal(9),
#     price=Decimal(38000)
# )
#
# placed_order = client.place_order(new_order)
# print(placed_order)

# get order status
# orders = client.get_orders()
# order_status = client.get_order_status(orders.results[0].client_id)
# print(order_status)

# cancel order

# get order to cancel
orders = client.get_orders()
# print(orders)
#
orders_to_cancel = CancelOrder(
    market_id=1,  # unique order id is insured only per market level
    orders_client_ids=[i.client_id for i in orders.results]  # list of orders to cancel
)
#
# cancel_order = client.cancel_order(orders_to_cancel)
# print(cancel_order)

# sleep(2)
#
# order_to_update = UpdateOrderMeta(
#     cliend_id=placed_order.client_id,
#     market_id=placed_order.market_id,
#     side=placed_order.side,
#     duration=placed_order.duration,
#     leverage=placed_order.leverage,
#     type=placed_order.type,
#     quantity=placed_order.quantity,
#     price=Decimal(37000)
# )
#
# updated_order = client.update_order(order_to_update)
# print(updated_order)
# orders = client.get_orders()
# print(orders)

