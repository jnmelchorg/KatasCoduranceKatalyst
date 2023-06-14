from src.ShoppingCart import ShoppingCart, Product, ShoppingCartList


class TestShoppingCart:
    def test_add_iceberg_lettuce(self):
        cart = ShoppingCart(ShoppingCartList())
        iceberg_lettuce = Product(name="Iceberg Lettuce",
                                  cost=1.55,
                                  quantity=1,
                                  tax_rate=0.21,
                                  revenue_rate=0.15)
        cart.add_item(iceberg_lettuce)
        actual_shopping_cart = cart.get_shopping_cart()
        expected_shopping_cart_list = ShoppingCartList()
        expected_shopping_cart_list.products = [iceberg_lettuce]
        expected_shopping_cart_list.total_cost = 2.17
        expected_shopping_cart_list.total_products = 1
        assert actual_shopping_cart == expected_shopping_cart_list
