import pandas as pd
student=pd.DataFrame({
    'id':[1,2,3,4],
    "name":["marium","aisha","ahmed","hania"]
})
grades=pd.DataFrame({
    "id":[1,5,3,4],
    "grade":["A","A1","B","C"]
})
#linear
result = pd.merge(student, grades, on="id",how="inner")
print("\ninner merge")
print(result)

result=pd.merge(student,grades,on="id",how="left")
print('\nleft merge')
print(result)


result = pd.merge(student, grades, on="id",how="right")
print("\nright merge")
print(result)

result=pd.merge(student,grades,on="id",how="outer")
print("\nouter merge")
print(result)