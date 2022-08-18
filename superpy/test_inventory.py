# imports
from purchases import buy_product
from sales import sales_product
from profit import get_total_profit
from inventory import GlobalInventory
from date import set_date_today

class Test:
    @classmethod
    def setup_method(self, method):
        f = open("data/purchasing_dep_test.csv", "w")
        f.write("id,name_product,buy_date,buy_price,expiration_date\n")
        f.close()

        f = open("data/sales_dep_test.csv", "w")
        f.write("id,product_stock_id,sales_date,selling_price\n")
        f.close()

        GlobalInventory.overwritePurchasingDepartmentFile('data/purchasing_dep_test.csv')
        GlobalInventory.overwriteSaleDepartmentFile('data/sales_dep_test.csv')

        set_date_today("2022-08-15")

    def test_get_total_profit(self):
        buy_product("Foo", 10, 10.2, 30)
        sales_product("Foo", 10, 12.0)

        assert get_total_profit() == '18.00'

    def test_get_purchased_products(self):
        buy_product("Foo", 1, 10.2, 5)

        assert GlobalInventory.get_purchased_products() == [
            {
                'buy_date': '2022-08-15',
                'buy_price': '10.2',
                'expiration_date': '2022-08-20',
                'id': '1',
                'name_product': 'Foo'
            }
        ]

    def test_get_sold_product_id(self):
        buy_product("Foo", 10, 10.2, 5)
        sales_product("Foo", 1, 12.0)

        assert GlobalInventory.get_sold_products_id() == ['1']

    def test_get_available_products(self):
        buy_product("Foo", 10, 10.2, 0)
        buy_product("Baz", 1, 8.5, 6)
        buy_product("Bar", 1, 10.2, 6)

        set_date_today("2022-08-20")

        assert GlobalInventory.get_available_products() == [
            {
                'buy_date': '2022-08-15',
                'buy_price': '8.5',
                'expiration_date': '2022-08-21',
                'id': '11',
                'name_product': 'Baz'
            },
            {
                'buy_date': '2022-08-15',
                'buy_price': '10.2',
                'expiration_date': '2022-08-21',
                'id': '12',
                'name_product': 'Bar'
            }
        ]

    def test_get_expired_products(self):
        buy_product("Foo", 1, 10.2, 1)

        set_date_today("2022-08-20")

        assert GlobalInventory.get_expired_products() == [
            {
                'buy_date': '2022-08-15',
                'buy_price': '10.2',
                'expiration_date': '2022-08-16',
                'id': '1',
                'name_product': 'Foo'
            }
        ]

    def test_get_one_available_product(self):
        buy_product("Baz", 1, 8.5, 6)

        assert GlobalInventory.get_one_available_product("Baz") == [{
            'buy_date': '2022-08-15',
            'buy_price': '8.5',
            'expiration_date': '2022-08-21',
            'id': '1',
            'name_product': 'Baz'
        }]

    def test_get_sold_between_dates(self):
        buy_product("Foo", 10, 8.5, 10)
        sales_product("Foo", 1, 12.0)
        set_date_today("2022-08-16")
        sales_product("Foo", 1, 12.0)
        set_date_today("2022-08-17")
        sales_product("Foo", 1, 12.0)

        assert GlobalInventory.get_sold_between_dates("2022-08-15", "2022-08-16") == [{
            'id': '1',
            'product_stock_id': '1',
            'sales_date': '2022-08-15',
            'selling_price': '12.0'
        }, {
            'id': '2',
            'product_stock_id': '2',
            'sales_date': '2022-08-16',
            'selling_price': '12.0'
        }]

    def test_get_purchased_between_dates(self):
        buy_product("Foo", 1, 8.5, 10)
        set_date_today("2022-08-16")
        buy_product("Bar", 1, 8.5, 10)
        set_date_today("2022-08-17")
        buy_product("Baz", 1, 8.5, 10)

        assert GlobalInventory.get_purchased_between_dates("2022-08-15", "2022-08-16") == [{
            'buy_date': '2022-08-15',
            'buy_price': '8.5',
            'expiration_date': '2022-08-25',
            'id': '1',
            'name_product': 'Foo'
        }, {
            'buy_date': '2022-08-16',
            'buy_price': '8.5',
            'expiration_date': '2022-08-26',
            'id': '2',
            'name_product': 'Bar'
        }]

    def test_get_inventory(self):
        buy_product("Foo", 10, 8.5, 10)
        buy_product("Bar", 5, 1.0, 7)

        assert GlobalInventory.get_inventory() == {'Bar': 5, 'Foo': 10}
