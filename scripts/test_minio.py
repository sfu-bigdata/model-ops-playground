import pandas as pd
import s3fs

s3 = s3fs.S3FileSystem(
    endpoint_url='http://localhost:9000',
    key='trino',
    secret='trino123',
    )

with s3.open('s3a://datalake/flights/flights.parquet', 'rb') as f:
    df = pd.read_parquet(f)

with pd.option_context('display.max_columns', None):
    print(df.dtypes)
#    print(df.head())
#    print(df.min())
