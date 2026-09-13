import pandas as pd
df=pd.read_csv("data.csv")
print("starting 5 rows")
print(df.head(5))

print("last 5 rows")
print(df.tail(5))

#uderstanding data
print(df.info())
