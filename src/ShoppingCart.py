import decimal

import attr


@attr.define
class Product:
    name: str = attr.ib(validator=attr.validators.instance_of(str))
    cost: float = attr.ib(validator=attr.validators.instance_of(float))
    quantity: int = attr.ib(validator=attr.validators.instance_of(int))
    tax_rate: float = attr.ib(validator=attr.validators.instance_of(float))
    revenue_rate: float = attr.ib(validator=attr.validators.instance_of(float))


class Discount:
    pass


@attr.define
class ShoppingCartList:
    products: list[Product] = attr.ib(validator=attr.validators.instance_of(list), factory=list)
    total_cost: float = attr.ib(validator=attr.validators.instance_of(float), default=0.0)
    total_products: int = attr.ib(validator=attr.validators.instance_of(int), default=0)


class ShoppingCart:
    def __init__(self, shopping_cart_list: ShoppingCartList):
        self.__shopping_cart_list = shopping_cart_list

    def add_item(self, item: Product):
        self.__shopping_cart_list.products.append(item)
        self.__shopping_cart_list.total_products += item.quantity
        self.__calculate_total_cost_in_shopping_cart(item)

    def __calculate_total_cost_in_shopping_cart(self, item):
        total_cost = decimal.Decimal(item.cost * item.quantity * (1 + item.revenue_rate)).quantize(
            decimal.Decimal('0.00'),
            rounding=decimal.ROUND_UP)
        total_cost = decimal.Decimal(float(total_cost) * (1 + item.tax_rate)).quantize(decimal.Decimal('0.00'),
                                                                                       rounding=decimal.ROUND_UP)
        self.__shopping_cart_list.total_cost += float(total_cost)

    def delete_item(self, item: Product):
        pass

    def apply_discount(self, discount: Discount):
        pass

    def get_shopping_cart(self) -> ShoppingCartList:
        return self.__shopping_cart_list
