import pandas as pd
data={
    "name":["Aisha","Ahmed",None,"Marium","Musfeerah","Hina","Usama","Fatimah","Zara","Bilal"],
    "age":[19,18,None,20,32,34,26,28,21,22],
    "salary":[50000,45000,None,52000,44000,33000,30000,47000,49000,37000],
    "perfomence_score":[75,68,None,92,88,95,96,80,87,96]

}
#deleting NAN VALUE
df=pd.DataFrame(data)
print (df)
df.dropna(axis=0,inplace=True)
print(df)
df.to_csv("ai_usage.csv",index=False)
