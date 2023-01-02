sample_dict={
    "name":"Kishore",
    "age":22,
    "salary":100000,
    "city":"New york:"
    }
keys=["name","salary"]

d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
print(d)



