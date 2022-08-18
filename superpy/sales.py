# imports
import csv

from purchases import create_product_id
from date import get_date
from inventory import GlobalInventory

from rich.table import Table 
from rich.console import Console

console = Console()


def sales_product(name_product, quantity, selling_price):
    sales_date = get_date()
    available_products = GlobalInventory.get_one_available_product(name_product)

    if available_products != None:
        if quantity > len(available_products):
            table = Table(title="UPDATE INVENTORY", show_header=True, header_style="steel_blue")
            table.add_column('PRODUCT', style='dim')
            table.add_column('CURRENT PRODUCT(S) IN STOCK')
            table.add_column('', style="red")
            table.add_row(f"{name_product}", f"{len(available_products)}", "NOT ENOUGH PRODUCTS AVAILABLE")
            console.print(table)
        else:
            with open(GlobalInventory.sales_department, "a", newline="") as sales_file:
                csv_writer = csv.writer(sales_file)

                for i in range(quantity):
                    product_stock_id = available_products[i]["id"]
                    id = create_product_id(GlobalInventory.sales_department) + i
                    sold_product = [id, product_stock_id, sales_date, selling_price]
                
                    csv_writer.writerow(sold_product)

            table = Table(title="SOLD PRODUCT(S)", show_header=True, header_style="steel_blue")
            table.add_column("PRODUCT", style="yellow", no_wrap=True)
            table.add_column("TOTAL")
            table.add_column("PRICE")
            table.add_column("DATE OF SALE")
            table.add_column("CURRENT STOCK", style="green")
            table.add_row(f"{name_product}", f"{quantity}", f"{selling_price}", f"{sales_date}", f"{len(available_products) - quantity}")

            console.print(table)