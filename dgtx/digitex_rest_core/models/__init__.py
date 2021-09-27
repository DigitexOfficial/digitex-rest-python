# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from dgtx.digitex_rest_core.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from dgtx.digitex_rest_core.model.bad_request_type import BadRequestType
from dgtx.digitex_rest_core.model.balance import Balance
from dgtx.digitex_rest_core.model.cancel_order import CancelOrder
from dgtx.digitex_rest_core.model.currency import Currency
from dgtx.digitex_rest_core.model.drf_generic_exception import DRFGenericException
from dgtx.digitex_rest_core.model.exchange_info import ExchangeInfo
from dgtx.digitex_rest_core.model.exchange_order_book import ExchangeOrderBook
from dgtx.digitex_rest_core.model.exchange_recent_trade import ExchangeRecentTrade
from dgtx.digitex_rest_core.model.exchange_recent_trade_list import ExchangeRecentTradeList
from dgtx.digitex_rest_core.model.market import Market
from dgtx.digitex_rest_core.model.market_type import MarketType
from dgtx.digitex_rest_core.model.notification import Notification
from dgtx.digitex_rest_core.model.ohlcv import OHLCV
from dgtx.digitex_rest_core.model.ohlcv_list import OHLCVList
from dgtx.digitex_rest_core.model.order_duration import OrderDuration
from dgtx.digitex_rest_core.model.order_meta import OrderMeta
from dgtx.digitex_rest_core.model.order_position import OrderPosition
from dgtx.digitex_rest_core.model.order_side import OrderSide
from dgtx.digitex_rest_core.model.order_status import OrderStatus
from dgtx.digitex_rest_core.model.order_status_info import OrderStatusInfo
from dgtx.digitex_rest_core.model.order_type import OrderType
from dgtx.digitex_rest_core.model.paged_history_trades import PagedHistoryTrades
from dgtx.digitex_rest_core.model.paged_orders_response import PagedOrdersResponse
from dgtx.digitex_rest_core.model.ping import Ping
from dgtx.digitex_rest_core.model.place_order import PlaceOrder
from dgtx.digitex_rest_core.model.position_item import PositionItem
from dgtx.digitex_rest_core.model.rate_limits import RateLimits
from dgtx.digitex_rest_core.model.test import Test
from dgtx.digitex_rest_core.model.trade_history import TradeHistory
from dgtx.digitex_rest_core.model.update_order import UpdateOrder
