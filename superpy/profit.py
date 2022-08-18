# imports
from revenue import get_total_revenue, get_revenue_between_dates
from inventory import GlobalInventory
from rich import print
from rich.console import Console 
from rich.table import Table

console = Console()


def get_total_profit():
    purchased_products = GlobalInventory.get_purchased_products()
    total_revenue = get_total_revenue()
    total = 0

    for product in purchased_products:
        total += float(product["buy_price"])

    sum = total_revenue - total
    format_sum = "%.2f" % sum
    return format_sum

def print_total_profit():
    total_profit = get_total_profit()

    table = Table(title="PROFIT REPORT", show_header=True, header_style="steel_blue")
    table.add_column("TOTAL PROFIT", style="green")
    table.add_row(f"€ {total_profit}")

    return console.print(table)


def get_profit_between_dates(first_date, second_date):
    total = 0
    products = GlobalInventory.get_purchased_between_dates(first_date, second_date)

    for product in products:
        total += float(product["buy_price"])
    return total

def print_profit_between_dates(first_date, second_date):
    buy_price = get_profit_between_dates(first_date, second_date)
    revenue = get_revenue_between_dates(first_date, second_date)
    profit = revenue - buy_price
    format_profit = "%.2f" % profit

    table = Table(title="DATE PROFIT REPORT", show_header=True, header_style="steel_blue")
    table.add_column("START DATE", style="dim", no_wrap=True)
    table.add_column("END DATE", style="dim")
    table.add_column("TOTAL PROFIT", style="green")
    table.add_row(f"{first_date}", f"{second_date}", f" €{format_profit}")

    return console.print(table)
