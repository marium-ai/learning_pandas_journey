import pandas as pd

df = pd.read_csv("data.csv")
print(df)

df = pd.read_json("data.json")
print(df)

df=pd.read_excel("my.xlsx")
print(df)