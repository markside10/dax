Cost (CURRENCY) = 
ROUND(
    CURRENCY([Cost])
    ,2
)



Customer Sales LY (COALESCE) = 
VAR Customer_Sales_LY = 
CALCULATE(
    [Customer Sales],
    DATEADD(
        'Calendar'[Transaction_Date],
        -1,
        Year
    )
)
RETURN
COALESCE(
    Customer_Sales_LY,
    "-"
)


Total Customers = 
DISTINCTCOUNT(
    'Customer Lookup'[customer_id]
)


Total Employees = 
COUNTROWS(
    'Employee Lookup'
)
