% Quantity Sold to Females = 
VAR TotalOrders_Female =
CALCULATE(
    SUM(
        'Sales by Store'[quantity_sold]
    ),
    FILTER(
        'Customer Lookup',
        'Customer Lookup'[gender] = "F"
    )
)
VAR QuantitySold = 
SUM(
    'Sales by Store'[quantity_sold]
)
VAR Ratio = 
DIVIDE(
    TotalOrders_Female,
    QuantitySold,
    "-"
)
RETURN
Ratio

Cost = 
SUMX(
    'Sales by Store',                  
    'Sales by Store'[quantity_sold] *   
    RELATED(
        'Product Lookup'[current_cost]
    )
)

Customer Sales = 
SUMX(
    'Sales by Store',
    'Sales by Store'[quantity_sold] * 'Sales by Store'[unit_price]
)

Customer Sales (Last Year) = 
CALCULATE(
    [Customer Sales],
    DATEADD(
        'Calendar'[Transaction_Date],
        -1,
        Year
    )
)

Customer Sales LY (ISBLANK) = 
IF(
    ISBLANK(
        [Customer Sales (Last Year)]
    ),
    "No Sales",
    [Customer Sales (Last Year)]
)

Order by Females (Wrong) = 
VAR TotalOrder = 
SUM(
    'Sales by Store'[quantity_sold]
)
RETURN
CALCULATE(
    TotalOrder,
    FILTER(
        'Customer Lookup',
        'Customer Lookup'[gender] = "F"
    )
)

Profit = 
[Customer Sales] - [Cost]



Date Format (yyyy-mm-dd) = 
FORMAT(
    'Calendar'[Transaction_Date],
    "yyyy-mm-dd"
) 


ISNUMBER = 
ISTEXT('Calendar'[Week_Desc])


Quarter & Year = 
VAR Q1 = 'Calendar'[Month_ID] IN {1,2,3}
VAR Q2 = 'Calendar'[Month_ID] IN {4,5,6}
VAR Q3 = 'Calendar'[Month_ID] IN {7,8,9}
VAR Q4 = 'Calendar'[Month_ID] IN {10,11,12}

RETURN
SWITCH(
    TRUE(),
    Q1, "Q1" & "-" & 'Calendar'[Year_ID],
    Q2, "Q2" & "-" & 'Calendar'[Year_ID],
    Q3, "Q3" & "-" & 'Calendar'[Year_ID],
    Q4, "Q4" & "-" & 'Calendar'[Year_ID],
    "-"
)


Year Half = 
SWITCH(
    'Calendar'[Month_ID],
    1, "1H",
    2, "1H", 
    3, "1H", 
    4, "1H", 
    5, "1H", 
    6, "1H", 
    7, "2H",
    8, "2H",
    9, "2H",
    10, "2H",
    11, "2H",
    12, "2H",
    "-"
)


Current Age = 
FLOOR(    
    DATEDIFF(
        'Customer Lookup'[birthdate],
        TODAY(),
        DAY
    ) / 365.25,
    1
)

Quantity Sold (CALCULATE) = 
CALCULATE(  
    SUM(
    'Food Inventory'[quantity_sold]
    )
)

Quantity Sold (SUM) = 
SUM(
    'Food Inventory'[quantity_sold]
)


Time Group = 
FLOOR(
    'Sales by Store'[transaction_time],
    "1:00"
)


Total Revenue = 
CURRENCY(
    'Sales by Store'[quantity_sold] * 'Sales by Store'[unit_price]
) 
