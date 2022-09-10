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
