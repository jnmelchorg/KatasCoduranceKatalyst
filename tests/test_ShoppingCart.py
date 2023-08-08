import copy

from src.ShoppingCart import ShoppingCart, Product, ShoppingCartList

def get_iceberg_lettuce():
        return Product(name="Iceberg Lettuce",
                                  cost=1.55,
                                  quantity=1,
                                  tax_rate=0.21,
                                  revenue_rate=0.15)

def get_tomato():
        return Product(name="Tomato",
                         cost=0.52,
                         quantity=1,
                         tax_rate=0.21,
                         revenue_rate=0.15)


class TestProduct:
    def test_calculate_price_with_revenue(self):
        iceberg_lettuce = get_iceberg_lettuce()
        iceberg_lettuce.calculate_total_cost()
        actual_cost_per_unit_with_revenue = iceberg_lettuce.cost_per_unit_with_revenue
        expected_cost_per_unit_with_revenue = 1.79
        assert actual_cost_per_unit_with_revenue == expected_cost_per_unit_with_revenue

    def test_calculate_price_with_revenue_and_after_tax(self):
        iceberg_lettuce = get_iceberg_lettuce()
        iceberg_lettuce.calculate_total_cost()
        actual_cost_per_unit_after_tax = iceberg_lettuce.cost_per_unit_after_tax
        expected_cost_per_unit_after_tax = 2.17
        assert actual_cost_per_unit_after_tax == expected_cost_per_unit_after_tax

    def test_calculate_total_price_with_revenue_and_after_tax_with_two_iceberg_lettuce(self):
        iceberg_lettuce = get_iceberg_lettuce()
        iceberg_lettuce.quantity = 2
        actual_total_cost = iceberg_lettuce.calculate_total_cost()
        expected_total_cost = 4.34
        assert actual_total_cost == expected_total_cost

    def test_check_if_product_has_same_name_as_another_product(self):
        iceberg_lettuce = get_iceberg_lettuce()
        iceberg_lettuce_2 = get_iceberg_lettuce()
        assert iceberg_lettuce.check_if_product_is_the_same(iceberg_lettuce_2)


class TestShoppingCart:
    def test_add_iceberg_lettuce(self):
        cart = ShoppingCart()
        cart.add_item(get_iceberg_lettuce())
        actual_shopping_cart = cart.get_shopping_cart()
        expected_shopping_cart_list = ShoppingCartList()
        iceberg_lettuce = get_iceberg_lettuce()
        iceberg_lettuce.calculate_total_cost()
        expected_shopping_cart_list.products = [iceberg_lettuce]
        expected_shopping_cart_list.total_cost = 2.17
        expected_shopping_cart_list.total_products = 1
        assert actual_shopping_cart == expected_shopping_cart_list

    def test_add_two_iceberg_lettuce(self):
        cart = ShoppingCart()
        iceberg_lettuce = get_iceberg_lettuce()
        iceberg_lettuce.quantity = 2
        cart.add_item(copy.deepcopy(iceberg_lettuce))
        actual_shopping_cart = cart.get_shopping_cart()
        expected_shopping_cart_list = ShoppingCartList()
        iceberg_lettuce.calculate_total_cost()
        expected_shopping_cart_list.products = [iceberg_lettuce]
        expected_shopping_cart_list.total_cost = 4.34
        expected_shopping_cart_list.total_products = 2
        assert actual_shopping_cart == expected_shopping_cart_list

    def test_add_one_iceberg_lettuce_then_one_tomato_then_another_iceberg_lettuce(self):
        cart = ShoppingCart()
        cart.add_item(get_iceberg_lettuce())
        cart.add_item(get_tomato())
        cart.add_item(get_iceberg_lettuce())
        actual_shopping_cart = cart.get_shopping_cart()
        expected_shopping_cart_list = ShoppingCartList()
        iceberg_lettuce = get_iceberg_lettuce()
        iceberg_lettuce.quantity = 2
        iceberg_lettuce.calculate_total_cost()
        tomato = get_tomato()
        tomato.calculate_total_cost()
        expected_shopping_cart_list.products = [iceberg_lettuce, tomato]
        expected_shopping_cart_list.total_cost = 5.07
        expected_shopping_cart_list.total_products = 3
        assert actual_shopping_cart == expected_shopping_cart_list

    def test_apply_discount_to_shopping_cart(self):
        cart = ShoppingCart()
        cart.add_item(get_iceberg_lettuce())
        cart.add_item(get_tomato())
        cart.apply_discount("PROMO_5")
        actual_shopping_cart = cart.get_shopping_cart()
        expected_shopping_cart_list = ShoppingCartList()
        iceberg_lettuce = get_iceberg_lettuce()
        iceberg_lettuce.calculate_total_cost()
        tomato = get_tomato()
        tomato.calculate_total_cost()
        expected_shopping_cart_list.products = [iceberg_lettuce, tomato]
        expected_shopping_cart_list.total_cost = 2.76
        expected_shopping_cart_list.total_products = 2
        assert actual_shopping_cart == expected_shopping_cart_list
    
    def test_delete_item_from_shopping_cart(self):
        cart = ShoppingCart()
        cart.add_item(get_iceberg_lettuce())
        cart.add_item(get_tomato())
        cart.get_shopping_cart()
        cart.delete_item(get_iceberg_lettuce())
        actual_shopping_cart = cart.get_shopping_cart()
        expected_shopping_cart_list = ShoppingCartList()
        tomato = get_tomato()
        tomato.calculate_total_cost()
        expected_shopping_cart_list.products = [tomato]
        expected_shopping_cart_list.total_cost = 0.73
        expected_shopping_cart_list.total_products = 1
        assert actual_shopping_cart == expected_shopping_cart_list
