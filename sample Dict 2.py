sample_dict={
    "name":"Kishore",
    "age":22,
    "salary":100000,
    "city":"New york:"}
keys=["name","salary"]


newDict={}
for i in keys:
    newDict[i]=sample_dict[i]

print(newDict)


newDict={i:sample_dict[i] for i in keys }
print(newDict)



res=dict()
for k in keys:
    res.update({k:sample_dict[k]})
print(res)
