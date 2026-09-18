import pandas as pd

student1 = pd.DataFrame({
    "name": ["Aisha", "Ahmed"],
    "grade": ["A", "B"]
})

student2 = pd.DataFrame({
    "name": ["Waqas", "Sara"],
    "grade": ["A", "C"]
})

result = pd.concat([student1, student2])

print(result)