# User Manual SuperPy

## General Information - System Overview

> _SuperPy is Command-Line Tool Application, which allows collecting information about supermarket's inventory and finances.
The application provides electronic version of form used in collecting, editing and using this information. The application saves data collected to several internal databases._

---

## Index

* [Command-Line Tool Usage](#command-line-tool-usage)
* [Commands and Arguments Overview](#commands-and-required-arguments)
* [Usage Commands and Usage Commands with Required Arguments](#usage-commands-and-usage-commands-with-required-arguments)
  * [Command: advancetime](#command-advancetime)
  * [Command: system-date](#command-system-date)
  * [Command: set-current-date](#command-set-current-date)
  * [Command: sell](#command-sell)
  * [Command: buy](#command-buy)
  * [Command: stock](#command-stock)
  * [Command: sales](#command-sales)
  * [Command: purch](#command-purch)
  * [Command: expdep](#command-expdep)
  * [Command: totalrev](#command-totalrev)
  * [Command: daterev](#command-daterev)
  * [Command: totalprofit](#command-totalprofit)
  * [Command: dateprofit](#command-dateprofit)

---

## Command-Line Tool Usage

> _You must run the application locally on the local terminal._

To see the --help menu, run the command:

* `python ./main.py -h`

``` -
usage: main.py [-h] {advancetime,system-date,set-current-date,sell,buy,stock,sales,purch,expdep,totalrev,daterev,totalprofit,dateprofit} ...

SuperPy Supermarkt Inventory Management System: Supports buying and selling inventory, and returning statistics about inventory, revenue and profit.

-- Positional Arguments:
  {advancetime,system-date,set-current-date,sell,buy,stock,sales,purch,expdep,totalrev,daterev,totalprofit,dateprofit}
    advancetime         Set system date in Advance time in number of days
    system-date         Displays current System date
    set-current-date    Reset system date to current date
    sell                Starts SALE registration process
    buy                 Starts BUY registration process
    stock               Displays the Current Stock Department
    sales               Report Sales Department
    purch               Report Purchasing Department
    expdep              Report Expiration Department
    totalrev            Report Total Revenue
    daterev             Report Revenue between dates
    totalprofit         Report Total Profit
    dateprofit          Report Profit between dates

-- Optional Arguments:
  -h, --help            show this help message and exit
```

---

## **Commands and Required Arguments**

Commands | Description | Required Arguments
---------|----------|---------
advancetime | Set system date in advance time in number of days | -d --days
system-date | Displays current System date
set-current-date | Reset system date to current date
sell | Starts SELL registration process | -n --name, -q --quantity, -p --price
buy | Starts BUY registration process | -n --name, -q --quantity, -p --price, -exp --exp-date
stock | Displays the Current Stock Department
sales | Report Sales Department
purch | Report Purchasing Department
expdep | Report Expiration Department
totalrev | Report Total Revenue
daterev | Report Revenue between time of period | -fd --firstdate, -sd --seconddate
totalprofit | Report Total Profit
dateprofit | Report Profit between time of period | -fd --firstdate, -sd --seconddate

---

## **Usage Commands and Usage Commands with Required Arguments**

## _Command: advancetime_

> _advancetime: gives the opertunity to set the system-date in advance. This command needs 1 required argument. It is important to give this command a number of days of choice. The command will not run without the required argument. To check the current system date, run the command: [system-date](#command-system-date). To reset the system-date of advancetime, run the command: [set-current-date](#set-current-date), beware; This option is not reversible._

```-
Command: advancetime

use the following required argument: 
-d or --days      Number of days to set the system-date in advance

advancetime -d [DAYS_OF_ADVANCE]
advancetime --days [DAYS_OF_ADVANCE]
```

* `python ./main.py advancetime -d [DAYS_OF_ADVANCE]`
* `python ./main.py advancetime -d 5`

``` -
EXAMPLE:

  % python ./main.py advancetime -d 5

            SYSTEM DATE -- ADVANCE TIME            
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ PREVIOUS SYSTEM DATE: ┃ THE NEW SYSTEM DATE IS: ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 2022-08-03            │ 2022-08-08              │
└───────────────────────┴─────────────────────────┘
```

---

## _Command: system-date_

> _system-date returns the current system date. The system date does not automatically update by relaunch or using the application. Make sure to check the system date before starting any operation. You can reset the system-date to current date by the [command: set-current-date](#command-set-current-date). This command has no required arguments._

* `python ./main.py system-date`

``` -
EXAMPLE:

   % python ./main.py system-date

          SYSTEM DATE          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ THE CURRENT SYSTEM DATE IS: ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│  2022-08-03                 │
└─────────────────────────────┘
```

---

## _Command: set-current-date_

> _set-current-date resets automatically the system-date if it is not set to current date and will always return the current date. Be aware that this command is not reversible, to set another date read the documentation of command: [advancetime](#command-advancetime). To check the currents system date, run the command: [system-date](#system-date). **Command: set-current-date** has no required arguments._

* `python ./main.py set-current-date`

``` -
EXAMPLE: 

  % python ./main.py set-current-date 

        CURRENT DATE         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ THE DATE IS SET TO TODAY: ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│  2022-08-03               │
└───────────────────────────┘
```

---

## _Command: sell_

> _Starts the sales registration process. **Command: sell** needs to be followed by 3 required arguments in a particular order; Name of the product, the quantity and the sales price. It is important to include all arguments to complete this operation. For product names that includes whitespaces use after the first name argument triple ", type the name of product and close the name of the product with triple ". When no whitespaces are needed, the triple " are not necessary to write. Be aware that only the available amount of products in the current stock can be sold. To check the available amount of products in the current stock, run the command: [stock](#command-stock)._

```-
Command: sell

Use the 3 required arguments in the following order:
-n or --name          Name of Product
-q or --quantity      Number of quantity of products
-p or --price         Sales price of product

sell -n [NAME] -q [QUANTITY] -p [PRICE]
sell --name [NAME] --quantity [QUANTITY] --price [PRICE]

Note: For product names including whitespaces use triple " and close with triple ".
```

* `python ./main.py sell -n [NAME] -q [QUANTITY] -p [PRICE]`
* `python ./main.py sell -n """BIO+ RAW ORGANIC HONEY""" -q 3 -p 6.50`

```-
EXAMPLE: 

  % python ./main.py sell -n """BIO+ RAW ORGANIC HONEY""" -q 3 -p 6.50

                             SOLD PRODUCT(S)                             
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ PRODUCT                ┃ TOTAL ┃ PRICE ┃ DATE OF SALE ┃ CURRENT STOCK ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ BIO+ RAW ORGANIC HONEY │ 3     │ 6.5   │ 2022-08-08   │ 0             │
└────────────────────────┴───────┴───────┴──────────────┴───────────────┘
```

> ### Sales inventory Error

* _If trying to sell more than the available quantity of the current stock of a certain product, the Command-Line Tool application will return an Sales Inventory Error message. Check the current stock for information about the quantity of the product. More information about the current stock: [Command: stock](#command-stock)_

```-
EXAMPLE:

           INVENTORY DEPARTMENT            
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ PRODUCT                 ┃ CURRENT STOCK ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩ 
│ BIO+ RAW ORGANIC HONEY  │ 2             │
└─────────────────────────┴───────────────┘

  % python ./main.py sell -n """BIO+ RAW ORGANIC HONEY""" -q 3 -p 6.50
  
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ SALES INVENTORY ERROR                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ NO AVAILABLE PRODUCTS ARE FOUND       │
│ usage: stock -- Display current stock │
└───────────────────────────────────────┘
```

---

## _Command: buy_

> _Starts the BUY registration process. **Command: buy** needs 4 required arguments to complete this operation. It is important to include the name of the product, the quantity, the price of purchase and in how many days the product will expire in this particular order. For product names that includes whitespaces use after the first name argument triple ", type the name of product and close the name of the product with triple ". When no whitespaces are needed, the triple " are not necessary to write._

``` -
Command: buy 

Use the 4 required arguments in the following order:
 -n   or --name         Name of Product
 -q   or --quantity     Quantity of Products
 -p   or --price        Purchase Price
 -exp or --exp-date     Number of days of expiration

 buy -n [NAME] -q [QUANTITY] -p [PRICE] -exp [DAYS_OF_EXPIRATION]
 buy --name [NAME] --quantity [QUANTITY] --price [PRICE] --exp-date [DAYS_OF_EXPIRATION]

 Note: For product names including whitespaces use triple " and close with triple ".
```

* `python ./main.py buy -n [NAME] -q [QUANTITY] -p [PRICE] -exp [DAYS_OF_EXPIRATION]`
* `python ./main.py buy -n """BIO+ RAW ORGANIC HONEY""" -q 3 -p 3.50 -exp 5`

```-
EXAMPLE: 

  % python ./main.py buy -n """BIO+ RAW ORGANIC HONEY""" -q 3 -p 3.50 -exp 6

                    PURCHASED PRODUCT(S)                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ PRODUCT                ┃ TOTAL ┃ PRICE ┃ EXPIRATION DATE ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ BIO+ RAW ORGANIC HONEY │ 3     │ 3.5   │ 2022-08-09      │
└────────────────────────┴───────┴───────┴─────────────────┘
```

---

## _Command: stock_

> _**Command: stock** returns the collected data of the current stock in an overview. It displays the name of the product and how many items the product are available for sale. This inventory will automatically be updated when purchased and sales are made. When products are sold or expired during time, these products will no longer be visible in the current stock department. **Command: stock**, has no required arguments._

* `python ./main.py stock`

``` -
EXAMPLE:

  % python ./main.py stock

           INVENTORY DEPARTMENT            
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ PRODUCT                 ┃ CURRENT STOCK ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ BIO+ RAW DARK CHOCOLATE │ 10            │
│ BIO+ QUINOA             │ 4             │
│ BIO+ RAW ORGANIC HONEY  │ 5             │
│ BIO+ MAPLE SYRUP        │ 3             │
└─────────────────────────┴───────────────┘
```

---

## _Command: sales_

> _**Command: sales** returns the collected data of the sales department which contains all sales that have been proceeded. This sales department will automatically update when a sales-process have been completed. The Sales Department contains information about the Product, Date of Sale and Sales Price. **Command: sales** has no required arguments._

* `python ./main.py sales`

``` -
EXAMPLE:

  % python ./main.py sales

          SALES DEPARTMENT                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ PRODUCT                ┃ DATE OF SALE ┃ PRICE SALE ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩       
│ BIO+ OATS              │ 2022-08-03   │ 4.5        │        
│ BIO+ ALMOND MILK       │ 2022-08-03   │ 3.5        │  
│ BIO+ GINGER            │ 2022-08-03   │ 5.5        │
│ BIO+ GINGER            │ 2022-08-03   │ 5.5        │     
│ BIO+ BROWN RICE        │ 2022-08-03   │ 6.5        │
│ BIO+ BROWN RICE        │ 2022-08-03   │ 6.5        │
│ BIO+ BROWN RICE        │ 2022-08-03   │ 6.5        │              
│ BIO+ HERBAL TEA        │ 2022-08-03   │ 4.5        │     
│ BIO+ QUINOA            │ 2022-08-03   │ 5.5        │
│ BIO+ QUINOA            │ 2022-08-03   │ 5.5        │   
│ BIO+ RAW ORGANIC HONEY │ 2022-08-03   │ 6.5        │
└────────────────────────┴──────────────┴────────────┘
```

---

## _Command: purch_

> _**Command: purch** runs the Purchasing Department and returns information about all the collected data of purchases that are made and will automatically stay updated when purchases of products are made. This Purchasing Department shows information about which Product, Purchase Date, Purchase Price and the Expiration Date of the Product. All purchases stay stored in the Purchasing Department database. **Command: purch** has no required arguments._

* `python ./main.py purch`

``` -
EXAMPLE:

  % python ./main.py purch

                            PURCHASING DEPARTMENT                             
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ PRODUCT                 ┃ PURCHASE DATE ┃ PURCHASE PRICE ┃ EXPIRATION DATE ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩     
│ BIO+ OATS               │ 2022-07-14    │ 2.56           │ 2022-07-24      │
│ BIO+ OATS               │ 2022-07-14    │ 2.56           │ 2022-07-24      │ 
│ BIO+ RAW DARK CHOCOLATE │ 2022-07-14    │ 2.99           │ 2022-08-08      │  
│ BIO+ RAW DARK CHOCOLATE │ 2022-07-14    │ 2.99           │ 2022-08-08      │
│ BIO+ RAW DARK CHOCOLATE │ 2022-07-14    │ 2.99           │ 2022-08-08      │
│ BIO+ QUINOA             │ 2022-07-19    │ 1.85           │ 2022-07-29      │
│ BIO+ QUINOA             │ 2022-07-19    │ 1.85           │ 2022-07-29      │    
│ BIO+ ALMOND MILK        │ 2022-07-19    │ 2.85           │ 2022-07-26      │
│ BIO+ ALMOND MILK        │ 2022-07-19    │ 2.85           │ 2022-07-26      │     
│ BIO+ HERBAL TEA         │ 2022-07-21    │ 3.5            │ 2022-07-31      │
│ BIO+ HERBAL TEA         │ 2022-07-21    │ 3.5            │ 2022-07-31      │ 
│ BIO+ BROWN RICE         │ 2022-07-22    │ 3.5            │ 2022-08-01      │
│ BIO+ BROWN RICE         │ 2022-07-22    │ 3.5            │ 2022-08-01      │   
│ BIO+ GINGER             │ 2022-07-22    │ 3.55           │ 2022-07-27      │
│ BIO+ GINGER             │ 2022-07-22    │ 3.55           │ 2022-07-27      │      
│ BIO+ QUINOA             │ 2022-07-22    │ 2.5            │ 2022-08-16      │
│ BIO+ QUINOA             │ 2022-07-22    │ 2.5            │ 2022-08-16      │     
│ BIO+ RAW ORGANIC HONEY  │ 2022-08-03    │ 3.5            │ 2022-08-09      │
│ BIO+ RAW ORGANIC HONEY  │ 2022-08-03    │ 3.5            │ 2022-08-09      │    
│ BIO+ MAPLE SYRUP        │ 2022-08-03    │ 2.8            │ 2022-08-09      │
│ BIO+ MAPLE SYRUP        │ 2022-08-03    │ 2.8            │ 2022-08-09      │
│ BIO+ MAPLE SYRUP        │ 2022-08-03    │ 2.8            │ 2022-08-09      │
└─────────────────────────┴───────────────┴────────────────┴─────────────────┘
```

---

## _Command: expdep_

> _**Command: expdep** returns the Expiration Department that keeps track of the collected data of information about expired products. It gives information about the Product, Purchase Date, Purchase Price and Expiration Date. The current stock will update automatically if products are expired and products will no longer be visible in the current stock. **Command: expdep** has no required arguments._

* `python ./main.py expdep`

``` -
EXAMPLE:

  % python ./main.py expdep

                         EXPIRATION DEPARTMENT                         
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ PRODUCT          ┃ PURCHASE DATE ┃ PURCHASE PRICE ┃ EXPIRATION DATE ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ BIO+ MAPLE SYRUP │ 2022-07-14    │ 4.99           │ 2022-07-19      │
│ BIO+ MAPLE SYRUP │ 2022-07-14    │ 4.99           │ 2022-07-19      │
│ BIO+ MAPLE SYRUP │ 2022-07-14    │ 4.99           │ 2022-07-19      │
│ BIO+ MAPLE SYRUP │ 2022-07-14    │ 4.99           │ 2022-07-19      │
│ BIO+ ALMOND MILK │ 2022-07-19    │ 2.85           │ 2022-07-26      │
│ BIO+ ALMOND MILK │ 2022-07-19    │ 2.85           │ 2022-07-26      │
│ BIO+ HERBAL TEA  │ 2022-07-21    │ 3.5            │ 2022-07-31      │
│ BIO+ BROWN RICE  │ 2022-07-22    │ 3.5            │ 2022-08-01      │
│ BIO+ BROWN RICE  │ 2022-07-22    │ 3.5            │ 2022-08-01      │
│ BIO+ GINGER      │ 2022-07-22    │ 3.55           │ 2022-07-27      │
│ BIO+ GINGER      │ 2022-07-22    │ 3.55           │ 2022-07-27      │
└──────────────────┴───────────────┴────────────────┴─────────────────┘
```

---

## _Command: totalrev_

> _**Command: totalrev** returns a report the total revenue of all transactions that have been reported of all departments. **Command: totalrev** has no required arugments._

* `python ./main.py totalrev`

``` -
EXAMPLE:

  % python ./main.py totalrev

 REVENUE REPORT  
┏━━━━━━━━━━━━━━━┓
┃ TOTAL REVENUE ┃
┡━━━━━━━━━━━━━━━┩
│ 421.47        │
└───────────────┘
```

---

## _Command: daterev_

> _**Command: daterev** returns a report the collected data of the total revenue between two specified dates. **Command: daterev** needs 2 required arguments. It is important to include a start date and an end date in the format [YYYY-mm-dd] to set a time of period to complete this operation. The report gives information about the given time of period and the total revenue of the given dates._

``` -
Use the required 2 arguments in the following order:
-fd or --firstdate          Start date of period
-sd or --seconddate         End date of period

Format of date is [YYYY-mm-dd]
```

* `python ./main.py daterev -fd [YYYY-mm-dd] -sd [YYYY-mm-dd]`
* `python ./main.py daterev -fd 2022-07-10 -sd 2022-08-03`

``` -
EXAMPLE:

  % python ./main.py daterev -fd 2022-07-10 -sd 2022-08-03

              DATE REVENUE REPORT               
┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ START DATE ┃ END DATE   ┃ TOTAL DATE REVENUE ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ 2022-07-10 │ 2022-08-03 │  €250.14           │
└────────────┴────────────┴────────────────────┘
```

---

## _Command: totalprofit_

> _**Command: totalprofit** returns a report that contains the total profit of all transactions that have been reported of all departments. **Command: totalprofit** has no required arguments._

* `python ./main.py totalprofit`

``` -
EXAMPLE:

  % python ./main.py totalprofit

 PROFIT REPORT  
┏━━━━━━━━━━━━━━┓
┃ TOTAL PROFIT ┃
┡━━━━━━━━━━━━━━┩
│ € 82.16      │
└──────────────┘
```

---

## _Command: dateprofit_

> _**Command: dateprofit** returns a report of the collected data of the total profit between two specified dates. **Command: dateprofit** needs 2 required arguments. It is important to include the a start date and an end date in the format [YYYY-mm-dd] to set a time of period to complete this operation. The report gives information about the given time of period and the total profit of the given dates._

``` -
Use the required 2 arguments in the following order:
-fd or --firstdate          Start date of period
-sd or --seconddate         End date of period

Format of date is [YYYY-mm-dd]
```

* `python ./main.py dateprofit -fd [YYYY-mm-dd] -sd [YYYY-mm-dd]`
* `python ./main.py dateprofit -fd 2022-07-10 -sd 2022-08-03`

``` -
EXAMPLE:

  % python ./main.py dateprofit -fd 2022-07-10 -sd 2022-08-03

            DATE PROFIT REPORT            
┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ START DATE ┃ END DATE   ┃ TOTAL PROFIT ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ 2022-07-10 │ 2022-08-03 │  €182.16     │
└────────────┴────────────┴──────────────┘
```

---

[Back to Top of the User Manual](#user-manual-superpy)
