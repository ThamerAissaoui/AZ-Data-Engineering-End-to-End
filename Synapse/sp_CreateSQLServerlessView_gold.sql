USE gold_db
GO
CREATE OR ALTER PROC CreateSQLServerlesView_gold @ViewName NVARCHAR(100)
AS
BEGIN

DECLARE @statement VARCHAR(MAX)
   SET @statement = N'CREATE OR ALTER VIEW ' + @ViewName + ' AS
      SELECT *
      FROM
        OPENROWSET(
        BULK ''https://thameurdatalakegen2.dfs.core.windows.net/gold/SalesLT/' + @ViewName + '/'',
        FORMAT = ''DELTA''
    ) AS [result]

    '
       
EXEC (@statement)

END
GO
