# Imports
import argparse
from datetime import datetime

from date import set_date_today, print_date, advance_date 
from purchases import buy_product
from sales import sales_product 
from tables import display_inventory, display_sales, display_purchases, display_expired
from revenue import print_total_revenue, print_revenue_between_dates
from profit import print_total_profit, print_profit_between_dates



# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
# ----------------------------------------------------------------

# Checks if <type>date is given in a valid format in arguments
def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        msg = "not a valid date: {0!r}".format(s)
        raise argparse.ArgumentTypeError(msg)


parser = argparse.ArgumentParser(description="SuperPy Supermarkt Inventory Management System: Supports buying and selling inventory, and returning statistics about inventory, revenue and profit.")
subparser = parser.add_subparsers(dest="command", required=True)

parser._positionals.title = "-- Positional Arguments"
parser._optionals.title = "-- Optional Arguments"

# DATE -- Parser Arguments
# Hier moet ik even over nadenken, want vind nergens op slaan deze optie.
advance_time = subparser.add_parser("advancetime", help="Set system date in Advance time in number of days")
advance_time.add_argument("-d", "--days", type=int, help="Number of days")

system_date = subparser.add_parser("system-date", help="Displays current System date")
current_date = subparser.add_parser("set-current-date", help="Set system to current date")

# SALES -- Parser Arguments
sell = subparser.add_parser("sell", help="Starts SALE registration process")
sell.add_argument("-n", "--name", type=str, help="Name of product")
sell.add_argument("-q", "--quantity", type=int, help="Amount of products")
sell.add_argument("-p", "--price", type=float, help="Price of product")

# PURCHASING -- Parser Arguments
buy = subparser.add_parser("buy", help="Starts BUY registration process")
buy.add_argument("-n", "--name", type=str, help="Name of product")
# inputArgument = """+argumentStoringValue+"""
buy.add_argument("-q", "--quantity", type=int, help="Amount of products")
buy.add_argument("-p", "--price", type=float, help="Price of product")
buy.add_argument("-exp", "--exp-date", type=int, help="Number of days for expiration")

# INVENTORY -- Parser Arguments
inventory = subparser.add_parser("stock", help="Displays the Current Stock Department")
sales_department = subparser.add_parser("sales", help="Report Sales Department")
purchasing_department = subparser.add_parser("purch", help="Report Purchasing Department")
expiration_department = subparser.add_parser("expdep", help="Report Expiration Department")

# REVENUE -- Parser Arguments
total_revenue = subparser.add_parser("totalrev", help="Report Total Revenue")
date_revenue = subparser.add_parser("daterev", help="Report Revenue between dates")
date_revenue.add_argument("-fd", "--firstdate", type=valid_date, help="START date to set time period", required=True)
date_revenue.add_argument("-sd", "--seconddate", type=valid_date, help="END date to set time period", required=True)

# PROFIT -- Parser Arguments
total_profit = subparser.add_parser("totalprofit", help="Report Total Profit")
date_profit = subparser.add_parser("dateprofit", help="Report Profit between dates")
date_profit.add_argument("-fd", "--firstdate", type=valid_date, help="START date to set time period", required=True)
date_profit.add_argument("-sd", "--seconddate", type=valid_date, help="END date to set time period", required=True)


def main():
    args = parser.parse_args()

    if args.command == "system-date":
        print_date()

    elif args.command == "set-current-date":
        set_date_today()

    elif args.command == "advancetime":
        advance_date(args.days)
    
    elif args.command == "buy":
        buy_product(
            args.name,
            args.quantity, 
            args.price,
            args.exp_date
        )
    
    elif args.command == "sell":
        sales_product(
            args.name,
            args.quantity,
            args.price
        )
    
    elif args.command == "totalrev":
        print_total_revenue()
    
    elif args.command == "daterev":
        print_revenue_between_dates(
            args.firstdate,
            args.seconddate
        )
    
    elif args.command == "totalprofit":
        print_total_profit()
    
    elif args.command == "dateprofit":
        print_profit_between_dates(
            args.firstdate,
            args.seconddate
        )
    
    elif args.command == "stock":
        display_inventory()
    
    elif args.command == "sales":
        display_sales()
    
    elif args.command == "purch":
        display_purchases()
    
    elif args.command == "expdep":
        display_expired()

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
