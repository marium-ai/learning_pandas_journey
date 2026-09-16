import pandas as pd
data={
    "name":["Ali","Sara",'Ahmed',"Aisha"],
    "age":[20,21,None,23]

}
df=pd.DataFrame(data)
print(df)

df["age"]=df["age"].interpolate()
print(df)