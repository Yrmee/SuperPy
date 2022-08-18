# imports
from inventory import GlobalInventory
from rich.console import Console
from rich.table import Table 

console = Console()


# Takes the inventory and displays it in a table 
def display_inventory():
    inventory = GlobalInventory.get_inventory()

    table = Table(title="INVENTORY DEPARTMENT", show_header=True, header_style="steel_blue")
    table.add_column('PRODUCT', style='dim')
    table.add_column('CURRENT STOCK')

    for key, value in inventory.items():
        table.add_row(
            key, 
            str(value),
        )
    console.print(table)

# Adds product names to the sale data and prints a table to display the sale data
def display_sales():
    sales = GlobalInventory.get_sold_products()
    purchases = GlobalInventory.get_purchased_products()

    for sales_product in sales:
        for purchases_product in purchases:
            if sales_product["product_stock_id"] == purchases_product["id"]:
                sales_product.update({"name_product": purchases_product["name_product"]})
    
    table = Table(title="SALES DEPARTMENT", show_header=True, header_style="steel_blue")
    table.add_column('PRODUCT', style='dim')
    table.add_column('DATE OF SALE')
    table.add_column('PRICE SALE')

    for sales_product in sales:
        table.add_row(
            sales_product['name_product'],
            sales_product['sales_date'],
            sales_product['selling_price']
        )
    console.print(table)

# Gets purchased products from purchasing_department.csv and shows relevant data in a table
def display_purchases():
    purchases = GlobalInventory.get_purchased_products()

    table = Table(title="PURCHASING DEPARTMENT", show_header=True, header_style="steel_blue")
    table.add_column('PRODUCT', style='dim')
    table.add_column('PURCHASE DATE')
    table.add_column('PURCHASE PRICE')
    table.add_column('EXPIRATION DATE')

    for product in purchases:
        table.add_row(
            product['name_product'],
            product['buy_date'],
            product['buy_price'],
            product['expiration_date']
        )
    console.print(table)

# Shows expired products list
def display_expired():
    expired_products = GlobalInventory.get_expired_products()

    table = Table(title="EXPIRATION DEPARTMENT", show_header=True, header_style="steel_blue")
    table.add_column('PRODUCT', style='dim')
    table.add_column('PURCHASE DATE')
    table.add_column('PURCHASE PRICE')
    table.add_column('EXPIRATION DATE')

    for product in expired_products:
        table.add_row(
            product['name_product'],
            product['buy_date'],
            product['buy_price'],
            product['expiration_date'],
        )
    console.print(table)




