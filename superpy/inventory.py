# imports
import csv
from date import get_date

from rich.console import Console
from rich.table import Table

console = Console()

class Inventory:
    purchasing_department = './data/purchasing_dep.csv'
    sales_department = './data/sales_dep.csv'

    def overwritePurchasingDepartmentFile(self, file):
        self.purchasing_department = file

    def overwriteSaleDepartmentFile(self, file):
        self.sales_department = file

    # Get a list of dicts containg all purchased products - from purchasing_department.csv file.
    def get_purchased_products(self):
        purchased_products = []

        with open(self.purchasing_department, 'r') as purchased_products_object:
            csv_reader = csv.DictReader(purchased_products_object)
            for row in csv_reader:
                purchased_products.append(row)

        return purchased_products

    # Get list of id's of all purchased products
    def get_sold_products_id(self):
        sold_products_id = []

        with open(GlobalInventory.sales_department, 'r') as sold_products_id_object:
            csv_reader = csv.DictReader(sold_products_id_object)
            for row in csv_reader:
                sold_products_id.append(row["product_stock_id"])

        return sold_products_id

    # Get a list of dicts containing al sold products - from sales_departmpent.csv file.
    def get_sold_products(self):
        sold_products = []

        with open(GlobalInventory.sales_department, 'r', encoding='utf-8-sig') as sold_products_object:
            csv_reader = csv.DictReader(sold_products_object)
            for row in csv_reader:
                sold_products.append(row)

        return sold_products

    # Get available products from current_stock
    # Comparing purchased_products, sales_products and the expiration_date
    def get_available_products(self):
        purchased_products = GlobalInventory.get_purchased_products()
        id_sold_products = GlobalInventory.get_sold_products_id()
        today = get_date()
        available_products_list = []

        for product in purchased_products:
            if product["id"] not in id_sold_products and product["expiration_date"] >= today:
                available_products_list.append(product)
        return available_products_list

    # Get list of expired products
    # Comparing purchased_products, sales_products and expiration_dates
    def get_expired_products(self):
        purchased_products = GlobalInventory.get_purchased_products()
        id_sold_products = GlobalInventory.get_sold_products_id()
        today = get_date()

        expired_products_list = []

        for product in purchased_products:
            if product["id"] not in id_sold_products and product["expiration_date"] < today:
                expired_products_list.append(product)

        return expired_products_list

    # Get single available product from current_stock
    def get_one_available_product(self, name_product):
        purchased_products = GlobalInventory.get_purchased_products()
        id_sold_products = GlobalInventory.get_sold_products_id()
        today = get_date()

        available_product_list = []

        for product in purchased_products:
            if product["id"] not in id_sold_products and product["expiration_date"] >= today and product['name_product'] == name_product:
                available_product_list.append(product)

        if available_product_list == []:
            table = Table(title="", header_style="yellow")
            table.add_column("SALES INVENTORY ERROR", style="red")
            table.add_row("NO AVAILABLE PRODUCTS ARE FOUND")
            table.add_row("usage: stock -- Display current stock", style="white")
            console.print(table)
        else:
            return available_product_list

        # Takes two dates as arguments - format [YYYY/mm/dd] - returns products sold between the given dates.
    def get_sold_between_dates(self, first_date, second_date):
        sold_products = GlobalInventory.get_sold_products()
        between_dates_product_list = []

        for product in sold_products:
            if product["sales_date"] >= first_date and product["sales_date"] <= second_date:
                between_dates_product_list.append(product)
        return between_dates_product_list

    #  Takes two dates as arguments - format [YYYY/mm/dd] - returns products purchased between the given dates.
    def get_purchased_between_dates(self, first_date, second_date):
        purchased_products = GlobalInventory.get_purchased_products()
        products = []

        for product in purchased_products:
            if product["buy_date"] >= first_date and product["buy_date"] <= second_date:
                products.append(product)
        return products

    # Gets a dict of all the currently available products.
    # To use for the inventory report.
    def get_inventory(self):
        product_list = GlobalInventory.get_available_products()
        inventory = {}

        for product in product_list:
            if product["name_product"] in inventory.keys():
                inventory[product["name_product"]] += 1
            else:
                inventory.update({product["name_product"]: 1})

        return inventory

GlobalInventory = Inventory()