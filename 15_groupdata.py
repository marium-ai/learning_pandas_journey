import pandas as pd

data = {
    "name": [
        "Marium", "Ali", "Sara", "Ahmed", "Gulnaz","Hooriya", "Usman", "Ayesha", "Musfeerah", "Bilal"],
    
    "class": [
        "ICS", "ICS", "Pre-Medical", "ICS", "Pre-Medical","Pre-Medical", "ICS", "Pre-Medical", "ICS", "Pre-Medical" ],
    
    "marks": [
        77, 23, 74, 91, 68, 45, 79, 88, 86, 72]
}

df = pd.DataFrame(data)

print(df)
result=df.groupby("class")["marks"].mean()
print(result)
#ex 2

data = {
    "name": [
        "Marium", "Ali", "Sara", "Ahmed", "Gulnaz","Hooriya", "Usman", "Ayesha", "Musfeerah", "Bilal"],
    
    "class": [
        "ICS", "ICS", "Pre-Medical", "ICS", "Pre-Medical","Pre-Medical", "ICS", "Pre-Medical", "ICS", "Pre-Medical" ],
    
    "grade": ["A1","A","A","B","C","F","B","A1","A","A1"]
}

df = pd.DataFrame(data)

print(df)
grouped = df.groupby(["class", "grade"]).size()

print("Students in each grade:")
print(grouped)
percentage = (
    df.groupby(["class", "grade"]).size()
    / df.groupby("class")["name"].count()
    * 100
)

print("\nPercentage:")
print(percentage)