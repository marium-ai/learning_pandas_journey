import pandas as pd
data={
    "name":["Aisha","Ahmed","Ali","Marium","Musfeerah","Hina","Usama","Fatimah","Zara","Bilal"],
    "age":[19,18,24,20,32,34,26,28,21,22],
    "salary":[50000,45000,39000,52000,44000,33000,30000,47000,49000,37000],
    "perfomence_score":[75,68,78,92,88,95,96,80,87,96]

}
df=pd.DataFrame(data)
print(df)
#single columns return series
name=df["name"]
print(name)
#multile colmuns
ss=df[["name","age"]]
print(ss)
#filtering rows
high_salry=df[df["salary"]>40000]
print("the employes with 40000+ salry are")
print(high_salry)
#filtering multoples rows
#using or condition
print("employes with 25+or salry 40000+")
f_or=df[(df["age"]>25)|(df["salary"]>40000)]
print(f_or)
#using and comdition
f_and=df[(df["salary"]>45000)&(df["perfomence_score"]>=75)]
print("employes with  salary 35000+ and score wth 75+ are:")
print(f_and)