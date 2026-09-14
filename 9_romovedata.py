import pandas as pd
data={
    "name":["Aisha","Ahmed","Ali","Marium","Musfeerah","Hina","Usama","Fatimah","Zara","Bilal"],
    "age":[19,18,24,20,32,34,26,28,21,22],
    "salary":[50000,45000,39000,52000,44000,33000,30000,47000,49000,37000],
    "perfomence_score":[75,68,78,92,88,95,96,80,87,96]

}
df=pd.DataFrame(data)
print (df)
#delete a coloumns
df.drop(columns=["age"],inplace=True)
print(df)
#deletea row
df.drop(index=4,inplace=True)
print(df)