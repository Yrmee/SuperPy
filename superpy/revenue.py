# imports
from inventory import GlobalInventory
from rich.console import Console
from rich.table import Table

console = Console()

# Gets total amount of revenue from all the selling prices of sold products
def get_total_revenue():
    sold_products = GlobalInventory.get_sold_products()
    total = 0

    for product in sold_products:
        total += float(product['selling_price'])
    return total 

def print_total_revenue():
    total_revenue = get_total_revenue()
    table = Table(title="REVENUE REPORT", show_header=True, header_style="bold steel_blue")
    table.add_column("TOTAL REVENUE", style="green")
    table.add_row(f"{total_revenue}")

    console.print(table)



# Gets total revenue of a period between two given dates
def get_revenue_between_dates(first_date, second_date):
    total = 0
    products = GlobalInventory.get_sold_between_dates(first_date, second_date)

    for product in products:
        total += float(product['selling_price'])
    return total 


def print_revenue_between_dates(first_date, second_date):
    total_revenue = get_revenue_between_dates(first_date, second_date)

    table = Table(title="DATE REVENUE REPORT", show_header=True, header_style="steel_blue")
    table.add_column("START DATE", style="dim", no_wrap=True)
    table.add_column("END DATE", style="dim")
    table.add_column("TOTAL DATE REVENUE", style="green")
    table.add_row(f"{first_date}", f"{second_date}",f" €{total_revenue}")

    console.print(table)

