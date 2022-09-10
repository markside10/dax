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

