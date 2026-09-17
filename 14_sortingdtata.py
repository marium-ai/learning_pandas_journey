import pandas as pd

data={
    "name":["Marium","Gulnaz","musfeerah","Hooriya"],
    "age":[19,15,18,17],
    "marks":[77,74,86,85]

}
df=pd.DataFrame(data)
print("data befor sorting")
print(df)
df.sort_values(
    by=["name", "age"],
    ascending=[True, True],
    inplace=True
)
print("\nafter sorting")
print(df)