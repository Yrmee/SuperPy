# imports
import csv
import datetime

from date import get_date
from inventory import GlobalInventory
from rich import print
from rich.console import Console 
from rich.table import Table

console = Console()


# Create a new unique ID for products
def create_product_id(file_name):
    with open(file_name) as file:
        csv_reader = csv.reader(file)
        product_id = len(next(zip(*csv_reader)))
    return product_id

# Takes an integer and returns todays date plus the integer's number of days 
def get_expiration_date(days):
    date = get_date() 
    today = datetime.datetime.strptime(date, '%Y-%m-%d').date()  
    new_date = today + datetime.timedelta(days)
    return new_date

# Buy Products  
def buy_product(name_product, quantity, buy_price, expiration_days):
    buy_date = get_date()
    expiration_date = get_expiration_date(expiration_days)

    with open(GlobalInventory.purchasing_department, "a", newline="") as new_file:
        csv_writer = csv.writer(new_file)

        for x in range(quantity):
            id = create_product_id(GlobalInventory.purchasing_department) + x
            new_product = [id, name_product, buy_date, buy_price, expiration_date]
            csv_writer.writerow(new_product)
    
    table = Table(title="PURCHASED PRODUCT(S)", show_header=True, header_style="steel_blue")
    table.add_column("PRODUCT", style="dim", no_wrap=True)
    table.add_column("TOTAL")
    table.add_column("PRICE")
    table.add_column("EXPIRATION DATE")
    table.add_row(f"{name_product}", f"{quantity}", f"{buy_price}", f"{expiration_date}")

    console.print(table)