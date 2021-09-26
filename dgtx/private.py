from dgtx.digitex_rest_core.model.order_status_info import OrderStatusInfo
from dgtx.digitex_rest_core.model.paged_orders_response import PagedOrdersResponse
from dgtx.digitex_rest_core.model.paged_history_trades import PagedHistoryTrades
from dgtx.digitex_rest_core.model.position_item import PositionItem
from dgtx.digitex_rest_core.model.cancel_order import CancelOrder
from dgtx.digitex_rest_core.model.update_order import UpdateOrder
from dgtx.digitex_rest_core.model.place_order import PlaceOrder
from dgtx.digitex_rest_core.model.order_type import OrderType
from dgtx.digitex_rest_core.model.balance import Balance

from dgtx.digitex_rest_core.api.private_api import PrivateApi
from dgtx.extra_data_classes import PlaceOrderMeta, UpdateOrderMeta
from dgtx.metaclasses import ClientMeta
from dgtx.digitex_rest_core.rest import ApiException
from decimal import Decimal
from typing import List


class PrivateApiClient(metaclass=ClientMeta):
    """
    Trading privat client of Digitex
    """

    def __make(self, func, *args, **kwargs):
        with self.client as client:
            instance = PrivateApi(client)
            try:
                return getattr(instance, func)(*args, **kwargs)
            except ApiException as e:
                return e

    def get_order_status(self, client_id) -> List[OrderStatusInfo]:
        """
        Get single order status.
        The exchange only guarantees unique order id per market.

        :param str, required client_id: Id of a an order UUID.
            **Examples**: "d3c32cc8-89b7-4a4a-8847-7a255e7739ad"

        :return: List[OrderStatusInfo]

        .. code-block:: json

            [
                {'average_price': Decimal('0'),
                 'client_id': 'ec825f37-1af8-46ae-89d5-d2b0ffbdaf3f',
                 'created_at': 1632500527901353,
                 'duration': 1,
                 'executed_quantity': None,
                 'market_id': 1,
                 'orig_quantity': Decimal('12.000000000000000000'),
                 'price': Decimal('48000.000000000000000000'),
                 'quantity': Decimal('12.000000000000000000'),
                 'reduce_only': None,
                 'side': 2,
                 'status': 2,
                 'stop_loss_price': None,
                 'type': 2}
             ]

        """

        func = 'v1_exchange_bot_order_status_get'
        return self.__make(func, client_id)

    def get_orders(self, **kwargs) -> PagedOrdersResponse:
        """
        Get all orders info, with extra params.
        Show only orders in status: ACCEPTED, FILLED, PARTIAL

        :param int, optional type: Filtering by order type.

        :param int, optional status: Filtering by order status.

        :param int, optional side: Filtering by order side.

        :param int, optional market_id: Filtering by market id.

        :param int, optional page_size: Number of items on a page.

        :param str, optional cursor: Query for listing pages.


        :return:
        .. code-block:: json

            {'next': None,
            'previous': None,
            'results': [{'average_price': Decimal('0'),
                      'client_id': 'ec825f37-1af8-46ae-89d5-d2b0ffbdaf3f',
                      'created_at': 1632500527901353,
                      'duration': 1,
                      'executed_quantity': None,
                      'market_id': 1,
                      'orig_quantity': Decimal('12.000000000000000000'),
                      'price': Decimal('48000.000000000000000000'),
                      'quantity': Decimal('12.000000000000000000'),
                      'reduce_only': None,
                      'side': 2,
                      'status': 2,
                      'stop_loss_price': None,
                      'type': 2},

                     {'average_price': Decimal('0'),
                      'client_id': 'e164d630-de6e-4549-bde1-123f06d663ab',
                      'created_at': 1632397829564555,
                      'duration': 1,
                      'executed_quantity': None,
                      'market_id': 1,
                      'orig_quantity': Decimal('7.000000000000000000'),
                      'price': Decimal('35000.000000000000000000'),
                      'quantity': Decimal('7.000000000000000000'),
                      'reduce_only': None,
                      'side': 1,
                      'status': 2,
                      'stop_loss_price': None,
                      'type': 2}]
              }


        """
        func = 'v1_exchange_bot_orders_get'
        return self.__make(func, **kwargs)

    def get_trade_history(self, **kwargs) -> PagedHistoryTrades:
        """
        Get trade history.

        :param int, optional traded_at_from: timestamp in nanoseconds. Return only trades from this ts

        :param int, optional traded_at_to: timestamp in nanoseconds. Return only trades prior to this ts

        :param int, optional market_id:  market id. Return only trades for this market

        :param int, optional page_size: Number of items on a page.

        :param str, optional cursor: return trades from this page (response.next, response.previous)

        :return: PagedHistoryTrades

        .. code-block:: python

            {'next': 'bz0xJnA9MjAyMS0wOS0yNiswOCUzQTM2JTNBNTguNTgzODM3JTJCMDAlM0EwMA==',
            'previous': None,
             'results': [{'contract_id': 170147649,
                          'market_id': 1,
                          'price': Decimal('41360.000000000000000000'),
                          'quantity': Decimal('3.000000000000000000'),
                          'side': 2,
                          'traded_at': 1632645707694451},
                         {'contract_id': 170144115,
                          'market_id': 1,
                          'price': Decimal('41310.000000000000000000'),
                          'quantity': Decimal('1.000000000000000000'),
                          'side': 2,
                          'traded_at': 1632645418583837},
                         {'contract_id': 169264015,
                          'market_id': 1,
                          'price': Decimal('42420.000000000000000000'),
                          'quantity': Decimal('9.000000000000000000'),
                          'side': 2,
                          'traded_at': 1632575224882760}]
              }

        """
        func = 'v1_exchange_bot_trade_history_get'
        return self.__make(func, **kwargs)

    def get_order_history(self, **kwargs) -> PagedOrdersResponse:

        """
        Get trader's order history. Returns orders that are no longer in execution.
        These are orders with statuses; FILLED, CANCELED or REJECTED

        :param str, optional created_at_from: timestamp in nanoseconds. Returns order created after this ts

        :param str, optional created_at_to: timestamp in nanoseconds. Returns order created before this ts

        :param int, optional market_id: Return orders only for this market id

        :param int, optional page_size: Number of items on a page.

        :param str, optional cursor:  return trades from this page (response.next, response.previous)

        :param int, optional status: return only orders with this status id


        :return: PagedOrdersResponse


        .. code-block:: python

            {'next': 'cD0yMDIxLTA5LTI2KzA4JTNBMzYlM0E1OC41ODM4MzclMkIwMCUzQTAw',
            'previous': None,
            'results': [{'average_price': Decimal('0'),
                          'client_id': '6ab2f191-c341-42c2-b31f-e0b9a06c234d',
                          'created_at': 1632645707702350,
                          'duration': 4,
                          'executed_quantity': None,
                          'market_id': 1,
                          'orig_quantity': Decimal('3.000000000000000000'),
                          'price': Decimal('0E-18'),
                          'quantity': Decimal('0E-18'),
                          'reduce_only': False,
                          'side': 2,
                          'status': 5,
                          'stop_loss_price': None,
                          'type': 1},

                         {'average_price': Decimal('0'),
                          'client_id': '2e5abae0-15d2-4128-9451-430cbe6c2afa',
                          'created_at': 1632645418590972,
                          'duration': 4,
                          'executed_quantity': None,
                          'market_id': 1,
                          'orig_quantity': Decimal('1.000000000000000000'),
                          'price': Decimal('0E-18'),
                          'quantity': Decimal('0E-18'),
                          'reduce_only': False,
                          'side': 2,
                          'status': 5,
                          'stop_loss_price': None,
                          'type': 1}]
              }


        """
        func = 'v1_exchange_bot_order_history_get'
        return self.__make(func, **kwargs)

    def get_balance(self) -> List[Balance]:
        """
        Returns user balances. for unrealized p&l see get position

        :return: List of balances per currency

        .. code-block:: python

            [{'available_balance': Decimal('0'),
             'currency': {'code': 'BXR',
                          'currency_scale': 4,
                          'id': 32,
                          'name': 'Blockster',
                          'withdraw_fee': Decimal('0E-18')},
             'main_balance': Decimal('0'),
             'total_balance': Decimal('0'),
             'trading_balance': Decimal('0')},

             {'available_balance': Decimal('0.000499750000000000'),
             'currency': {'code': 'BTC',
                          'currency_scale': 8,
                          'id': 2,
                          'name': 'Bitcoin',
                          'withdraw_fee': Decimal('0.000050000000000000')},
             'main_balance': Decimal('0'),
             'total_balance': Decimal('0.000499750000000000'),
             'trading_balance': Decimal('0.000499750000000000')},

             {'available_balance': Decimal('65772.610500000000000000'),
             'currency': {'code': 'DGTX',
                          'currency_scale': 4,
                          'id': 1,
                          'name': 'Digitex',
                          'withdraw_fee': Decimal('100.000000000000000000')},
             'main_balance': Decimal('0'),
             'total_balance': Decimal('65772.610500000000000000'),
             'trading_balance': Decimal('65772.610500000000000000')},

             {'available_balance': Decimal('0.014990700000000000'),
             'currency': {'code': 'ETH',
                          'currency_scale': 8,
                          'id': 4,
                          'name': 'Ethereum',
                          'withdraw_fee': Decimal('100.000000000000000000')},
             'main_balance': Decimal('0'),
             'total_balance': Decimal('0.014990700000000000'),
             'trading_balance': Decimal('0.014990700000000000')},

             {'available_balance': Decimal('1.553271480000000000'),
             'currency': {'code': 'USDC',
                          'currency_scale': 4,
                          'id': 7,
                          'name': 'USD Coin',
                          'withdraw_fee': Decimal('100.000000000000000000')},
             'main_balance': Decimal('0'),
             'total_balance': Decimal('1.553271480000000000'),
             'trading_balance': Decimal('1.553271480000000000')},

             {'available_balance': Decimal('0'),
             'currency': {'code': 'USDT',
                          'currency_scale': 4,
                          'id': 6,
                          'name': 'USDT',
                          'withdraw_fee': Decimal('100.000000000000000000')},
             'main_balance': Decimal('0'),
             'total_balance': Decimal('0'),
             'trading_balance': Decimal('0')}
             ]

        """
        func = 'v1_exchange_bot_balances_get'
        return self.__make(func)

    def get_position(self) -> List[PositionItem]:
        """
        Shows current position of the trader in the futures market.

        :return: List[PositionItem]

        .. code-block:: python

            [
            {'contract_currency_id': 1,
             'entry_price': Decimal('41347.500000000000000000'),
             'leverage': Decimal('9.0'),
             'liquidation_price': Decimal('43642.500000000000000000'),
             'mark_price': Decimal('41375.308400000000000000'),
             'market_id': 1,
             'position_margin': Decimal('367.533600000000000000'),
             'position_side': 2,
             'quantity': Decimal('4.000000000000000000'),
             'timestamp': 1632645712797059,
             'unrealized_pnl': Decimal('-4.200000000000000000000000000')},

             {'contract_currency_id': 1,
             'entry_price': None,
             'leverage': None,
             'liquidation_price': None,
             'mark_price': Decimal('2765.148000000000000000'),
             'market_id': 2,
             'position_margin': Decimal('0E-18'),
             'position_side': None,
             'quantity': Decimal('0E-18'),
             'timestamp': 1632645314273798,
             'unrealized_pnl': None},

        """

        func = 'v1_exchange_bot_position_get'
        return self.__make(func)

    def place_order(self, order: PlaceOrderMeta) -> PlaceOrder:

        """

        :param order: PlaceOrderMeta instance

        :return: PlaceOrder instance

        .. code-block:: python

                {'client_id': '0344b6d7-9fc1-419e-b4aa-cff0b9bd82d5',
                 'duration': 2,
                 'leverage': 10,
                 'market_id': 1,
                 'price': Decimal('38000.000000000000000000'),
                 'quantity': Decimal('9.000000000000000000'),
                 'side': 1,
                 'trader_id': 119887,
                 'type': 2}

        """
        func = 'v1_exchange_bot_trader_order_post'
        return self.__make(func, order.to_post())

    def cancel_order(self, orders: CancelOrder) -> CancelOrder:
        """
        :param orders: CancelOrder class instance

        to cancel an order(s) - send market_id and list of client_id(s)

        to cancel order(s) by market - send only market_id

        to cancel all orders for the account - send empty body

        :return: CancelOrder class instance


        .. code-block:: python

            {'market_id': 1,
             'orders_client_ids': ['0344b6d7-9fc1-419e-b4aa-cff0b9bd82d5',
                                   'ec825f37-1af8-46ae-89d5-d2b0ffbdaf3f',
                                   'e164d630-de6e-4549-bde1-123f06d663ab'],
             'trader_id': 119887}

        """
        func = 'v1_exchange_bot_trader_order_cancel_post'
        return self.__make(func, orders)

    def update_order(self, order: UpdateOrderMeta) -> UpdateOrder:
        """
                If at the time of the order change it is executed or becomes inactive for any of the reasons, then you will open a new order with the parameters that you passed

                :param order:
                :type order:
                :param str(UUID-4), required client_id: client id, can be found in orders instance

                :param int, required market_id: market id, can be found in markets instance

                :param int, required side: BUY = 1 SELL = 2

                :param int, required type: MARKET = 1 LIMIT = 2

                :param int, required duration: Duration of the order GFD = 1 GTC = 2 GTF = 3 IOC = 4 FOK = 5

                :param int, required leverage: Leverage of the trades, only valid for futures market and will be ignored for spot

                :param decimal, required quantity: Quantity of the order. If you are trading futures, this is - amount of contracts. for spot - it depends on your side.

                :param decimal, required price: Price of the orders

                :return
                .. code-block:: json

                {
                    "client_id": "6a7bc84b-746a-405a-8688-85502b275b7d",
                    "duration": 2,
                    "leverage": 1,
                    "market_id": 1,
                    "price": "46000.000000000000000000",
                    "quantity": "1.000000000000000000",
                    "side": 1,
                    "trader_id": 119511,
                    "type": 2
                }
                """

        func = 'v1_exchange_bot_trader_order_update_post'
        return self.__make(func, order.to_post())
