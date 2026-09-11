
import pandas as pd

data = {
    "name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal", "Hina", "Usman", "Zara", "Hamza", "Fatima"],
    
    "age": [20, 21, 19, 22, 20, 23, 18, 21, 24, 19],
    
    "city": ["Karachi", "Lahore", "Islamabad", "Karachi", "Multan", "Lahore", "Karachi", "Islamabad", "Multan", "Karachi"]
}
df = pd.DataFrame(data)

print(df)
#save csv
df.to_csv("data.csv", index=False)
#save data in excel file
df.to_excel("my.xlsx", index=False)
#save data in json file
df.to_json("data.json",index=False)