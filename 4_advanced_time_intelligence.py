# ADVANCED CALCULATE
% of Store Sales (REMOVEFILTERS) = 
VAR AllStoreSales = 
CALCULATE(
    [Customer Sales],
    REMOVEFILTERS(
        'Store Lookup'[store_id]
    )
)
VAR Ratio = 
DIVIDE(
    [Customer Sales],
    AllStoreSales
)
RETURN
Ratio


CALCULATE Sum Quantity Sold = 
CALCULATE(
    SUM(
        'Food Inventory'[quantity_sold]
    )
)

Store 3 Sales (KEEPFILTERS) = 
CALCULATE(
    [Customer Sales],
    KEEPFILTERS(
        'Store Lookup'[store_id] = 3
    )
)

Store 3 Sales of Whole Beans & Teas (ALL Modifier) = 
CALCULATE(
    [Customer Sales],
    'Store Lookup'[store_id] = 3,
    'Product Lookup'[product_group] = "Whole Bean/Teas",
    ALL(
        'Store Lookup'
    )
)

Store 3 Sales of Whole Beans & Teas (CALCULATE) = 
CALCULATE(
    [Customer Sales],
    'Store Lookup'[store_id] = 3,
    'Product Lookup'[product_group] = "Whole Bean/Teas"
)

Store 5 Profit = 
CALCULATE(
    [Profit],
    'Store Lookup'[store_id] = 5
)

Store 5 Profit (KEEPFILTERS) = 
CALCULATE(
    [Profit],
    KEEPFILTERS(
        'Store Lookup'[store_id] = 5
    )
)

Store 5 Sales (KEEPFILTERS) = 
CALCULATE(
    [Customer Sales],
    KEEPFILTERS(
        'Store Lookup'[store_id] = 5
    )
)

Store 8 Sales (KEEPFILTERS) = 
CALCULATE(
    [Customer Sales],
    KEEPFILTERS(
        'Store Lookup'[store_id] = 8
    )
)

SUM Quantity Sold = 
SUM(
    'Food Inventory'[quantity_sold]
)

Total Profit = 
CALCULATE(
    [Profit],
    REMOVEFILTERS(
        'Sales by Store'
    )
)

#ADVANCED TIME INTELLIGENCE
% of Total Sales = 
VAR AllSales =
CALCULATE(
    [Customer Sales],
    ALL(
        'Sales by Store'
    )
)
VAR Ratio =
DIVIDE(
    [Customer Sales],
    AllSales
)
Return
Ratio

Customer Sales Last Month (PARALLELPERIOD) = 
CALCULATE(
    [Customer Sales],
    PARALLELPERIOD(
        'Calendar'[Transaction_Date],
        -1,
        MONTH
    )
)

Customer Sales MoM % Change = 
DIVIDE(
    ([Customer Sales] - [Customer Sales Last Month (PARALLELPERIOD)]),
    [Customer Sales Last Month (PARALLELPERIOD)],
    BLANK()
)

Customer Sales YoY % Change = 
VAR LastYearsSales = 
CALCULATE(
    [Customer Sales],
    SAMEPERIODLASTYEAR(
        'Calendar'[Transaction_Date]
    )
)
VAR Ratio =
DIVIDE(
    ([Customer Sales] - LastYearsSales),
    LastYearsSales,
    "-"
)
Return
Ratio

Last QTD Sales (4-5-4) = 
VAR LastPeriod =
CALCULATE(
    [Customer Sales],
    FILTER(
        ALL(
            '4-5-4 Calendar'
        ),
        IF(
            SELECTEDVALUE('4-5-4 Calendar'[FiscalQuarter]) = 1,
            '4-5-4 Calendar'[FiscalQuarter] =4 && '4-5-4 Calendar'[FiscalYear] = SELECTEDVALUE('4-5-4 Calendar'[FiscalYear]) -1,
            '4-5-4 Calendar'[FiscalYear] = SELECTEDVALUE('4-5-4 Calendar'[FiscalYear]) &&
            '4-5-4 Calendar'[FiscalQuarter] = SELECTEDVALUE('4-5-4 Calendar'[FiscalQuarter]) -1
        )
    )
)
RETURN
LastPeriod

Last Quarter's Sales (PARALLELPERIOD) = 
CALCULATE(
    [Customer Sales],
    PARALLELPERIOD(
        'Calendar'[Transaction_Date],
        -1,
        QUARTER
    )
)

Last Quarter's Sales (PREVIOUSQUARTER) = 
CALCULATE(
    [Customer Sales],
    PREVIOUSQUARTER(
        'Calendar'[Transaction_Date]
    )
)

Last Week's Sales 4-5-4 (DATEADD) = 
CALCULATE(
    [Customer Sales],
    DATEADD(
        '4-5-4 Calendar'[Date],
        -7,
        DAY
    )
)

Last Years Sales (SAMEPERIODLASTYEAR) = 
CALCULATE(
    [Customer Sales],
    SAMEPERIODLASTYEAR(
        'Calendar'[Transaction_Date]
    )
)

MTD Sales (4-5-4) = 
VAR MaxDate = MAX('4-5-4 Calendar'[Date])
VAR MaxPeriod = MAX('4-5-4 Calendar'[FiscalMonthYear])
VAR OutPut =
IF(
    HASONEVALUE(
        '4-5-4 Calendar'[FiscalMonthName]
    ),
    CALCULATE(
        [Customer Sales],
        '4-5-4 Calendar'[Date] <= MaxDate,
        '4-5-4 Calendar'[FiscalMonthYear] = MaxPeriod
    ),
    "-"
)
RETURN
OutPut


QTD Sales (4-5-4) = 
VAR MaxDate = MAX('4-5-4 Calendar'[Date])
VAR MaxPeriod = MAX('4-5-4 Calendar'[FiscalQuarterYear])
VAR OutPut =
IF(
    HASONEVALUE(
        '4-5-4 Calendar'[FiscalQuarterYear]
    ),
    CALCULATE(
        [Customer Sales],
        '4-5-4 Calendar'[Date] <= MaxDate,
        '4-5-4 Calendar'[FiscalQuarterYear] = MaxPeriod
    ),
    "-"
)
RETURN
OutPut


WoW % Change (4-5-4) = 
DIVIDE(
    ([Customer Sales] - [Last Week's Sales 4-5-4 (DATEADD)]),
    [Last Week's Sales 4-5-4 (DATEADD)],
    BLANK()
)
     
     

YTD Sales (4-5-4) = 
VAR MaxDate = MAX('4-5-4 Calendar'[Date])
VAR MaxPeriod = MAX('4-5-4 Calendar'[FiscalYear])
VAR MaxSellDate = MAX('Sales by Store'[transaction_date])
VAR OutPut =
CALCULATE(
    [Customer Sales],
    '4-5-4 Calendar'[Date] <= MaxDate,
    '4-5-4 Calendar'[FiscalYear] = MaxPeriod,
    'Calendar'[Transaction_Date] <= MaxSellDate
)
RETURN
OutPut
     
     
#CALCULATED TABLE JOINS
Profit (INTERSECT Assignment) = 
SUM(
    'Repeat Customer Sales (INTERSECT Assignment)'[Profit]
)
     
     
Revenue (INTERSECT Assignment) = 
SUM(
    'Repeat Customer Sales (INTERSECT Assignment)'[Revenue]
)
     
     
#ITERATORS
% of Customer Sales (CONCATENATEX Assignment) = 
VAR AllExceptSales = 
CALCULATE(
    [Customer Sales],
    ALLEXCEPT(
        'Sales by Store',
        'Sales by Store'[store_id]
    )
)
VAR Ratio =
DIVIDE(
    [Customer Sales],
    AllExceptSales,
    BLANK()
)
RETURN
Ratio
     
     
Average Daily Sales (AVERAGEX) = 
AVERAGEX(
    'Calendar',
    [Customer Sales]
)
     
     
Average Profit (AVERAGEX) = 
AVERAGEX(
    'Calendar',
    [Profit]
)
     
     
Moving Average (AVERAGEX) = 
VAR LastTransactionDate = MAX('Calendar'[Transaction_Date])
VAR AverageDay = 30
VAR PeriodInVisual = 
FILTER(
    ALL(
        'Calendar'[Transaction_Date]
    ),
    AND(
        'Calendar'[Transaction_Date] > LastTransactionDate - AverageDay,
        'Calendar'[Transaction_Date] <= LastTransactionDate
    )
)
VAR OutPut =
CALCULATE(
    AVERAGEX(
        'Calendar',
        [Customer Sales]
    ),
    PeriodInVisual
)
RETURN
OutPut
     
     
Moving Average Profit (AVERAGEX) = 
VAR LastTransactionDate = MAX('Calendar'[Transaction_Date])
VAR AverageDay = [Average Days Value]
VAR PeriodInVisual = 
FILTER(
    ALL(
        'Calendar'[Transaction_Date]
    ),
    AND(
        'Calendar'[Transaction_Date] > LastTransactionDate - AverageDay,
        'Calendar'[Transaction_Date] <= LastTransactionDate
    )
)
VAR OutPut =
CALCULATE(
    AVERAGEX(
        'Calendar',
        [Profit]
    ),
    PeriodInVisual
)
RETURN
OutPut
     
     
Rank of Customer Sales (RANKX) = 
IF(
    HASONEVALUE(
        'Product Lookup'[product_category]
    ),
    RANKX(
        ALL(
            'Product Lookup'[product_category]
        ),
        [Customer Sales]
    )
)
     
     
Rank of Rounded Customer Sales (RANKX) = 
IF(
    HASONEVALUE(
        'Product Lookup'[product_category]
    ),
    RANKX(
        ALL(
            'Product Lookup'[product_category]
        ),
        [Rounded Customer Sales],
        ,DESC
        ,Skip
    )
)
     
     
Rounded Customer Sales = 
MROUND(
    [Customer Sales],
    100000
)
     
     
Sales by Employee Name (CONCATENATEX) = 
IF(
    HASONEVALUE(
        'Employee Lookup'[first_name]
    ),
    "Employee: " &
    CONCATENATEX(
        VALUES(
            'Employee Lookup'[first_name]
        ),
        'Employee Lookup'[first_name] &
        "-" &
        FORMAT([% of Customer Sales (CONCATENATEX Assignment)], "Percent"),
        ", ",
        'Employee Lookup'[first_name],
        ASC
    ),
    "Select a Single Employee"
)
     
     
Selected Product Category (CONCATENATEX) = 
"Showing Sales For: " &
CONCATENATEX(
    VALUES(
        'Product Lookup'[product_category]
    ),
    'Product Lookup'[product_category],
    ", ",
    'Product Lookup'[product_category],
    ASC
)
     
     
     
Top 5 Products by Profit (RANKX) = 
VAR ProfitRank =
IF(
    HASONEVALUE(
        'Product Lookup'[product_category]
    ),
    RANKX(
        ALL(
            'Product Lookup'[product]
        ),
        [Customer Sales] - [Cost]
    )
)
VAR Top5Products = 
IF(
    ProfitRank <= 5,
    [Profit]
)
Return
Top5Products
     
     
#RELATIONSHIP FUNCTIONS
Average Order Value (CWP) = 
DIVIDE(
    [Customer Sales],
    [Customers who Purchased],
    BLANK()
)
     
     
Bean % to Goal = 
DIVIDE(
    [Bean Goal (TREATAS)],
    CALCULATE(
        SUM(
            'Sales by Store'[quantity_sold]
        ),
        'Product Lookup'[product_group] = "Whole Bean/Teas"
    )
)
     
     
Bean Goal (TREATAS) = 
CALCULATE(
    SUM(
        'UNION Demo'[Bean/Teas Goal]
    ),
    TREATAS(
        SUMMARIZE(
            'Calendar',
            'Calendar'[Year_ID],
            'Calendar'[Month_Name]
        ),
        'UNION Demo'[Year],
        'UNION Demo'[Month]
    )
)
     
     
Beverage % to Goal = 
DIVIDE(
    [Beverage Goal (TREATAS)],
    CALCULATE(
        SUM(
            'Sales by Store'[quantity_sold]
        ),
        'Product Lookup'[product_group] = "Beverages"
    )
)
     
     
Beverage Goal (TREATAS) = 
CALCULATE(
    SUM(
        'UNION Demo'[Beverage Goal]
    ),
    TREATAS(
        SUMMARIZE(
            'Calendar',
            'Calendar'[Year_ID],
            'Calendar'[Month_Name]
        ),
        'UNION Demo'[Year],
        'UNION Demo'[Month]
    )
)
     
     
     
Customers who Purchased = 
CALCULATE(
    COUNTROWS(
        'Customer Lookup'
    ),
    CROSSFILTER(
        'Sales by Store'[customer_id],
        'Customer Lookup'[customer_id],
        Both
    )
)
     
     
Food % to Goal = 
DIVIDE(
    [Food Goal (TREATAS)],
    CALCULATE(
        SUM(
            'Sales by Store'[quantity_sold]
        ),
        'Product Lookup'[product_group] = "Food"
    )
)
     
     
Food Goal (TREATAS) = 
CALCULATE(
    SUM(
        'UNION Demo'[Food Goal]
    ),
    TREATAS(
        SUMMARIZE(
            'Calendar',
            'Calendar'[Year_ID],
            'Calendar'[Month_Name]
        ),
        'UNION Demo'[Year],
        'UNION Demo'[Month]
    )
)
     
     
Merchandise % to Goal = 
DIVIDE(
    [Merchandise Goal (TREATAS)],
    CALCULATE(
        SUM(
            'Sales by Store'[quantity_sold]
        ),
        'Product Lookup'[product_group] = "Merchandise"
    )
)
     
     
Merchandise Goal (TREATAS) = 
CALCULATE(
    SUM(
        'UNION Demo'[Merchandise Goal]
    ),
    TREATAS(
        SUMMARIZE(
            'Calendar',
            'Calendar'[Year_ID],
            'Calendar'[Month_Name]
        ),
        'UNION Demo'[Year],
        'UNION Demo'[Month]
    )
)
     
     
     
Number of Employees (CROSSFILTER) = 
CALCULATE(
    COUNTROWS(
        'Employee Lookup'
    ),
    CROSSFILTER(
        'Sales by Store'[staff_id],
        'Employee Lookup'[staff_id],
        Both
    )
)
     
     
Quantity Sold (USERELATIONSHIP) = 
CALCULATE(
    [SUM Quantity Sold],
    USERELATIONSHIP(
        'Food Inventory'[baked_date],
        'Calendar'[Transaction_Date]
    )
)
     
     
     
Wholesale Cost = 
SUMX(
    'Sales by Store',
    'Sales by Store'[quantity_sold] *
    RELATED(
        'Product Lookup'[current_wholesale_price]
    )
)
