set1={10,20,30,40,50}
set2={30,40,50,60,70}
print(set1.intersection(set2))


print(set1.union(set2))
#remove duplicates.
print(set1^set2)


set1.difference_update(set2)
print(set1)

set3={10,20,30,40,50}
set3.difference_update({10,20,30,35})
print(set3)
