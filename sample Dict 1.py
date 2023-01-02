employees=["Deviprasad","Rajesh"]
defaults={"designation":'Developer','salary':80000}
data=dict.fromkeys(employees,defaults)
print(data)
print(data["Rajesh"])
print(data["Deviprasad"])
