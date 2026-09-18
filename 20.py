import pandas as pd

data = {
    "customer_id": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115
    ],

    "customer": [
        "Aisha", "Ahmed", "Sara", "Waqas", "Marium",
        "Ali", "Hina", "Usman", "Fatima", "Bilal",
        "Zara", "Hamza", "Sana", "Danish", "Areeba"
    ],

    "category": [
        "Electronics", "Clothing", "Beauty", "Electronics", "Books",
        "Clothing", "Beauty", "Books", "Electronics", "Clothing",
        "Beauty", "Electronics", "Books", "Clothing", "Beauty"
    ],

    "product": [
        "Headphones", "Hoodie", "Face Wash", "Keyboard", "Python Book",
        "T-Shirt", "Lip Balm", "Novel", "Mouse", "Jeans",
        "Sunscreen", "Smart Watch", "AI Book", "Jacket", "Perfume"
    ],

    "price": [
        4500, 3200, 1200, 2800, 1800,
        2200, 850, 1500, 1900, 3500,
        1600, 7500, 2200, 4200, 3000
    ],

    "rating": [
        4.5, 4.0, 4.8, 4.2, 4.7,
        3.9, 4.6, 4.1, 4.3, 4.0,
        4.9, 4.4, 4.8, 3.8, 4.5
    ],

    "payment_method": [
        "Card", "Cash", "Card", "Bank Transfer", "Cash",
        "Card", "Cash", "Card", "Bank Transfer", "Cash",
        "Card", "Card", "Cash", "Bank Transfer", "Card"
    ],

    "city": [
        "Karachi", "Lahore", "Karachi", "Islamabad", "Karachi",
        "Lahore", "Karachi", "Islamabad", "Karachi", "Lahore",
        "Karachi", "Islamabad", "Karachi", "Lahore", "Karachi"
    ],

    "returned": [
        "No", "Yes", "No", "No", "No",
        "Yes", "No", "No", "Yes", "No",
        "No", "Yes", "No", "Yes", "No"
    ]
}

df = pd.DataFrame(data)

# Save files
df.to_csv("orders.csv", index=False)
df.to_excel("orders.xlsx", index=False)

# Total orders
print("\nTotal orders:")
print(df.shape[0])

# Orders by category
print("\nOrders by category:")
print(df["category"].value_counts())

# Orders by city
print("\nOrders by city:")
print(df["city"].value_counts())

# Average price
print("\nAverage product price:")
print(df["price"].mean())

# Returned products
returned_count = (df["returned"] == "Yes").sum()
print("\nReturned products:")
print(returned_count)

# Payment methods
print("\nPayment methods:")
print(df["payment_method"].value_counts())

# Average price by category
print("\nAverage price by category:")
print(df.groupby("category")["price"].mean())

# Orders by category using groupby
print("\nOrders by category:")
print(df.groupby("category").size())

# Total price by category
print("\nTotal price by category:")
print(df.groupby("category")["price"].sum())

# Sort by rating
print("\nProducts sorted by rating:")
print(df.sort_values("rating", ascending=False))

# Check missing values
print("\nMissing values:")
print(df.isna().sum())

# Most expensive product
print("\nMost expensive product:")
print(df.loc[df["price"].idxmax()])