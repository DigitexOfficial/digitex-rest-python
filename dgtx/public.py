from typing import List, Union

from dgtx.digitex_rest_core.model.exchange_recent_trade_list import ExchangeRecentTradeList
from dgtx.digitex_rest_core.model.ohlcv_list import OHLCVList
from dgtx.metaclasses import ClientMeta

from dgtx.digitex_rest_core.rest import ApiException
from dgtx.digitex_rest_core.api.public_api import PublicApi
from dgtx.digitex_rest_core.model.ping import Ping
# from dgtx.digitex_rest_core.model.exchange_recent_trade import ExchangeRecentTrade
from dgtx.digitex_rest_core.model.ohlcv import OHLCV
from dgtx.digitex_rest_core.model.exchange_order_book import ExchangeOrderBook
from dgtx.digitex_rest_core.model.exchange_info import ExchangeInfo
from dgtx.digitex_rest_core.model.market import Market
from dgtx.digitex_rest_core.model.currency import Currency


class PublicApiClient(metaclass=ClientMeta):
    """
    Collection of methods that returns public information from the exchange
    """

    def __make(self, func, *args, **kwargs):
        with self.client as client:
            instance = PublicApi(client)
            try:
                return getattr(instance, func)(*args, **kwargs)
            except ApiException as e:
                return e

    def ping(self) -> Union[Ping, ApiException]:
        """
        Check if server is responding,
        also returns server time in milliseconds

        :return: a data model of ping response. methods can be accessed with dot-notation.


            .. code-block:: python

                {"message": "pong",
                "timestamp": 1632567734971007}


        """
        func = "v1_exchange_bot_ping_get"
        return self.__make(func)

    def get_currencies(self, *args, **kwargs) -> Union[List[Currency], ApiException]:
        """
        Returns a list of walletable currencies with some extra params

        Each currency instance is a model with the following parameters:

        - id - internal currency id

        - name - currency name

        - code - short currency code

        - currency_scale - amount of digits

        - withdraw_fee - amount in currency you pay if you want to use digitex withdrawal service


        :param currency_id: [int] - optional currency id, returns only this currency instance

        :return: List of currencies data models


        .. code-block:: python

            [
                {"code": "DGTX",
                "currency_scale": 4,
                "id": 1,
                "name": "Digitex",
                "withdraw_fee": Decimal("100.000000000000000000")},

                {"code": "BTC",
                "currency_scale": 8,
                "id": 2,
                "name": "Bitcoin",
                "withdraw_fee": Decimal("0.000050000000000000")}
             ]


        """

        func = "v1_exchange_bot_currency_get"

        return self.__make(func, *args, **kwargs)

    def get_order_book(self, market_id, **kwargs) -> ExchangeOrderBook:
        """
        Get current order book of selected market

        :param market_id: id of a market

        :return: class ExchangeOrderBook, asks/bids can be accessed with dot-notation

        .. code-block:: python

            {"asks": [[Decimal("2913"), Decimal("449")],
                      [Decimal("2914"), Decimal("3430")],
                      [Decimal("2915"), Decimal("2525")],
                      [Decimal("2916"), Decimal("2738")],
                      [Decimal("2928"), Decimal("3039")]],
            "bids": [[Decimal("2910"), Decimal("4570")],
                      [Decimal("2909"), Decimal("2050")],
                      [Decimal("2079"), Decimal("8")],
                      [Decimal("2076"), Decimal("1000")],
                      [Decimal("1070"), Decimal("10")]],
             "market_id": 2,
             "timestamp": 1632571422798363}

        """
        func = "v1_exchange_bot_order_book_get"
        return self.__make(func, market_id, **kwargs)

    def get_recent_trades(self, market_id, **kwargs) -> ExchangeRecentTradeList:
        """
        Get the list of recent trades at the exhchange for selected markets

        :param market_id: int - market id
        :param max_trades: int - optional parameter to limit output to last max_trades


        :return: class ExchangeRecentTradeList

        .. code-block:: python

            {"market_id": 23,
             "recent_trades": [{"base_volume": Decimal("9364"),
                                "price": Decimal("4E-8"),
                                "quote_volume": Decimal("0.00037456"),
                                "side": 2,
                                "timestamp": 1632590930368437,
                                "trade_id": 169471322},
                               {"base_volume": Decimal("3518"),
                                "price": Decimal("7E-8"),
                                "quote_volume": Decimal("0.00024626"),
                                "side": 1,
                                "timestamp": 1632590961604440,
                                "trade_id": 169471696}],
             "timestamp": 1632640603867893}

        """

        func = "v1_exchange_bot_recent_trades_get"
        return self.__make(func, market_id, **kwargs)


    def get_k_lines(self, market_id, resolution, **kwargs) -> OHLCV:
        """
        Get list of ohlcv values for selected market and timeframe/resolutions

        :param int, required market_id:  Filtering by number market id. To get market id use "Get list of currently active Markets on exchange" endpoint.

        :param str, required resolution: Symbol resolution. Possible resolutions are daily (D or 1D, 2D ... ), weekly (1W, 2W ...), monthly (1M, 2M...) and an intra-day resolution – minutes(1, 2 ...)

        :param int, optional, utc, milliseconds date_from:  Unix timestamp (UTC) of the leftmost required bar, including from.

        :param int, optional utc, milliseconds date_to: Unix timestamp (UTC) of the rightmost required bar, including to. It can be in the future. In this case, the rightmost required bar is the latest available bar.

        :param int, optional top_n: Number which limits the maximum number of answers. (default = 1000)


        :return:
        .. code-block:: json


            [
                {
                    "timestamp": 1617284280000000,
                    "open": "59020.000000000000000000",
                    "high": "59045.000000000000000000",
                    "low": "58980.000000000000000000",
                    "close": "58990.000000000000000000",
                    "volume": "2129.000000000000000000"
                },
                {
                    "timestamp": 1617284340000000,
                    "open": "58995.000000000000000000",
                    "high": "59030.000000000000000000",
                    "low": "58985.000000000000000000",
                    "close": "58990.000000000000000000",
                    "volume": "315.000000000000000000"
                }
            ]

        """

        func = "v1_exchange_bot_history_ohlcv_get"
        return self.__make(func, market_id=market_id, resolution=resolution, **kwargs)


    def get_exchange_info(self) -> Union[ExchangeInfo, ApiException]:
        """
        Returns list of available currencies, markets and order meta data.

        :return: Exchange Info Meta Data

        .. code-block:: python

            {
            "currencies": # list of currencies, same as get currencies
                [
                    {"code": "DGTX",
                    "currency_scale": 4,
                    "id": 1,
                    "name": "Digitex",
                    "withdraw_fee": Decimal("100.000000000000000000")},
                ...],
            "markets": # list of markets, same as get markets
                [
                    {"base_currency": {"code": "BTC",
                                    "currency_scale": 8,
                                    "id": 2,
                                    "name": "Bitcoin",
                                    "withdraw_fee": Decimal("0.000050000000000000")},
                    "code": "S:BTCUSDC",
                    "contract_currency": None,
                    "description": "BTC/USDC spot",
                    "funding": "0E-18",
                    "id": 18,
                    "market_type": 2,
                    "name": "BTC/USDC",
                    "quote_currency": {"code": "USDC",
                                     "currency_scale": 4,
                                     "id": 7,
                                     "name": "USD Coin",
                                     "withdraw_fee": Decimal("100.000000000000000000")}},
                    {"base_currency": {"code": "BTC",
                                "currency_scale": 8,
                                "id": 2,
                                "name": "Bitcoin",
                                "withdraw_fee": Decimal("0.000050000000000000")},
                    "code": "FS:BTCUSD",
                     "contract_currency": {"code": "USDC",
                                    "currency_scale": 4,
                                    "id": 7,
                                    "name": "USD Coin",
                                    "withdraw_fee": Decimal("100.000000000000000000")},
                      "description": "BTC/USD future nominated in USDC",
                      "funding": Decimal("0.000300000000000000"),
                      "id": 14,
                      "market_type": 1,
                      "name": "BTC/USD USDC",
                      "quote_currency": {"code": "USD",
                                         "currency_scale": 2,
                                         "id": 3,
                                         "name": "USD",
                                         "withdraw_fee": Decimal("100.000000000000000000")}},
                    ...]

            "notifications": [], // list of exchange announcements

            "order_meta": # order meta data
                {"duration": {"DURATION_UNDEFINED": 0,
                                         "FOK": 5,
                                         "GFD": 1,
                                         "GTC": 2,
                                         "GTF": 3,
                                         "IOC": 4},
                "position": {"LONG": 1, "SHORT": 2, "UNDEFINED": 0},
                "side": {"BUY": 1, "SELL": 2},
                "status": {"ACCEPTED": 2,
                           "CANCELED": 4,
                           "FILLED": 5,
                           "PARTIAL": 6,
                           "PENDING": 1,
                           "REJECTED": 3},
                "type": {"LIMIT": 1, "MARKET": 2}},
            "rate_limits": # not implemented at the moment, but will be soon
                            [{"interval": "SECOND", "limit": 50},
                             {"interval": "MINUTE", "limit": 500}],
             "server_time": 1632607288438219}


        """
        func = "v1_exchange_bot_exchange_info_get"
        return self.__make(func)

    def get_markets(self, **kwargs) -> List[Market]:
        """
        Get markets available to trade

        :param market_id: [int] - optional market id, returns just this market

        :return: List of markets data class

        .. code-block:: python

            [
                {
                    "base_currency": {"code": "BTC",
                                       "currency_scale": 8,
                                       "id": 2,
                                       "name": "Bitcoin",
                                       "withdraw_fee": Decimal("0.000050000000000000")},
                     "code": "S:BTCUSDC",
                     "contract_currency": None,
                     "description": "BTC/USDC spot",
                     "funding": Decimal("0E-18"),
                     "id": 18,
                     "market_type": 2,
                     "name": "BTC/USDC",
                     "quote_currency": {"code": "USDC",
                                        "currency_scale": 4,
                                        "id": 7,
                                        "name": "USD Coin",
                                        "withdraw_fee": Decimal("100.000000000000000000")},
                    "tick_size": "5.000000000000000000",
                    "tick_price": "0.100000000000000000",
                    "tick_scale": 0


                }
            ]


        """

        func = "v1_exchange_bot_markets_get"
        return self.__make(func, **kwargs)

