sample_dict={
    "name":"Kishore",
    "age":22,
    "salary":100000,
    "city":"New york:"}
#keys to remove
keys=["name","salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)
