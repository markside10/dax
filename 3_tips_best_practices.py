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
