import pandas as pd

# Simple interpolation
data = {
    "name": ["Ali", "Sara", "Ahmed", "Aisha"],
    "age": [20, None, None, 26]
}

df = pd.DataFrame(data)

print("Before interpolation:")
print(df)

df["age"] = df["age"].interpolate()

print("\nAfter interpolation:")
print(df)


# Linear interpolation
data2 = {
    "name": ["Ali", "Sara", "Ahmed", "Aisha"],
    "age": [20, 21, None, 23]
}

df2 = pd.DataFrame(data2)

print("\nBefore linear interpolation:")
print(df2)

df2["age"] = df2["age"].interpolate(method="linear")

print("\nAfter linear interpolation:")
print(df2)
#polinomial
data3 = {
    "day": [1, 2, 3, 4],
    "marks": [1, 4, None, 16]
}

df3 = pd.DataFrame(data3)
print("\nBefore polinomial interpolation")
print(df3)
df3["marks"] = df3["marks"].interpolate(
    method="polynomial",
    order=2
)
print("\n After polynomial interpoalation")
print(df3)