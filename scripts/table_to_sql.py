from pathlib import Path
import pandas as pd

file_name = 'flights/flights.parquet'
table_name = Path(file_name).stem
df = pd.read_parquet(file_name)
schema = ', '.join([f'{col} {dtype}' for col, dtype in df.dtypes.items()])
create_table_sql = f'CREATE TABLE {table_name} ({schema})'
print(create_table_sql)
