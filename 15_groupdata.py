import pandas as pd

data = {
    "name": [
        "Marium", "Ali", "Sara", "Ahmed", "Gulnaz","Hooriya", "Usman", "Ayesha", "Musfeerah", "Bilal"],
    
    "class": [
        "ICS", "ICS", "Pre-Medical", "ICS", "Pre-Medical","Pre-Medical", "ICS", "Pre-Medical", "ICS", "Pre-Medical" ],
    
    "marks": [
        77, 23, 74, 91, 68, 45, 79, 88, 86, 74]
}

df = pd.DataFrame(data)

print(df)
result=df.groupby(["class","marks"])["marks"].mean()
print(result)