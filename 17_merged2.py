import pandas as pd
student=pd.DataFrame({
    "name":["aisha","ahmed","waqas"]

})
subjects = pd.DataFrame({
    "subject": ["Python", "Pandas"]
})
resut=pd.merge(student,subjects,how="cross")
print(resut)