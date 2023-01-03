##a={10,20,30,40,50}
##b={30,40,50,60,70}
##print(a-b)
##print(b-a)
##
##print(a.symmetric_difference(b)) #a-b union b-a

##set1={10,20,30,40,50}
##set2={30,40,50,60,70}
##if set1.isdisjoint(set2):
##    print("Two sets have no items in common")
##else:
##    print("Two sets have items in common")
##    print(set1.intersection(set2))
##    
    
set1={10,20,30,40,50}
set2={30,40,50,60,70}
#set1.symmetric_difference_update(set2)
set1.intersection_update(set2)
print(set1)
