import pandas as pd

# Data
data = {
    "Date": [
        "2026-09-01", "2026-09-02", "2026-09-03", "2026-09-04", "2026-09-05",
        "2026-09-06", "2026-09-07", "2026-09-08", "2026-09-09", "2026-09-10",
        "2026-09-11", "2026-09-12", "2026-09-13", "2026-09-14", "2026-09-15"
    ],

    "Tool": [
        "ChatGPT", "Gemini", "Claude", "ChatGPT", "Copilot",
        "Gemini", "ChatGPT", "Claude", "Copilot", "ChatGPT",
        "Gemini", "Claude", "ChatGPT", "Copilot", "Gemini"
    ],

    "Task": [
        "Coding", "Research", "Writing", "Debugging", "Coding",
        "Study", "Research", "Coding", "Debugging", "Study",
        "Writing", "Research", "Coding", "Coding", "Study"
    ],

    "Time_Minutes": [
        45, 30, 25, 60, 40,
        35, 50, 55, 30, 40,
        20, None, 70, 45, 25
    ],

    "Success": [
        "Yes", "Yes", "Yes", "Yes", "No",
        "Yes", "Yes", "Yes", "No", "Yes",
        "Yes", "Yes", "Yes", "No", "Yes"
    ],

    "Rating": [
        5, 4, 5, 5, 3,
        4, 5, 4, 2, 5,
        4, 5, None, 3, 4
    ]
}

df = pd.DataFrame(data)

print(df)

# Save messy data in CSV and Excel files
df.to_csv("ai_usage.csv", index=False)
df.to_excel("ai_usage.xlsx", index=False)

# Print first 5 rows of data
print(df.head())

# Display information about the DataFrame
print(df.info())

# Statistical information
print("Statistical information")
print(df.describe())

# Find the number of NaN values
print("Number of NaN values")
print(df.isnull().sum())

# Cleaning data
df["Time_Minutes"] = df["Time_Minutes"].fillna(
    df["Time_Minutes"].mean()
)

df["Rating"] = df["Rating"].fillna(
    df["Rating"].mean()
)

# Save cleaned data
df.to_csv("cleaned_ai_usage.csv", index=False)
df.to_excel("cleaned_ai_usage.xlsx", index=False)

print("Data after cleaning")
print(df)