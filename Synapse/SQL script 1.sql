CREATE VIEW address
AS
SELECT
     *
FROM
    OPENROWSET(
        BULK 'https://thameurdatalakegen2.dfs.core.windows.net/gold/SalesLT/Address/',
        FORMAT = 'DELTA'
    ) AS [result]
