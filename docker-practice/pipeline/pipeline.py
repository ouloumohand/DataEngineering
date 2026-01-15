#passing argument to command line
import sys

print("arguments", sys.argv)

month = int(sys.argv[1])
print(f"Running pipeline for month {month}")

#using pamdas
#import sys
import pandas as pd

df = pd.DataFrame({"bikes": [1, 2], "NumberBikes": [3, 4]})
df['Month'] = month
print(df.head())

df.to_parquet(f"output_day_{month}.parquet")