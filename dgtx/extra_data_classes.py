from decimal import Decimal

from dgtx.digitex_rest_core.model.order_duration import OrderDuration
from dgtx.digitex_rest_core.model.order_side import OrderSide
from dgtx.digitex_rest_core.model.order_type import OrderType
from dgtx.digitex_rest_core.model.place_order import PlaceOrder
from dgtx.digitex_rest_core.model.update_order import UpdateOrder


class PlaceOrderMeta:
    """
    Helper class to show typehint and manage data transformation of placing an order
    """
    def __init__(self,
                 market_id: int,
                 side: OrderSide,
                 duration: OrderDuration,
                 leverage: int,
                 type: OrderType,
                 quantity: Decimal,
                 price: Decimal
                 ):
        self.market_id = market_id
        self.side = side
        self.duration = duration
        self.leverage = leverage
        self.type = type
        self.quantity = quantity
        self.price = price

    def to_post(self):
        return PlaceOrder(
            market_id=self.market_id,
            side=self.side,
            duration=self.duration,
            leverage=self.leverage,
            type=self.type,
            quantity=str(self.quantity),
            price=str(self.price)
        )


class UpdateOrderMeta:
    """
    Helper class to show typehints and manage data transformation of updating an order
    """
    def __init__(self,
                 cliend_id: str,
                 market_id: int,
                 side: OrderSide,
                 duration: OrderDuration,
                 leverage: int,
                 type: OrderType,
                 quantity: Decimal,
                 price: Decimal,
                 ):
        self.client_id = cliend_id
        self.market_id = market_id
        self.side = side
        self.duration = duration
        self.leverage = leverage
        self.type = type
        self.quantity = quantity
        self.price = price

    def to_post(self):
        return UpdateOrder(
            client_id=self.client_id,
            market_id=self.market_id,
            side=self.side,
            duration=self.duration,
            leverage=self.leverage,
            type=self.type,
            quantity=str(self.quantity),
            price=str(self.price)
        )

