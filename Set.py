samplelist=[1,2,3,4,5,6,7,8,9,10]
print(samplelist)
sampleset=set(samplelist)
print(sampleset)
a=10,9,8,7,6,5,4,3,2,1
#print(sampleset[6])
#sets are not indexable
#check if an element exists in the set
if 11 in sampleset:
    print("Yes")
else:
    print("No")
newset=set([])
newset.add(11)
newset.add(12)
newset.add(13)
newset.add(14)
newset.add(15)
print(newset)
