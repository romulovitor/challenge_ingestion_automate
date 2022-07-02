SELECT region
FROM coordinate
WHERE datasource = 'cheap_mobile'

SELECT region,
RANK() OVER (
    PARTITION BY regions
    ORDER BY datetime DESC
)
FROM  coordinate
LIMIT 2