# imports
import datetime
import os
from rich.console import Console 
from rich.table import Table
from rich import print

console = Console()

# path date
DATE = "./data/date.txt"

def get_date():
    with open(DATE, 'r') as date_file:
        for row in date_file:
            return row

def print_date():
    date = ''
    with open(DATE, 'r') as print_date_file:
        for row in print_date_file:
            date = row 
    
    table = Table(title="SYSTEM DATE", show_header=True, header_style="bold steel_blue")
    table.add_column('THE CURRENT SYSTEM DATE IS:', style="bold white")
    table.add_row(f" {date}")
    console.print(table)


# Get today's date and store it in a CSV file
def set_date_today(today = str(datetime.date.today())):
    with open(DATE, 'w') as today_date_file:
        today_date_file.write(today)

    table = Table(title="CURRENT DATE", show_header=True, header_style="bold steel_blue")
    table.add_column('THE DATE IS SET TO TODAY:', style="bold green")
    table.add_row(f" {today}")
    console.print(table)


def advance_date(days):
    try:
        today = datetime.datetime.strptime(get_date(), '%Y-%m-%d').date()
        new_date = today + datetime.timedelta(days)

        with open(DATE, 'w') as advance_date_file:
            advance_date_file.write(str(new_date))
            
            table = Table(title="SYSTEM DATE -- ADVANCE TIME", show_header=True, header_style="bold steel_blue")
            table.add_column('PREVIOUS SYSTEM DATE:', style="bold red")
            table.add_column('THE NEW SYSTEM DATE IS:', style="bold green")
            table.add_row(f"{today}", f"{new_date}")
            console.print(table)

    except ValueError:
        table = Table(show_header=True, header_style="bold yellow")
        table.add_column("VALUE ERROR", style="bold red")
        table.add_row("Not a valid value. Please enter a valid value")
        console.print(table)