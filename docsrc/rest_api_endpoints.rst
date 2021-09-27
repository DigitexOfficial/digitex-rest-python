Rest API Endpoints
__________________

Public Endpoints
================

`Ping <public.html#dgtx.public.PublicApiClient.ping>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pings the Digitex server and returns server timestamp in nanoseconds.
Is used only to check whether server is alive.


.. code:: python

    ping = client.ping():

`Currencies <public.html#dgtx.public.PublicApiClient.get_currencies>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a list of currencies that the use can have a wallet at.

    `Link to API description <https://digitexofficial.github.io/rest-api-docs/#tag/Public/paths/~1v1~1exchange~1bot~1currency~1/get>`_

.. code:: python

    currencies = client.get_currencies(**kwargs):


`Markets <public.html#dgtx.public.PublicApiClient.get_markets>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns list of markets available to trade.

    `Link to API description <https://digitexofficial.github.io/rest-api-docs/#tag/Public/paths/~1v1~1exchange~1bot~1markets~1/get>`_

.. code:: python

    markets = client.get_markets(**kwargs):


`Exchange Information <public.html#dgtx.public.PublicApiClient.get_exchange_info>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns list of meta data of the exchange, such as list of currencies, list of markets
and list of order parameters (ENUMS for order types, duration, etc).

Using integer representation of order parameters is heavily used in our websocket api.
At one moment in the future we will fully synchronise these two api's, hence we use
same approach with order parameters as much as possible in this client. And yes, it would have been much easier to use string
representation of orders and market names, yet string representation of 'BUY' is bigger in size
then int 1.

    `Link to API description <https://digitexofficial.github.io/rest-api-docs/#tag/Exchange-Meta-Data/paths/~1v1~1exchange~1bot~1exchange_info~1/get>`_


.. code:: python

    exchange_info = get_exchange_info()



`Get Order Book <public.html#dgtx.public.PublicApiClient.get_order_book>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns order book of selected market

    `Link to API <https://digitexofficial.github.io/rest-api-docs/#tag/Public/paths/~1v1~1exchange~1bot~1order_book~1/get>`_

.. code:: python

    order_book = private.get_order_book(market_id=1):


`Get Recent Trades <public.html#dgtx.public.PublicApiClient.get_recent_trades>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get recent trades executed at the exchange for selected market

    `Link to API <https://digitexofficial.github.io/rest-api-docs/#tag/Public/paths/~1v1~1exchange~1bot~1recent_trades~1/get>`_



.. code:: python

    recent_trades = private.get_recent_trades(market_id=1, max_trades=5):

`Get K-Lines / OHLCV values <public.html#dgtx.public.PublicApiClient.get_k_lines>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns list of K-Lines / OHLCV values for selected market and selected resolution
with optional date filters

    `Link to API <https://digitexofficial.github.io/rest-api-docs/#tag/Public/paths/~1v1~1exchange~1bot~1history~1ohlcv~1/get>`_

.. code:: python

    ohlcv = client.get_k_lines(market_id=1, resolution='1D')


Private Endpoints
=================


`Get Account Balance <private.html#dgtx.private.PrivateApiClient.get_balance>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get trader's account balance. In addition to wallet balance, returns available balance per currency -
balance that is available for trading

    `Link to API <https://digitexofficial.github.io/rest-api-docs/#tag/Private/paths/~1v1~1exchange~1bot~1balances~1/get>`_

.. code:: python

    my_balance = client.get_balance()



`Get Position <private.html#dgtx.private.PrivateApiClient.get_position>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shows current position of the trader in the futures market.

    `Link to API <https://digitexofficial.github.io/rest-api-docs/#tag/Private/paths/~1v1~1exchange~1bot~1position~1/get>`_

.. code:: python

    position = client.get_position():



`Get Trade History <private.html#dgtx.private.PrivateApiClient.get_trade_history>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns paginated trade history

    `Link to API <https://digitexofficial.github.io/rest-api-docs/#tag/Private/paths/~1v1~1exchange~1bot~1trade_history~1/get>`_

.. code:: python

    trade_history = client.get_trade_history(**kwargs)


`Get Order History <private.html#dgtx.private.PrivateApiClient.get_order_history>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get trader's order history. Returns orders that are no longer in execution.
These are orders with statuses:

    - FILLED - numerical status 5. Order has been fully filled
    - CANCELLED - numerical status 4. Order has been cancelled by user. Note partially filled order can be cancelled as well
    - REJECTED - numerical status 3. Order has been rejected by matching engine.


    `Link to API <https://digitexofficial.github.io/rest-api-docs/#tag/Private/paths/~1v1~1exchange~1bot~1order_history~1/get>`_


.. code:: python

    order_history  = client.get_order_history(**kwargs)



`Get Open Orders <private.html#dgtx.private.PrivateApiClient.get_orders>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get trader's open orders. Returns orders that are currently in execution.

These are order with order_status:

    - PENDING - numerical status 1 - the order has been recieved, however not yet accepted by the exchange matching engine
    - ACCEPTED - numerical status 2 - the order has been recieved, validated and accepted by the exchange matching engine
    - PARTIAL - numerical status 6 - ACCEPTED + partially filled. Partial filled information and remaining volume are part of the open order information

    `Link to API <https://digitexofficial.github.io/rest-api-docs/#tag/Private/paths/~1v1~1exchange~1bot~1orders~1/get>`_
.. code:: python

    orders = client.get_orders(**kwargs)



`Get Order Status <private.html#dgtx.private.PrivateApiClient.get_order_status>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get single order status

    `Link to API <https://digitexofficial.github.io/rest-api-docs/#tag/Private/paths/~1v1~1exchange~1bot~1orders~1/get>`_


.. code:: python

    order_status = client.get_order_status(order_id='d3c32cc8-89b7-4a4a-8847-7a255e7739ad)



`Place an order <private.html#dgtx.private.PrivateApiClient.place_order>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    `Link to API <https://digitexofficial.github.io/rest-api-docs/#tag/Private/paths/~1v1~1exchange~1bot~1trader~1order~1/post>`_

Create and place a new order. This requires importing some additional classes:

.. code:: python

    from dgtx.digitex_rest_core.model.order_duration import OrderDuration
    from dgtx.digitex_rest_core.model.order_side import OrderSide
    from dgtx.digitex_rest_core.model.order_type import OrderType
    from dgtx.extra_data_classes import PlaceOrderMeta

    new_order = PlaceOrderMeta(
        market_id=1, # BTCUSDS Futures
        side=OrderSide(1), # see order_meta for description
        duration=OrderDuration(2), # see order_meta for description
        leverage=10, # desired leverage
        type=OrderType(2), # see order_meta for description
        quantity=Decimal(9),
        price=Decimal(38000)
    )

    placed_order = client.place_order(new_order)

"placed_order" is just confirmation of your order params, not the confirmation
that the order has been accepted or executed. You can then query order status by calling.

.. code:: python

    my_order_status = client.get_order_status(client_id=placed_order.client_id)


`Cancel order <private.html#dgtx.private.PrivateApiClient.cancel_order>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cancel order an existing order or orders list or cancel by market_id.
This requires additional import of CancelOrder data model.

    `Link to API <https://digitexofficial.github.io/rest-api-docs/#tag/Private/paths/~1v1~1exchange~1bot~1trader~1order~1cancel~1/post>`_


.. code:: python

    from dgtx.client import Client
    from dgtx.digitex_rest_core.model.cancel_order import CancelOrder

    # get order to cancel, e.g. all
    orders = client.get_orders()

    orders_to_cancel = CancelOrder(
        market_id=1,  # unique order id is insured only per market level
        orders_client_ids=[i.client_id for i in orders.results]  # list of orders to cancel
    )

    cancelled_orders = client.cancel_order(orders_to_cancel)

Status of the orders can then be queried with:


.. code:: python

    for order_id in cancelled_orders.orders_client_ids:
        my_cancelled_order = client.get_order_status(client_id=order_id)
        print(my_cancelled_order)