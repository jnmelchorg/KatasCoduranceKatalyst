from __future__ import annotations

import decimal
import attr


@attr.define
class Product:
    name: str = attr.ib(validator=attr.validators.instance_of(str))
    cost: float = attr.ib(validator=attr.validators.instance_of(float))
    quantity: int = attr.ib(validator=attr.validators.instance_of(int))
    tax_rate: float = attr.ib(validator=attr.validators.instance_of(float))
    revenue_rate: float = attr.ib(validator=attr.validators.instance_of(float))
    cost_per_unit_with_revenue: float = attr.ib(validator=attr.validators.instance_of(float), default=-1.0)
    cost_per_unit_after_tax: float = attr.ib(validator=attr.validators.instance_of(float), default=-1.0)

    def calculate_total_cost(self) -> float:
        self.__calculate_cost_per_unit_with_revenue_per_unit()
        self.__calculate_cost_per_unit_after_tax_per_unit()
        return self.cost_per_unit_after_tax * self.quantity

    def __calculate_cost_per_unit_after_tax_per_unit(self):
        cost_per_unit_after_tax = \
            decimal.Decimal(self.cost_per_unit_with_revenue * (1 + self.tax_rate)).quantize(decimal.Decimal('0.00'),
                                                                                            rounding=decimal.ROUND_UP)
        self.cost_per_unit_after_tax = float(cost_per_unit_after_tax)
        return None

    def __calculate_cost_per_unit_with_revenue_per_unit(self):
        cost_per_unit_with_revenue = decimal.Decimal(self.cost * (1 + self.revenue_rate)).quantize(
            decimal.Decimal('0.00'),
            rounding=decimal.ROUND_UP)
        self.cost_per_unit_with_revenue = float(cost_per_unit_with_revenue)
        return None

    def check_if_product_is_the_same(self, product: Product) -> bool:
        if self.name == product.name and self.cost == product.cost and self.tax_rate == product.tax_rate and \
                self.revenue_rate == product.revenue_rate:
            return True
        return False


class Discount():
    def __init__(self):
        self.__codes = {
            'PROMO_5': 5,
            'PROMO_10': 10
        }
    
    def get_discount(self, code: str) -> float:
        if code not in self.__codes:
            raise ValueError(f'Code {code} is not valid')
        return self.__codes[code]


@attr.define
class ShoppingCartList:
    products: list[Product] = attr.ib(validator=attr.validators.instance_of(list), factory=list)
    total_cost: float = attr.ib(validator=attr.validators.instance_of(float), default=0.0)
    total_products: int = attr.ib(validator=attr.validators.instance_of(int), default=0)


class ShoppingCart:
    def __init__(self):
        self.__shopping_cart_list = ShoppingCartList()

    def add_item(self, item: Product):
        self.__update_shopping_cart_list(item)
        self.__shopping_cart_list.total_products += item.quantity
        self.__shopping_cart_list.total_cost += item.calculate_total_cost()

    def delete_item(self, item: Product):
        for product in self.__shopping_cart_list.products:
            if product.check_if_product_is_the_same(item):
                self.__shopping_cart_list.total_products -= item.quantity
                self.__shopping_cart_list.total_cost -= item.calculate_total_cost()
                self.__shopping_cart_list.products.remove(product)

    def apply_discount(self, discount: str):
        discount = Discount().get_discount(discount)
        self.__shopping_cart_list.total_cost = \
            float(decimal.Decimal(self.__shopping_cart_list.total_cost * (1 - discount / 100)).quantize(
                decimal.Decimal('0.00'), rounding=decimal.ROUND_UP))

    def get_shopping_cart(self) -> ShoppingCartList:
        return self.__shopping_cart_list

    def __update_shopping_cart_list(self, item: Product):
        for product in self.__shopping_cart_list.products:
            if product.check_if_product_is_the_same(item):
                product.quantity += item.quantity
                return None
        self.__shopping_cart_list.products.append(item)
