Helper Classes
=================

`PlaceOrderMeta`
^^^^^^^^^^^^^^^^

Helper class to create an order. Is used when calling client.place_order

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

`CancelOrder`
^^^^^^^^^^^^^^

Helper class to create cancel order message. Is used with client.cancel_order method

.. code:: python

    from dgtx.digitex_rest_core.model.cancel_order import CancelOrder

    orders_to_cancel = CancelOrder(
        market_id=1,  # unique order id is insured only per market level
        orders_client_ids=['ec825f37-1af8-46ae-89d5-d2b0ffbdaf3f']  # list of orders to cancel
    )

`OrderSide`
^^^^^^^^^^^^^^

Helper class to indicate OrderSide. Accepts ints as input.
Possible values can be found at `client.get_exchange_info().order_meta <http://localhost:63342/digitex-rest-python/docs/build/public.html#dgtx.public.PublicApiClient.get_exchange_info>`_


Current value list:

.. code:: python

        {'side':
                {'BUY': 1,
                'SELL': 2}
        }


Example usage:

.. code:: python

    from dgtx.digitex_rest_core.model.order_side import OrderSide

    order_side = OrderSide(1)


`OrderDuration`
^^^^^^^^^^^^^^^^

Helper class to indicate Order Duration. Accepts ints as input.
Possible values can be found at `client.get_exchange_info().order_meta <http://localhost:63342/digitex-rest-python/docs/build/public.html#dgtx.public.PublicApiClient.get_exchange_info>`_


.. code:: python

        {'duration': {'DURATION_UNDEFINED': 0,
                                     'FOK': 5,
                                     'GFD': 1,
                                     'GTC': 2,
                                     'GTF': 3,
                                     'IOC': 4}
        }


Example usage:


.. code:: python

    from dgtx.digitex_rest_core.model.order_duration import OrderDuration

    order_duration = OrderDuration(1)

`OrderType`
^^^^^^^^^^^^^^

Helper class to indicate Order Type. Accepts ints as input.
Possible values can be found at `client.get_exchange_info().order_meta <http://localhost:63342/digitex-rest-python/docs/build/public.html#dgtx.public.PublicApiClient.get_exchange_info>`_

Current value list:

.. code:: python

        {'type':
                {'LIMIT': 1,
                'MARKET': 2}
        }


Example usage:

.. code:: python

    from dgtx.digitex_rest_core.model.order_type import OrderType

    order_type = OrderType(2)


`OrderStatus`
^^^^^^^^^^^^^^

Helper class to indicate Order Status. Accepts ints as input.
Possible values can be found at `client.get_exchange_info().order_meta <http://localhost:63342/digitex-rest-python/docs/build/public.html#dgtx.public.PublicApiClient.get_exchange_info>`_

Current value list:

.. code:: python

        {'status': {'ACCEPTED': 2,
                   'CANCELED': 4,
                   'FILLED': 5,
                   'PARTIAL': 6,
                   'PENDING': 1,
                   'REJECTED': 3}
            }


Example usage:

.. code:: python

    from dgtx.digitex_rest_core.model.order_type import OrderStatus

    order_type = OrderStatus(2)

